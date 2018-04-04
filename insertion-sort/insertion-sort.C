#include<stdio.h>

int main(){
  int a[20], i, n, j, key, hole;
  scanf("%d",&n);
  for(i=0;i<n;i++){
    scanf("%d",&a[i]);
  }
  for(i=1; i<n; i++){
    key = a[i];
    hole = i-1;
    while(hole>0 && a[hole]>key){
      a[hole+1] = a[hole];
      hole = hole-1;
    }
    a[hole+1] = key;
  }
  for(i=0;i<n;i++){
    printf("%d \t",a[i]);
  }
  return 0;
}
