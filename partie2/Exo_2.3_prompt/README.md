## 📌 Exercice 2.3 – Analyse d'Expériences de Prompt Engineering

Ce document présente l’analyse de trois expériences de prompt engineering réalisées à l’aide d’un modèle de langage (IA) pour générer une fonction en Python.  
Chaque partie décrit :
- Le **prompt utilisé**
- Le **code généré**
- Une **analyse critique** du résultat obtenu

---

### 🌀 Prompt Vague

#### 📝 Le prompt

```
"Écris une fonction pour faire des opérations entre deux nombres en Python."
```

#### 💻 Réponse de l'IA
> Génération d'une **interface HTML/CSS/JS**  
> 📄 Fichier généré : `calcule1.html`

#### 🔍 Résultat observé
- Design **très simple** et basique
- **Aucune gestion des erreurs** (exemple : `a / 0` renvoie `Infinity`)
- Utilisation directe de `eval()` sans vérification

---

### 🎯 Prompt Spécialisé

#### 📝 Le prompt
> *"Écrire une mini-application web en HTML/CSS/JS qui simule une calculatrice simple pour un étudiant ingénieur en génie informatique, avec un style élégant et la gestion des erreurs."*

#### 💻 Réponse de l'IA
> Génération d'une interface **plus aboutie**  
> 📄 Fichier généré : `calcule2.html`

---

### ⚖️ Comparaison des deux versions

| Élément              | `calcule1.html`                             | `calcule2.html`                                  |
|----------------------|---------------------------------------------|--------------------------------------------------|
| 💡 Interface         | Simple, épurée, boutons standards           | Moderne, sombre, boutons arrondis et interactifs |
| 🎨 Esthétique        | Basique, adaptée à l’apprentissage          | Plus professionnelle, meilleure UX              |
| 🛡️ Sécurité          | Aucune vérification, `eval()` brut          | Détection des divisions par zéro                |
| ⚠️ Vulnérabilité     | Risque élevé via `eval()`                   | Toujours vulnérable, mais légèrement renforcée   |
| 🎯 Cible             | Usage éducatif ou expérimental              | Usage semi-professionnel, étudiant ingénieur     |

---

### 🧠 Conclusion

- `calcule1.html` est une version minimaliste, utile pour l’apprentissage ou les démonstrations simples.  
- `calcule2.html` propose une **expérience utilisateur enrichie**, avec un style plus abouti et une gestion rudimentaire des erreurs.
- **Les deux versions** utilisent `eval()` — ce qui reste une méthode **risquée** sans validation stricte.  
Il est donc essentiel de **renforcer la sécurité** dans un usage réel.
