# Examen Informatique

Ce référentiel contient le nécessaire pour la génération de l'examen final d'informatique 1 pour les étudiants en filière Génie Électrique et Microtechniques de la Haute École d'Ingénierie et de Gestion du canton de Vaud.

## Composition de l'examen

Première de couverture, nom de l'examen, résumé des points obtenus, date de réalisation, nom de l'étudiant et consignes d'examen. Deuxième de couverture vide. Troisième et quatrième de couverture vides.

Chaque problème est un feuillet soit A4, soit A3 avec en tête le numéro du problème.

- `pb1.tex`,
- `pb2.tex`,
- `pb3.tex`,
- `pb4.tex`,
- `Makefile` pour la macro `DATE_EXAM`,

Les objectifs de génération sont :

- regrouper l'examen en un feuillet simplement manipulable ;
- réduire le nombre de pages ;
- isoler les problèmes en des feuillets indépendants ;
- faciliter le tirage et l'assemblage.

## Prérequis

- Docker ou
- XeLatex + Latexmk
