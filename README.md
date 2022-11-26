# forest-main
# Django Forest

An app to catalog things in the forest including animals and trees. Trees can be added to a park through a one to many relationship. Created using Python, Django, Postgres.

## Routes Tables
### Animal Routes

| Verb   | URI Pattern     | Controller#Action  |
|--------|-----------------|--------------------|
| POST   | `/animals`         | `animals#create`      |
| GET    | `/animals/` | `animals#index`        |
| GET    | `/animals/:animalId` | `animals#show`        |
| PATCH  | `/animal/:animalId` | `animal#update`      |
| DELETE | `/animal/:animalId` | `animal#delete`      |

### Tree Routes

| Verb   | URI Pattern     | Controller#Action  |
|--------|-----------------|--------------------|
| POST   | `/trees`| `trees#create`|
| GET    | `/trees/`|`trees#index`|
| GET    | `/trees/:treeId` | `trees#show`|
| PATCH  | `/tree/:treeId` | `tree#update`|
| DELETE | `/tree/:treeId` | `tree#delete`|


## Starting Instructions

`pip3 install --upgrade pip`
`pip install pipenv`
`pipenv shell`
`pipenv install django==4.1 psycopg2-binary`
`python manage.py runserver`