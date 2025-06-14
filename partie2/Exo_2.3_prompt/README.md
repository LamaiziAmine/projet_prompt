------------------------------------------------------------
|                       exercice 2.3                        |
------------------------------------------------------------


# Analyse d'Expériences de Prompt Engineering

Ce document présente l’analyse de trois expériences de prompt engineering réalisées à l’aide d’un modèle de langage (IA) pour générer une fonction en Python. Chaque partie décrit le prompt employé, le code produit, ainsi qu’une analyse critique de la réponse générée.

---

## Prompt Vague :

### Le Prompt
```
"Écris une fonction pour faire des opérations entre deux nombres en Python."
```
### répense AI
HTML/CSS/JS
--> dans le fichier **calcule1.html** 

### résultat observé 
- le style est trés simple 
- pas de gestion de erreurs (a/0 donne infinity)

---
## Prompt spécialisé :

écrire un mini-application web en html css js qui simule une calculatrice simple pour un étudiant ingénieur en génie informatique avec un style élégant et la gestion des erreurs.

### répense AI
HTML/CSS/JS
--> dans le fichier **calcule2.html**


## la différence entre les deux versions

 La première, **calcule1.html**, adopte une interface claire, simple et épurée, avec un design minimaliste et des boutons standards. Elle convient bien à un usage de base ou à des projets d'apprentissage. En revanche, **calcule2.html** propose une version plus avancée, au style sombre et moderne, avec des boutons colorés, arrondis et réactifs, offrant une meilleure ergonomie et une expérience utilisateur plus professionnelle.

Sur le plan fonctionnel, la différence majeure réside dans la gestion des erreurs. Alors que    **calcule1.html** utilise *eval()* de manière directe sans aucune vérification, **calcule2.html** introduit une sécurité minimale en détectant explicitement les cas de division par zéro, ce qui renforce légèrement sa robustesse. Toutefois, les deux versions restent vulnérables car elles reposent toutes deux sur *eval()*, une méthode risquée si elle n’est pas strictement contrôlée. En résumé, **calcule1.html** est plus adaptée pour des usages simples ou éducatifs, tandis que **calcule2.html** cible un usage plus avancé, avec une meilleure esthétique et une gestion des erreurs un peu plus rigoureuse.