#include<stdio.h>

void swap(int *, int *);

int main(){
  int a[10], n, i, j;
  scanf("%d",&n);
  for(i=0;i<n;i++){
    scanf("%d",&a[i]);
  }
  for(i=0;i<n;i++){
    for(j=0;j<n-i-1;j++){
      if(a[j]>a[j+1]){
        swap(&a[j],&a[j+1]);
      }
    }
  }
  for(i=0;i<n;i++){
    printf("%d",a[i]);
  }
  return 0;
}

void swap(int *a, int *b){
  int temp;
  temp = *a;
  *a = *b;
  *b = temp;
}

//added
