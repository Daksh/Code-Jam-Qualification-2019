#include<bits/stdc++.h>
using namespace std;

void printInt(char* x){
    int i = 0;
    while(x[i]!='\0' && x[i]=='0') i++;
    if(x[i]=='\0'){
        printf("0");
        return;
    }
    while(x[i]!='\0'){
        printf("%c",x[i++]);
    }
}

int main(){
    int t;
    scanf("%d", &t);
    
    char num[101], a[101], b[101];
    int i;

    for(int tNum = 1; tNum <= t; tNum++){
        scanf("%s", num);
        for(i = 0; num[i]!='\0'; i++){
            if(num[i]=='4'){
                a[i]='2';
                b[i]='2';
            } else{
                a[i] = num[i];
                b[i] = '0';
            }
        }
        a[i]='\0';
        b[i]='\0';

        printf("Case #%d: ", tNum);
        printInt(a);
        printf(" ");
        printInt(b);
        printf("\n");
    }
    return 0;
}