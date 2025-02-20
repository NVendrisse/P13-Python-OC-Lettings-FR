Installation
============

Cloner le repository github
---------------------------

Afin de récuperer le code de l'application utilisez la commande suivante
(Dans le dossier de votre choix)

``git clone https://github.com/NVendrisse/P13-Python-OC-Lettings-FR.git``

Installer les modules nécessaires
---------------------------------

**Windows**

``cd ..\P13-Python-OC-Lettings-FR
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
``
**OSx et Linux**

``cd ..\P13-Python-OC-Lettings-FR
python -m venv env
env/bin/activate
pip install -r requirements.txt
``

Disclaimer sur les modifications
--------------------------------

Pour toutes modifications apportées au projet, merci de bien veiller a travailler sur une branche 
séparée de la branche master, en effet la branche master étant automatiquement déployée,
nous ne voudrions pas que des bugs viennent entacher le site web
De plus si de nouvelles fonctions sont ajoutées n'oubliez pas de les tester car aucun déploiement 
n'aura lieu si moins de 80% de l'application est testée
