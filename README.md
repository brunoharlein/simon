# Application de jeu type Simon pour terminal en python orienté objet

Il s'agit d'une application développée dans le cadre de mon poste de formateur en programmation et plus particulièrement pour l'élaboration d'un programme d'apprentissage du python. L'objectif est que les apprenants produisent une application orientée objet fonctionnelle dans le terminal qui simule le célèbre jeux Simon. La seule différence est qu'au lieu d'afficher des couleurs, ici le jeu affiche des nombres.

Au travers de cet exercice, ils apprennent à :
- Organiser une applications en modules
- Respecter la logique du pattern MVC
- Déclarer et instancier des classes
- Déclarer et utiliser des attributs
- Déclarer et utiliser des méthodes
- Faire interagir des objets entre-eux
- Utiliser les bases de la librairie Pandas (Aller plus loin)

## Consignes

Vous êtes développeur dans une entreprise qui fabrique des jouets. Votre entreprise souhaite créer le jouet qui sera demandé par tous les enfants à Noël. Les ingénieurs ont eu une idée, ils veulent créer un jeu de société familial dont le concept est le suivant : à intervalle régulier le jeu affiche une couleur au hasard parmi un ensemble de couleurs définies, le joueur doit alors appuyer sur la couleur qui s'est affichée. S'il a bon le jeu recommence en ajoutant une deuxième couleur, puis une troisième etc... Cela tant qu'aucun des joueurs ne se trompe dans la séquence à reproduire.

Rassurez-vous, vous n'aurez pas à développeur la version physique du jeu mais votre direction vous a demander de développer un POC(proof of concept) afin de voir si un programme électronique pourrait simuler le jeu désiré. La seule différence sera que vous afficherez des nombres puisque votre terminal est en noir et blanc et qu'un seul joueur sera attendu.

Spécifications fonctionnelles :
- Le jeu demande le nom du joueur
- Le jeu demande un niveau de difficulté (facile, moyen ou difficile)
- Le jeu génère et affiche à l'écran une séquence aléatoire de nombres qui grandit d'un nouveau nombre à chaque tour de jeux
- L'utilisateur doit indiquer l'ensemble des nombres de la séquence via une série d'inputs
- Si le joueur se trompe dans un nombre, le jeu s'arrête
- Le joueur peut choisir de rejouer une nouvelle partie quand il s'est trompé
- Le niveau de difficulté choisi impact le jeu de la manière suivante :
  - facile : nombres entre 1 et 10, intervalle entre deux nombres de 3 secondes
  - moyen : nombres entre 1 et 20, intervalle entre deux nombres de 2 secondes
  - difficile : nombres entre 1 et 100, intervalle entre deux nombres de 1 secondes

Spécifications techniques :
- Utiliser au maximum la programmation orientée objet

## Pour aller plus loin

Il pourrait être intéressant de proposer un système de sauvegardes au joueur qui conserverait quelques informations sur les parties jouées. Idéalement, il faudrait conserver :
- Le nom du joueur
- La difficulté choisie
- Le nombre de tours joués avant de se tromper

Ces informations seront conservées dans un fichier au format de votre choix. Vous pouvez utiliser le format python, JSON ou CSV, à vous de choisir celui qui vous convient le mieux. Sachez cependant que dans la suite de votre formation ce seront plutôt les formats JSON (API et fichiers de configuration) ou CSV (data analyse) qui seront utilisés. Si vous choisissez le format CSV, utilisez la librairie Pandas.
