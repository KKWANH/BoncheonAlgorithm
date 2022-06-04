#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    map<int, set<int>> win;
    map<int, set<int>> lose;
    for (size_t i = 0; i < results.size(); i++) {
        int w = results[i][0];
        int l = results[i][1];
        win[w].insert(l);
        lose[l].insert(w);
    }
    for (size_t i = 1; i < n + 1; i++) {
        for (auto iter = win[i].begin(); iter != win[i].end(); iter++) {
            // iter : 선수 i에게 진 사람(들)
            auto& loses = lose[*iter];
            // loses : 선수 i에게 진 사람에게 이긴 사람들
            loses.insert(lose[i].begin(), lose[i].end());
            // 선수 i에게 진 사람들에게 이긴 사람들에 선수 i에게 이긴 사람들을 추가함
        }
        for (auto iter = lose[i].begin(); iter != lose[i].end(); iter++) {
            win[*iter].insert(win[i].begin(), win[i].end());
        }
    }
    for (size_t i = 1; i < n + 1; i++) {
        if ((win[i].size() + lose[i].size()) == n - 1) {
            answer++;
        }
    }
    return answer;
}