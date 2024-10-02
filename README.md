une API RESTful simple pour la gestion de livres. 

Voici quelques problématiques courantes et comment cette API les résout :

Problématique : Récupération de données
Solution : L'endpoint GET /books renvoie la liste de tous les livres.

Problématique : Récupération d'un élément spécifique
Solution : L'endpoint GET /books/<int:book_id> permet de récupérer un livre par son ID.

Problématique : Ajout de nouvelles données
Solution : L'endpoint POST /books permet d'ajouter un nouveau livre à la liste.

# executer le script
python run.py

# pour utiliser les méthodes de l'API dans un terminal shell
# Obtenir tous les livres

curl http://localhost:5000/books

# Obtenir un livre spécifique
curl http://localhost:5000/books/1

# Ajouter un nouveau livre
curl -X POST -H "Content-Type: application/json" -d '{"title":"Dune","author":"Frank Herbert"}' http://localhost:5000/books

# En mode sécurisé
curl -H "X-API-Key: my-key" http://127.0.0.1:5000/books
extension : chrome:POSTMAN firefox:RESTED

# via navigateur
http://127.0.0.1/books