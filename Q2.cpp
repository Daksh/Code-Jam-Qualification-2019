#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    scanf("%d", &t);

    for(int cNum = 1; cNum <= t; cNum++){
        printf("Case #%d: ", cNum);
        int n;
        scanf("%d", &n);
        char in[50001];
        scanf("%s", in);

        int lx=0,ly=0,mx=0,my=0,i;
        char prev='x';

        for(i=0; i<2*n-2; i++){
            if(in[i] == 'S') printf("%c", 'E');
            else printf("%c", 'S');
        }
        assert(in[i]=='\0');
        printf("\n");
    }

    return 0;
}