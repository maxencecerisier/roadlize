# Roadlize

Roadlize est une application qui permet aux utilisateurs de trouver facilement et rapidement des prestataires de services indépendants pour effectuer des modifications sur leur véhicule.

## Technologies utilisées

- Django pour le backend
- Django Rest Framework pour l'API
- MySQL pour la base de données
- Flutter pour le frontend
- Stripe pour les paiements

## Installation

1. Clonez ce dépôt :
    ```
    git clone https://github.com/username/roadlize.git
    ```

2. Lancez le projet :
    ```
    docker-compose up
    ```
    
3. Si besoin, appliquez les modifications :
    ```
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
    ```

## Développement

Pour ajouter de nouvelles fonctionnalités à l'application, créez une nouvelle branche et faites un pull request une fois que vous avez terminé.

## Tests

Pour exécuter les tests, utilisez la commande suivante :
    ```
    python manage.py test
    ```

## Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez ce dépôt
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request
