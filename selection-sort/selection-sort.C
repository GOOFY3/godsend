#include<stdio.h>

int main(){
  int a[20], n, i, j, temp;
  scanf("%d",&n);
  for(i=0;i<n;i++){
    scanf("%d",&a[i]);
  }
  for(i=0;i<n-1;i++){
    for(j=i+1;j<n;j++){
      if(a[i]>a[j]){
        temp = a[i];
        a[i] = a[j];
        a[j] = temp;
      }
    }
  }
  for(i=0;i<n;i++){
    printf("%d \t",a[i]);
  }
  printf("\n");
  return 0;
}


//take an element. compare it with all other elements after it. Then it is sorted. Now go for second element.
