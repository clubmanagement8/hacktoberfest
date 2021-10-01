#include<stdio.h>
#include<stdlib.h>

void bubble();


int a[5]={5,4,7,2,9};

int main(){
int i;
selection(a,5);
for(i=0;i<5;i++){
    printf("%d\n",a[i]);
}
return 0;
}
void swap(int *k, int *l){
    int temp;
    temp=*k;
    *k=*l;
    *l=temp;
}

void bubble(int *b, int size){
int i,j,c=0,temp;
for(i=0;i<size;i++){
    c=0;
    for(j=0;j<size-1;j++){
        if(b[j]>b[j+1]){
           swap(b+j,b+j+1);
            c++;
        }
    //printf("c=%d\n",c);
    }
    if(!c) break;
}
}
