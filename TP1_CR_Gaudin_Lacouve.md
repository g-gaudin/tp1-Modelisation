# TP 1 : Problème du Bin Packing
par Pierre Lacouve et Guillaume Gaudin

## Rappel du problème

En optimisation combinatoire, le bin packing est un problème algorithmique qui consiste à ranger des objets d'une taille donnée dans un nombre minimum de boîtes. Le bin packing trouve de nombreuses applications, notamment pour le stockage de données sur des supports informatiques, pour le découpage de la matière première et pour le transport d'articles ou de ressources.
## Description des heuristiques utilisées

 - **Stratégies Next-Fit (NF) et Next-Fit Decreasing (NFD)**
 Dans cette stratégie on ne considère qu’un bin ouvert à la fois. Les objets sont traités selon un ordre donné. Les objets sont rangés successivement dans le bin ouvert tant qu’il y a de la place pour l’objet ai en cours, sinon le bin en cours est fermé et un nouveau bin est ouvert. Une heuristique qui adopte une stratégie NF a l’avantage d’avoir une complexité temporelle linéaire en fonction du nombre d’objets à placer. Par contre, le fait de ne considérer qu’un seul bin à la fois cause beaucoup de perte d’espaces exploitables. Le Next-Fit Decreasing (NFD) consiste à trier les objets par ordre décroissant de hauteurs et appliquer la stratégie NF pour les ranger.
 - **Stratégies First-Fit (FF) et First-Fit Decreasing (FFD)**
Initialement un seul bin est considéré, et les objets sont traités selon un ordre donné. Quand il n’y a plus de la place dans le premier bin pour ranger l’objet ai en cours, un deuxième bin est alors ouvert mais sans fermer le premier. Dans une étape intermédiaire où on dispose de k bins ouverts numérotés de 1 à k selon l’ordre de leur première utilisation, un objet ai en cours est rangé dans le bin du plus faible numéro qui peut le contenir. Dans le cas où aucun bin ne peut contenir ai, un nouveau bin k+1 est alors utilisé sans fermer les autres. L’ordre selon lequel on traite les objets est crucial pour la qualité de la solution. Un choix heuristique consiste à trier les objets par ordre décroissant de hauteurs, on parle dans ce cas d’heuristiques First-Fit Decreasing.
 - **Stratégies Best-Fit (BF) et Best-Fit Decreasing (BFD)** 
Comme dans la stratégie FF, les algorithmes BF laissent les bins toujours ouverts. Cependant, le choix du bin dans lequel l’objet ai en cours va être placé dépend des valeurs des gaps (hauteurs non utilisées) présentes dans les bins. Ainsi, ai sera placé dans le bin qui présente le moindre gap parmi les bins qui peuvent le contenir. Les heuristiques BF et FF peuvent être implantées en O(nlog(n)) en utilisant une structure de données appropriée. On parle de Best-Fit Decreasing (BFD) quand il s’agit de trier les objets à ranger dans l’ordre décroissant de hauteurs avant de les ranger suivant une stratégie BF.
## Formulations linéaires

On note n le nombre d'objets à ranger et ai le volume de l'objet i. On dispose d'un nombre non borné de boîtes, chacune ayant un volume V. Sachant i le numéro d'un objet et j le numéro d'une boîte, on considère les variables xij = 1 si l'objet i est affecté à la boite j (0 sinon) et yj = 1 si la boîte j est utilisée (0 sinon).

Le problème du bin packing peut être modélisé avec la formulation linéaire suivante :
$$
\left \{
\begin{array}{r c l}
      &\forall j \in \N^*,&\quad y_j \in \{0;1\} \\
      &\forall i \in \{1;...;n\},\forall j \in \N^*,& \quad x_{ij} \in \{0;1\} \\
      &&\displaystyle\sum_{i=1}^{+\infty}{y_j}=K (min)\\
      &\forall j \in \N^*,& \displaystyle\sum_{i=1}^{n}{a_ix_{ij}\leq Vy_j}\\
      &\forall i \in \{1;...;n\},&\displaystyle\sum_{j=1}^{+\infty}{x_{ij}}=1\\
\end{array}
\right .
$$

Bien que le nombre j de boites est non bornée, nous savons que l'objectif est de minimiser le nombre de boîtes utilisées et qu'un objet peut être rangé dans une seule boîte au plus. Nous pouvons donc simplifier le problème en bornant j par n le nombre d'objets à ranger :
$$
\left \{
\begin{array}{r c l}
      &\forall j \in \{1;...;n\},&\quad y_j \in \{0;1\} \\
      &\forall i \in \{1;...;n\},\forall j \in \{1;...;n\},& \quad x_{ij} \in \{0;1\} \\
      &&\displaystyle\sum_{i=1}^{n}{y_j}=K (min)\\
      &\forall j \in \{1;...;n\},& \displaystyle\sum_{i=1}^{n}{a_ix_{ij}\leq Vy_j}\\
      &\forall i \in \{1;...;n\},&\displaystyle\sum_{j=1}^{n}{x_{ij}}=1\\
\end{array}
\right .
$$

## Instances sélectionnées

Nous avons choisi les instances Falkenauer U et Falkenauer T :

- Falkenauer U contient des problèmes bin packing de 120, 250, 500 ou 1000 objets à ranger pour un volume de boîte de 150. Les objets occupent des volumes de 20 à 100 unités dans les boîtes. Tous les objets des fichiers de Falkenauer U sont rangés dans l'ordre décroissant de volume occupé, les heuristiques appliquées à ces fichiers seront donc forcément les variantes Decreasing des heuristiques sans tri préalable.
- Falkenauer T contient des problèmes bin packing de 60, 120, 249 ou 501 objets à ranger dans des boîtes de volume de 1000 unités. Les objets occupent des volumes de 250 à 500 unités. Les objets sont là aussi déjà triés dans l'ordre décroissant de volume occupé.

## Description de l'approche et des scripts

Pour comparer les différentes heuristiques présentées et la résolution par CPLEX, nous décidons de ne considérer que la qualité de la solution obtenue, et non pas le temps d'exécution de chaque approche. Nous expliquerons ce choix plus loin.

### Code des heuristiques Next-Fit, First-Fit et Best-Fit :

`heuristics.py` contient toutes les fonctions nécessaires à la partie heuristique de notre script `main.py` : avec une taille de boîte `int box_size` et une liste de volumes d'objets à ranger `int object_list[]` en paramètres, les fonctions `first_fit()`, `next_fit()` et `best_fit()` appliquent leurs algorithmes respectifs et renvoient le nombre de boîtes utilisées sous la forme de la longueur de la liste des boites.

Bien que les variantes en tri décroissant soient aussi implémentées (`first_fit_dec()`, `next_fit_dec()` et `best_fit_dec()`), leur emploi est inutile pour les instances choisies car elles sont déjà triées dans l'ordre décroissant de volume occupé.

### Code de la résolution par CPLEX :

Pour utiliser le solver IBM-CPLEX dans notre script `main.py`, nous appelons les fonctions de la bibliothèque doOpl. Pour fonctionner, doOpl nécessite plusieurs étapes pour préparer le système hôte :

- [ ] Téléchargement et Installation de  CPLEX Studio IDE 12.9.0 (la dernière version étudiante 12.10 n'est pas compatible avec doOpl)
- [ ] Ajout de ...\IBM\ILOG\CPLEX_Studio129\opl\bin\x64_win64 dans la variable d'environnement PATH

En utilisant l'IDE de CPLEX, nous créons notre modèle `bin-packing-model.mod` selon la formulation linéaire précédente :

```
// Paramètres :
 tuple binPacking
    {
    int nbObj;
    int V;
    }
 tuple object
    {
    key int numObj;
    int v;
    }
 {binPacking} pb = ...;
 {object} listobjects = ...;
 int n = first(pb).nbObj;
 int V = first(pb).V;
 range Item = 1..n;
 range Bin = 1..n;
 int ai[i in Item] = item(listobjects,i-1).v;
 
 // Variables :
 dvar boolean x[Item][Bin];
 dvar boolean y[Bin];
 
 // Objectif :
 minimize sum(j in Bin) y[j];

 // Contraintes :
   subject to {
   forall(j in Bin)
     sum(i in Item)ai[i]*x[i][j] <= V*y[j];

   forall(i in Item)
     sum(j in Bin)x[i][j] == 1;
}
tuple solution
{
  key int sol;
  int nbUsedBins;
}

{solution} results = {<1,sum(j in Bin)y[j]>};
```

doOpl n'étant capable d'envoyer en entrée et de recevoir en sortie que des sets de tuples, le modèle est adapté pour que toutes les données paramétrables (n objets, V volume de boite et ai volumes d'objets) soient reçues à l'intérieur de set de tuple. Dans le script `cplexSolver.py`, la fonction `solveWithCplex()` convertit les entiers `numobj` et `box_size` en un set d'un seul tuple, la liste `object_list` en un set de tuples avec clés, et crée le modèle opl à partir du fichier `bin-packing-model.mod`. La solution est reçue sous la forme d'une structure de donnée Dataframe, dont nous tirons notre nombre de boîtes utilisées.

Notre approche se heurte à un obstacle : la résolution par CPLEX est beaucoup trop lente, même pour les fichiers de 60 objets, et le nombre de fichier à traiter (160) rend impossible la résolution en temps raisonnable. Pour palier à ce problème, des fichiers d'options d'exécution `bin-packing-base.ops` et `bin-packing-500+.ops` limitent le temps d'exécution de CPLEX à 10 secondes pour les fichiers de moins de 500 objets et une minute pour les fichiers de 500 ou plus objets. C'est pour cette raison que les temps d'exécution des différentes approches ne seront pas comparés, l'approche par CPLEX étant bridée par commodité.

### Fonctionnement de main.py :

Notre script principal `main.py` cherche les différents chemins des fichiers stockés dans les dossiers Falkenauer U et Falkenauer_T, lit les différentes instances dans ces fichiers et appliquent les fonctions heuristiques et la résolution de CPLEX à ces instances. Pour chaque dossier et chaque quantité d'objets à ranger, notre script calcule la moyenne du nombre de boîtes utilisées par chaque approche et les affiche dans deux graphes.

## Résultats

![](D:\cours_M1\tp1-Modelisation-master\falkenauer_u.png)

![](D:\cours_M1\tp1-Modelisation-master\falkenauer_t.png)

Nos résultats confirment plusieurs prévisions que nous avons eu sur ce problème de Bin Packing :

- Des trois heuristiques, Next-Fit est la plus rapide (complexité en O(n)) et la plus mauvaise en terme de qualité de solution. Pour tous les cas de liste d'objets inférieure à 501 éléments, cette heuristique propose le plus grand nombre de boîtes utilisées. Cette différence avec les autres approches semble toutefois diminuer avec l'augmentation du volume des boîtes V.
- Les différences entre les heuristiques First-Fit, Best-Fit et la résolution par CPLEX sont très faibles pour les listes d'objets de moins de 500 éléments. Ceci est probablement due au fait que nos heuristiques profitent d'un tri préalable décroissant des volumes d'objets et que la résolution par CPLEX est bridée en temps d'exécution.
- Si la résolution linéaire de CPLEX produit des résultats légèrement meilleurs pour des listes de moins de 500 éléments, la qualité des solutions se dégradent rapidement avec l'augmentation du nombre d'objets à traiter.