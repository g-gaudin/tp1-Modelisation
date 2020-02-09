/*********************************************
 * OPL 12.9.0.0 Model
 * Author: Guillaume Gaudin
 * Creation Date: 8 févr. 2020 at 16:53:36
 *********************************************/

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