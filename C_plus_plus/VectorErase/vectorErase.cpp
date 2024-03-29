#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    
    //Se tomó el tamaño del vector, que es el primer valor que ingresa
    int sizeVector;
    cin >> sizeVector;
    
    //Se tomó los valores que van a llenar el vector
    vector<int> miVector;
    for(int i; i<sizeVector; i++){
        int nuevoValor;
        cin >> nuevoValor; 
        miVector.push_back(nuevoValor);
    }
    
    //Se tomó la posición que se va a borrar
    int positionVector;
    cin >> positionVector;
    
    //Se elimina la posición
    miVector.erase(miVector.begin()+positionVector-1); 

    //Se especificaron los puntos de inicio y fin para borrar una sección del vector
    int start; 
    int end; 
    cin >> start;
    cin >> end;

    //Se borró la sección del vector
    miVector.erase(miVector.begin()+start-1,miVector.begin()+end-1);

    //Se muestra el nuevo valor
    cout << miVector.size() << endl;
    for (int i = 0; i < miVector.size(); ++i) {
        cout << miVector[i] << " ";
    }

    return 0;
}