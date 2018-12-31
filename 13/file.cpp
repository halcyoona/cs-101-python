#include<iostream>
using namespace std;

string to_stringx(const int& n); 
void str2inta(string s, int x[], int size);
string inta2str(int x[], int size);


void array_sum(int a[], int b[], int c[], int size) {
    
    int carry = 0;
    for (int i = 0 ; i < size + 1 ; i++) {
        
        
        int sum = 0;


        sum = a[i] + b[i];
        if (sum < 10) {
            sum = sum + carry;
            c[i] = sum;
            carry = 0;
        }
        else { 
            sum = (sum + carry) - 10; 
            carry = 1;
            c[i] = sum;
       }
    }
    return;
       
}
     

int main(){
    int a[6] = {8,2,1,0,0,0};
    int b[6] = {5,8,9,0,0,0};
    int c[6];
    
    array_sum(a, b, c, 6);
    cout <<  c[2] << endl;
    return 0;

}

