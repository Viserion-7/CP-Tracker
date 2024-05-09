#include <iostream>
#include <string>
using namespace std;
int main() {
    string s,res;
    cin >> s;
    for(int i =0; i<s.length();++i){
        s[i] = tolower(s[i]);
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || s[i] == 'y') continue;
        else {
            printf(".%c",s[i]);
        }
    }
    printf("\n");
    return 0;

}
