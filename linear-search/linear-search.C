#include<stdio.h>

int main(){
  int a[10], i, n, num, index, cout=0;
  scanf("%d",&n);
  for(i=0;i<n;i++){
    scanf("%d",&a[i]);
  }
  scanf("%d",&num);
  for(i=0; i<n; i++){
    if(a[i] == num){
      index = i;
    }else{
      cout++;
    }
  }
  if(index<=n){
    printf("found %d at %d",index,index-1);
  }
  if(cout==n){
    printf("Not Found!");
  }
}
