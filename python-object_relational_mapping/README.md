## Bases de données et Python : Connexion avec MySQL et utilisation d'un ORM avec SQLAlchemy

### Introduction
Dans ce projet, nous allons lier deux mondes incroyables : les bases de données et le langage Python. 

La première partie se concentre sur l'utilisation du module **MySQLdb** pour se connecter à une base de données MySQL et exécuter des requêtes SQL. 
La seconde partie introduit **SQLAlchemy**, un ORM (*Object Relational Mapper*) qui permet d'abstraire les bases de données et de manipuler des objets Python au lieu d'écrire des requêtes SQL.

L'ORM simplifie la gestion des bases de données en transformant les tables en classes Python et les lignes en objets. Plus besoin d'écrire des requêtes SQL complexes : les opérations CRUD sont effectuées avec du code Python lisible et intuitif.

---

### Partie 1 : Connexion à MySQL avec MySQLdb

#### Installation de MySQLdb
```bash
pip install mysqlclient
```

#### Connexion à la base de données
```python
import MySQLdb

# Connexion à la base de données
conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    db="my_db",
    charset="utf8"
)

# Création d'un curseur
cur = conn.cursor()
```

#### Sélectionner des lignes dans une table MySQL
```python
# Exécution d'une requête SQL SELECT
cur.execute("SELECT * FROM states ORDER BY id ASC")

# Récupération des résultats
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
```

#### Insérer des lignes dans une table MySQL
```python
# Requête SQL INSERT
cur.execute("INSERT INTO states (name) VALUES (%s)", ("New State",))

# Valider la transaction
conn.commit()
```

#### Fermeture du curseur et de la connexion
```python
cur.close()
conn.close()
```

### Partie 2 : Utilisation de SQLAlchemy

#### Installation de SQLAlchemy
```bash
pip install SQLAlchemy
```

#### Qu'est-ce qu'un ORM ?
Un ORM (*Object Relational Mapper*) est un outil permettant de faire le lien entre des bases de données relationnelles (comme MySQL) et des objets Python. Plutôt que d'écrire des requêtes SQL, on manipule des classes et des objets Python, rendant le code plus lisible et indépendant du système de base de données.

#### Configuration de la base avec SQLAlchemy
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Création de l'engine
engine = create_engine('mysql+mysqldb://root:root@localhost/my_db', pool_pre_ping=True)

# Création de la base de métadonnées
Base = declarative_base()
```

#### Mapper une classe Python sur une table MySQL
```python
# Définition d'un modèle
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

# Création des tables
Base.metadata.create_all(engine)
```

#### Création d'une session
```python
Session = sessionmaker(bind=engine)
session = Session()
```

#### Sélectionner des lignes avec SQLAlchemy
```python
for state in session.query(State).order_by(State.id).all():
    print(f"{state.id}: {state.name}")
```

#### Insérer des lignes avec SQLAlchemy
```python
new_state = State(name="New State")
session.add(new_state)
session.commit()
```

#### Fermeture de la session
```python
session.close()
```

### Différences entre SQL natif et ORM
| Critère             | SQL natif (MySQLdb) | ORM (SQLAlchemy)     |
|---------------------|--------------------|---------------------|
| Syntaxe              | Requêtes SQL directes | Manipulation d'objets |
| Courbe d'apprentissage | Facile si on connaît SQL | Syntaxe ORM à apprendre |
| Maintenance         | Dépendante du type de base | Indépendante du stockage |
| Lisibilité          | Mélange SQL/Python | Code Python pur     |

### Ressources utiles
- [Object Relational Mappers (ORMs)](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [Documentation MySQLdb](https://mysqlclient.readthedocs.io/)
- [Tutoriel SQLAlchemy](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [SQLAlchemy 101](https://overiq.com/sqlalchemy-101/)
- [SQLAlchemy ORM Tutorial](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)

---

En maîtrisant ces deux approches, vous serez capable de choisir entre la flexibilité des requêtes SQL natives et la puissance d'abstraction offerte par SQLAlchemy. Bonne pratique !

