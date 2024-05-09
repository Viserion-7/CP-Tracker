#include <bits/stdc++.h>
using namespace std;

int main(){
    string n, nw;
    cin>>n;
    while(n.find("WUB")!=- 1) {
        int i=n. find ("WUB");
        n.erase (i, 3);
        n.insert(i, " ");
    }
    for (int i=0; i<n.length();i++){
        if(n[i]!=' ') 
            nw+=n[i];
        if(n[i]==' ' && n[i+1]!=' ')
            nw+=n[i];
    }
    cout<< nw;
    return 0;
}