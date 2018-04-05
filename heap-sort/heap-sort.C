#include<stdio.h>

void heapsort(int a[], int n);
void heapify(int a[], int n, int i);
void swap(int a, int b);

int main(){
  int a[10], i, n;
  scanf("%d",&n);
  for(i=0;i<n;i++){
    scanf("%d",&a[i]);
  }
  heapsort(a,n);
}

void heapsort(int a[], int n){
  int i;
  for(i=(n/2)-1;i>=0;i++){
    heapify(a,n,i);
  }
  for(i=n-1;i>=0;i--){
    swap(a[0],a[i]);
    heapify(a,i,0);
  }
}

void heapify(int a[], int n, int i){
  int largest = i;
  int l = 2*i;
  int r = 2*i + 1;
  if(l<n && a[l]<a[i]){
    largest = i;
  }
  else if(r<n && a[r]<a[i]){
    largest = r;
  }
  if(largest != i){
    swap(a[largest],a[i]);
  }
  heapify(a,n,largest);
}

void swap(int a, int b){
  int temp;
  temp = a;
  a = b;
  b = temp;
}
