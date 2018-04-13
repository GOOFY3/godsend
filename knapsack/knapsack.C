#include<stdio.h>

int knapsack(int W, int wt[], int val[], int n);
int max(int a, int b);


int main(){
  int i, n, val[10], wt[10], W, res;
  scanf("%d",&n);
  printf("Weights?\n");
  for(i=0;i<n;i++){
    scanf("%d",&wt[i]);
  }
  printf("Values?\n");
  for(i=0;i<n;i++){
    scanf("%d",&val[i]);
  }
  printf("Max weight of knapsack?\n");
  scanf("%d", &W);
  res = knapsack(W, wt, val, n);
  printf("%d",res);
  return 0;
}

int max(int a, int b){
  if(a>b){
    return a;
  }
  else
  return b;
}

int knapsack(int W, int wt[], int val[], int n){
  if(n==0 || W==0){
    return 0;
  }
  if(wt[n-1]>W){
    return knapsack(W, wt, val, n-1);
  }
  else
  return max(val[n-1] + knapsack(W-wt[n-1], wt, val, n-1), knapsack(W, wt, val, n-1));
}
