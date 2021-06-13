#include <iostream>
using namespace std;
void ring(int& x, int& y) {
    for(int i = 2; i <= x && i <= y; i++) {
        if(x % i == 0 && y % i == 0) {
            x /= i;
            y /= i;

            i = 1;
        }
    }
}
int main() {
    int n;
    cin >> n;
    n-=1;
    int c;
    cin >> c;

    for(int i = 0; i < n; i++) {
        int z;
        cin >> z;

        int dd = c;

        ring(dd, z);
        cout << dd << "/" << z<< endl;
    }
}
