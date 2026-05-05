# 🚪 Système de Gestion d'Accès - Fablab

Ce projet propose une interface web (HTML/CSS) permettant de gérer l'accès à une porte connectée de Fablab. Il comprend une interface de connexion sécurisée et un tableau de bord pour visualiser les informations d'état et l'historique des accès (logs).
Il comprend également le développement de la partie logicielle du microcontrôlleur Raspberry PI 2. 

## 🚀 Fonctionnalités

- 🔐 **Page de Connexion :** Interface moderne et responsive pour l'authentification des membres.
- 📊 **Dashboard d'Informations :** Affichage en temps réel du nombre d'ouverture de la porte du Fablab.
- 📟 **Raspberry :** Code utilisé pour le système, sans et avec l'tuilisation du serveur en ligne
- 📜 **Journal des Logs :** Historique chronologique des badgeages.

## 📂 Structure du projet

```text
├── index.html          # Page de connexion (Login)
├── logs.html           # Page d'affichage des logs
├── people.html         # Page gérant l'accés au fablab
├── Raspberry/
│   ├── RC522.py        # Programmation du module RC522 (Local)
│   └── VF.py           # Programmation complète (Serveur)
├── css/
│   ├── style.css       # Styles généraux
│   ├── logs.css        # Styles pour le tableau des logs
│   └── people.css      # NOUVEAU : Styles pour la gestion des membres
└── README.md
