#include<stdio.h>

int main(){
  int mid, i, j, n, a[10], temp, cout=0, index, num;
  scanf("%d",&n);
  for(i=0;i<n;i++){
    scanf("%d",&a[i]);
  }
  for(i=0;i<n;i++){
    for(j=i+1;j<n;j++){
      if(a[i]>a[j]){
        temp = a[i];
        a[i] = a[j];
        a[j] = temp;
      }
    }
  }
  scanf("%d",&num);
  mid = n/2;
  if(num<a[mid]){
    for(i=0;i<mid;i++){
      if(num == a[i]){
        index = i;
        }
      }
    }
    if(num>a[mid]){
      for(i=mid+1;i<n;i++){
        if(num == a[i]){
          index = i;
        }
      }
    }
  printf("found %d at %d",num,index+1);

}
