#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    vector<int> dp(n + 1, 20000);
    multimap<int, int> pq; // len, dist
    map<int, set<int>> edges;
    int answer = 0;
    // 0. 엣지 초기화
    for (size_t i = 0; i < edge.size(); i++) {
        int a = edge[i][0];
        int b = edge[i][1];
        edges[a].insert(b);
        edges[b].insert(a);
    }
    // 1. 1에서 출발
    pq.insert(make_pair(0, 1));
    // 2. 가능한 간선을 모두 탐색
    while (pq.size() > 0) {
        int len = pq.begin()->first;
        int dist = pq.begin()->second;
        pq.erase(pq.begin());
        if (dp[dist] < len) {
            continue;
        } else {
            dp[dist] = len;
        }
        for (auto iter = edges[dist].begin(); iter != edges[dist].end(); iter++) {
            if (len + 1 < dp[*iter]) {
                dp[*iter] = len + 1;
                pq.insert(make_pair(len + 1, *iter));
            }
        }
    }
    // 3. 가장 멀리 떨어진 노드의 개수 구하기
    for (size_t i = 0; i < n; i++) {
        pq.insert(make_pair(dp[i + 1], i + 1));
    }
    int m = pq.rbegin()->first;
    for (auto iter = pq.rbegin(); iter != pq.rend(); iter++) {
        if (m == iter->first) {
            answer++;
        }
    }
    return answer;
}