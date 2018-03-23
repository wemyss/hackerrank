#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    unsigned int n, m;
    cin >> n >> m;
    auto list = vector<unsigned int>(n);

    for (auto i = 0U; i < m; ++i) {
        unsigned int a, b, k;
        cin >> a >> b >> k;
        for (auto j = a-1; j < b; ++j) {
            list[j] += k;
        }
    }

    auto result = 0U;
    for (auto iter = list.begin(); iter != list.end(); ++iter) {
        result = max(result, *iter);
    }
    cout << result << '\n';
    return 0;
}
