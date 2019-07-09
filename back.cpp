#include <iostream> 
#include <fstream> 

using namespace std; 

void p ( double &x0 ) 
{ 
    x0 = x0 * x0 ;
    cout<< x0 << endl; 
    cout<< &x0 << endl; 
} 

void p1 ( double &x1 ) 
{ 
    x1 = x1 / 2 ;
    cout<< x1 << endl; 
    cout<< &x1 << endl; 
} 
int main()
{ 
    cout << "parameters addresses" << endl;
    double x0 = 2;
    cout << &x0 << endl;
    p(x0);
    p1(x0);
    cout << x0 << endl;
} 
