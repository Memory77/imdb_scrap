La différence entre la nécessité d'utiliser des identifiants de connexion (comme le nom d'utilisateur et le mot de passe) pour PostgreSQL et leur absence pour SQLite provient de la conception et de l'utilisation prévues de ces systèmes de gestion de base de données (SGBD).

SQLite
Conception intégrée: SQLite est conçu pour être léger et autonome, sans nécessiter un serveur de base de données séparé. Il stocke l'ensemble de la base de données (définitions, tables, index, et les données elles-mêmes) dans un seul fichier sur le disque.
Pas de configuration de l'utilisateur: Il n'y a pas de concept d'utilisateurs ou de rôles dans SQLite. L'accès à la base de données est contrôlé par les permissions du système de fichiers de l'OS sur le fichier de la base de données. Cela signifie qu'il n'est pas nécessaire de spécifier un nom d'utilisateur ou un mot de passe pour se connecter à une base de données SQLite ; l'accès au fichier détermine l'accès à la base de données.

PostgreSQL
Système client-serveur: PostgreSQL est un SGBD relationnel avancé qui fonctionne selon un modèle client-serveur. Cela signifie que le serveur de base de données PostgreSQL fonctionne comme un processus séparé qui gère la base de données, et les clients communiquent avec le serveur pour interroger ou modifier les données.
Gestion des utilisateurs et des rôles: PostgreSQL gère les connexions, les permissions, et la sécurité au niveau du serveur de base de données, avec des concepts détaillés d'utilisateurs (parfois appelés rôles). Pour se connecter à une base de données PostgreSQL, un client doit fournir des identifiants valides (nom d'utilisateur et mot de passe), qui sont vérifiés par le serveur.
