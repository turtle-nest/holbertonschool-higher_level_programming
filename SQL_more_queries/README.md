## Comment créer un nouvel utilisateur MySQL

Pour créer un nouvel utilisateur dans MySQL, vous devez avoir des privilèges d'administrateur ou de super-utilisateur. Voici la commande de base :

```sql
CREATE USER 'nom_utilisateur'@'localhost' IDENTIFIED BY 'mot_de_passe';
```

- `nom_utilisateur` : Le nom du nouvel utilisateur.
- `localhost` : Indique que l'utilisateur ne peut se connecter qu'à partir de la machine locale.
- `mot_de_passe` : Le mot de passe associé à cet utilisateur.

Exemple :

```sql
CREATE USER 'test_user'@'localhost' IDENTIFIED BY 'password123';
```

## Comment gérer les privilèges d'un utilisateur sur une base ou une table

Les privilèges permettent de définir les actions qu'un utilisateur peut effectuer sur une base de données ou une table spécifique.

### Accorder des privilèges

```sql
GRANT ALL PRIVILEGES ON nom_base_de_donnees.* TO 'nom_utilisateur'@'localhost';
```

Exemple :

```sql
GRANT SELECT, INSERT, UPDATE ON mydb.* TO 'test_user'@'localhost';
```

### Révoquer des privilèges

```sql
REVOKE INSERT ON mydb.* FROM 'test_user'@'localhost';
```

### Appliquer les changements

```sql
FLUSH PRIVILEGES;
```

## Qu'est-ce qu'une PRIMARY KEY

Une clé primaire est une contrainte qui identifie de manière unique chaque enregistrement d'une table. Elle ne peut contenir que des valeurs uniques et ne peut pas être NULL.

```sql
CREATE TABLE utilisateurs (
    id INT AUTO_INCREMENT,
    nom VARCHAR(100),
    email VARCHAR(100),
    PRIMARY KEY (id)
);
```

## Qu'est-ce qu'une FOREIGN KEY

Une clé étrangère établit une relation entre deux tables. Elle garantit l'intégrité référentielle des données.

```sql
CREATE TABLE commandes (
    id INT AUTO_INCREMENT,
    utilisateur_id INT,
    produit VARCHAR(100),
    PRIMARY KEY (id),
    FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs(id)
);
```

## Contraintes NOT NULL et UNIQUE

- **NOT NULL** : Empêche une colonne d'accepter des valeurs NULL.
- **UNIQUE** : Assure que toutes les valeurs d'une colonne sont uniques.

```sql
CREATE TABLE produits (
    id INT AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    code_produit VARCHAR(50) UNIQUE,
    PRIMARY KEY (id)
);
```

## Comment récupérer des données de plusieurs tables en une seule requête

On utilise les **JOINS** pour récupérer des données à partir de plusieurs tables.

```sql
SELECT utilisateurs.nom, commandes.produit
FROM utilisateurs
JOIN commandes ON utilisateurs.id = commandes.utilisateur_id;
```

## Que sont les sous-requêtes (subqueries)

Une sous-requête est une requête imbriquée dans une autre requête.

```sql
SELECT nom
FROM utilisateurs
WHERE id IN (
    SELECT utilisateur_id
    FROM commandes
    WHERE produit = 'Ordinateur'
);
```

## Différence entre JOIN et UNION

- **JOIN** : Combine les lignes de deux tables basées sur une condition commune.

```sql
SELECT utilisateurs.nom, commandes.produit
FROM utilisateurs
JOIN commandes ON utilisateurs.id = commandes.utilisateur_id;
```

- **UNION** : Combine les résultats de deux requêtes en supprimant les doublons.

```sql
SELECT nom FROM utilisateurs
UNION
SELECT nom_client FROM clients;
```

