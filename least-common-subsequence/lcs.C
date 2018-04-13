#include<stdio.h>
#include<string.h>

int max(int a, int b);
int lcs(char a[], char b[], int m, int n);

int main(){
  int m,n;
  char a[] = "AGGTAB", b[] = "GCTXAYB";
  m = strlen(a);
  n = strlen(b);
  int res = lcs(a,b,m,n);
  printf("%d",res);
}
int lcs(char a[], char b[], int m, int n){
  if(m==0 || n==0){
    return 0;
  }
  if(a[m-1] == b[n-1]){
    return 1 + lcs(a,b,m-1,n-1);
  }
  else
  return max(lcs(a,b,m,n-1),lcs(a,b,m-1,n));
}
int max(int a, int b){
  if(a>b){
    return a;
  }
  else{
    return b;
  }
}
