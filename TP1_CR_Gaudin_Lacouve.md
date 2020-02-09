# TP 1 : Problème du Bin Packing
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