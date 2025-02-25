Les technologies derrière l'API
===============================

Language de programmation
-------------------------

Cette API est dévellopée en python, ce language est un language de programmation interprété
Pour plus d'information sur le language veuillez aller sur ce `site <https://www.python.org>`_

Framework de développement
--------------------------

Pour le dévellopement de l'API a été utilisé le framework Django,
Ce framework permet le dévellopement d'API web de façon claire et organiséen

Vous trouverez plus d'information sur le `site officiel <https://www.djangoproject.com>`_

Outils et technologies
----------------------

**Test**

Dans un soucis de sécurité chaque fonction du projet est testée, ici avec les outils de test fournis par Django
Ils permettent d'assurer un bon fonctionnement de l'application et que aucun bug ne vienne entraver l'utilisateur

**Propreté du code**

Afin que vous puissiez comprendre le programme, il respecte les normes de la PEP8
Pour s"en assurer l'outil flake8 a été utilisé et permet de vérifier en une simple commande
que l'intégralité de notre code est propre

**CI/CD**

Afin d'obtenir une application disponible a tous, en ligne le développement d'un pipeline CI/CD
a été nécessaire
Pour cela l'utilisation de github action a été privilégiée
Cela permet de lancer un script d'intégration a chaque push sur la branche master de créer une image `Docker <https://www.docker.com/get-started/>`_
et enfin de déclencher le déploiement sur Render
Vous pouvez trouver plus d'information dans la section déploiement de cette documentation

**Enregistrement des erreurs**

Pour assurer une maintenabilité du code, chaque erreur qui serai non gérée est stockée sur Sentry ce qui permet un suivi correct de toute anomalie sur l'application