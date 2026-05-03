#!/usr/bin/env python3
#
#  RC552.py
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

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

# GPIO relais
RELAY = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY, GPIO.OUT)
GPIO.output(RELAY, GPIO.LOW)

reader = SimpleMFRC522()

# Liste des badges autorises
AUTHORIZED = [
    182744188615,
]

print("Systeme pret. Passe une carte...")

try:
    while True:
        id, text = reader.read()
        print("UID detecte :", id)

        if id in AUTHORIZED:
            print("ACCES AUTORISE")
            
            GPIO.output(RELAY, GPIO.HIGH)  # ouvre porte
            time.sleep(3)
            GPIO.output(RELAY, GPIO.LOW)   # referme

        else:
            print("ACCES REFUSE")

        time.sleep(1)

except KeyboardInterrupt:
    print("Arret")
    GPIO.cleanup()
