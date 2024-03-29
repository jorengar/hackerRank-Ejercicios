#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n;
    cin >> n;
    
    vector<int> vec;
    
    for(int i = 0; i<n;i++){
        int valor;
        cin >> valor;
        vec.push_back(valor);
    }
    
    cin >> n;
    
    for(int i = 0; i<n;i++){
        int valor;
        cin >> valor;
        auto it = lower_bound(vec.begin(), vec.end(), valor);

        // Mostrar el resultado
        if (it != vec.end() && *it == valor) {
            cout << "Yes " << (it - vec.begin())+1 << endl;
        } else {
            cout << "No " << (it - vec.begin())+1 << endl;
        }
    } 
    
    return 0;
}