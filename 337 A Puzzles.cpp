#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <climits>
#include <vector>
using namespace std;

int main(){
    int n, m;
    cin >> n >> m;
    int a[m];
    for (int i = 0; i < m; i++){
        cin >> a[i];
    }
    sort(a, a + m);
    int minm = INT_MAX;
    for (int i = 0; i < m; i++){
        for (int j = n + i - 1; j < m; j++){ 
            minm = min(a[j] - a[i], minm); 
        }
    }
    cout << minm << endl;
}
