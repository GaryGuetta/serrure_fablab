#!/usr/bin/env python3
#
#  supabaseV2
#  
#  Copyright 2026 paull <paull@CITRONNELLE>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests
import time

GPIO.setwarnings(False)

# === CONFIG ===
RELAY = 17
BUTTON = 27

GPIO.setmode(GPIO.BCM)

# Relais
GPIO.setup(RELAY, GPIO.OUT)
GPIO.output(RELAY, GPIO.LOW)

# Bouton avec pull-up interne
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

reader = SimpleMFRC522()

# === SUPABASE ===
SUPABASE_URL = "https://fjksprfocmyqebjfxftf.supabase.co/rest/v1/users"
API_KEY = "sb_publishable_A3J91eJqawcbb2s6a-8vRQ_9bOFqaE_"

headers = {
    "apikey": API_KEY,
    "Authorization": f"Bearer {API_KEY}"
}

def open_door():
    print("OUVERTURE PORTE")
    GPIO.output(RELAY, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(RELAY, GPIO.LOW)

def check_access(uid):
    try:
        url = f"{SUPABASE_URL}?uid=eq.{uid}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return len(response.json()) > 0

        return False

    except Exception as e:
        print("Erreur reseau:", e)
        return False

print("Systeme pret (RFID + bouton sortie)")

try:
    while True:

        # === GESTION BOUTON ===
        if GPIO.input(BUTTON) == GPIO.LOW:
            print("Bouton sortie appuye")
            open_door()
            time.sleep(1)  # anti-rebond

        # === GESTION RFID ===
        print("Approche une carte...")
        uid, text = reader.read()
        uid = int(uid)

        print("UID detecte:", uid)

        if check_access(uid):
            print("ACCES AUTORISE")
            open_door()
        else:
            print("ACCES REFUSE")

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
