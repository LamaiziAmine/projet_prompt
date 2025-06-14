## 🧩 Exercice 3.2 – Analyse et refactoring d’un code de tri par sélection

---

### ❓ Question 1 – Défauts de lisibilité

1. **Indentation manquante**  
Le code initial n’est pas indenté, ce qui le rend difficile à lire et provoque des erreurs en Python.

2. **Noms de variables peu explicites**  
Variables comme `a`, `i`, `j`, `tmp` sont courantes mais manquent de clarté.  
Des noms comme `array`, `min_index`, `temp` amélioreraient la compréhension.

3. **Absence de commentaires**  
Aucun commentaire n’explique le fonctionnement de la boucle ni la logique du tri.

4. **Pas de fonction**  
Le tri est réalisé dans le code principal, ce qui limite la réutilisabilité et la clarté.

---

### 🎯 Question 2 – Prompt pour améliorer le code

> "Refactore le code suivant qui trie une liste en ordre croissant.  
> Améliore la lisibilité, l’indentation, et utilise de bonnes pratiques de programmation.  
> Le tri doit être placé dans une fonction nommée `selection_sort`, avec une documentation claire.  
> Utilise des noms de variables explicites, évite les redondances, et assure-toi que le code reste fonctionnel."

---

### 🎯 Question 3 – Prompt plus complet avec contraintes

> "Refactore le code Python ci-dessous pour améliorer sa qualité et sa lisibilité.  
> Respecte les contraintes suivantes :  
> - Suivre la convention PEP8 (indentation, espacement, noms, etc.).  
> - Ajouter des docstrings pour chaque fonction.  
> - Séparer le code en fonctions modulaires (ex. : fonction pour trier, fonction principale).  
> - Utiliser des noms explicites pour les variables et les fonctions.  
> - Ajouter un bloc `if __name__ == "__main__":` pour l’exécution du programme principal."
