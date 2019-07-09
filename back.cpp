#include <iostream> 
#include <fstream> 

using namespace std; 

#define p(x0)x0*x0
#define p1(x1)x1/0
double x0 = 3;
int main()
{ 
    cout << x0 << endl;
    cout<< p(x0) <<endl;
    cout<< p1(x0) <<endl;
    cout << x0 << endl;
} 
