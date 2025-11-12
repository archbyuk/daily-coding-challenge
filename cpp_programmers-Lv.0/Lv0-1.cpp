#include <iostream>
#include <vector>

using namespace std;

vector<int> solution (int n, vector<int> slicer, vector<int> num_list) {
    vector<int> answer;

    int a = slicer[0], b = slicer[1], c = slicer[2];

    if (n == 1) {
        answer.assign(num_list.begin() + a, num_list.begin() + b + 1)
    }

    else if (n == 2) {
        answer.assign(num_list.begin() + a, num_list.end())
    }

    else if (n ==3) {
        answer.assign(num_list.begin() + a, num_list.begin() + b + 1 )
    }

    else {
        for (int i = a; i <= b; i += c) {
            answer.push_back(num_list[i]);
        }
    }
}

int main() {
    int n = 4;
    vector<int> slicer = {1, 5, 2};
    vector<int> num_list = {10, 20, 30, 40, 50, 60};

    vector<int> result = solution(n, slicer, num_list);

    for (int x : result) cout << x << " ";

    return 0;
}