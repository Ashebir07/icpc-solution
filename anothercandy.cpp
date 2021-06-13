#include <iostream>
#include <string>
using namespace std;
int main() {
    int n;
    cin >> n;

    for(int i = 0; i < n; i++) {
        int t;
        cin >> t;

        int sum= 0;

        for(int j = 0; j < t; j++) {
            long long  temp;
            cin >> temp;

            sum += temp % t;
        }

        if(sum % t == 0) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }
}
