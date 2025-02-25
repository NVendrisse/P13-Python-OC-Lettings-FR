Déploiement
===========

Le déploiement de l'application est automatisé sur la plateforme Github Action

Pour cela un script de CI/CD a été mis en place

Il permet l'execution des tests et le linting a chaque push de l'application

Cependant ce déploiement n'a lieu que si le push se fait sur la branche master du dépot Github 

Mise en ligne
-------------

Le site est actuellement hébergé sur Render

A chaque mise a jour de l'image Docker, un hook permet un déploiment immédiat de la nouvelle version du site

