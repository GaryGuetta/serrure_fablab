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
├── dashboard.html      # Page d'affichage des infos et logs
├── Raspberry/
│   ├── RC522.py        # Programmation du module RC522 sans les infos du serveur en ligne
│   └── VF.py           # Programmation complet du système, avec le serveur
├── css/
│   ├── style.css       # Styles généraux et mise en page
│   └── logs.css        # Styles spécifiques au tableau des logs
└── README.md
