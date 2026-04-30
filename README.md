# 🚪 Système de Gestion d'Accès - Fablab

Ce projet propose une interface web (HTML/CSS) permettant de gérer l'accès à une porte connectée de Fablab. Il comprend une interface de connexion sécurisée et un tableau de bord pour visualiser les informations d'état et l'historique des accès (logs).

## 📋 Aperçu du projet

L'objectif est de fournir une interface utilisateur fluide pour :
1. **S'authentifier** avant d'accéder aux commandes de la porte.
2. **Surveiller l'état** de la porte (Ouverte / Fermée).
3. **Consulter les logs** (Historique des passages) pour savoir qui a accédé au lab et à quelle heure.

## 🚀 Fonctionnalités

- 🔐 **Page de Connexion :** Interface moderne et responsive pour l'authentification des membres.
- 📊 **Dashboard d'Informations :** Affichage en temps réel de l'état du système.
- 📜 **Journal des Logs :** Liste chronologique des ouvertures et fermetures de la porte.
- 🎨 **Design Moderne :** Utilisation de CSS moderne (Flexbox/Grid) avec un style épuré adapté aux environnements tech.

## 📂 Structure du projet

```text
├── index.html          # Page de connexion (Login)
├── dashboard.html      # Page d'affichage des infos et logs
├── css/
│   ├── style.css       # Styles généraux et mise en page
│   └── logs.css        # Styles spécifiques au tableau des logs
└── README.md
