/*
직/간접적으로 이루어진 노드들을 그룹으로 생각하고 그룹의 개수를 세는 문제입니다.

주어진 노드들이 이어졌는지 DFS로 탐색하고 이미 탐색한 노드는 가지를 쳐서 시간복잡도를 줄였습니다.

탐색 여부는 visited에 저장합니다.
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
    void dfs(size_t idx, vector<int>& visited, vector<vector<int>>& isConnected, int rtn) {
        for (size_t i = 0; i < isConnected.size(); i++) {
            if (isConnected[idx][i] == 1 && visited[i] == -1) {
                visited[i] = rtn;
                dfs(i, visited, isConnected, rtn);
            }
        }
    }
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        vector<int> visited(isConnected.size(), -1);
        int rtn = 0;

        for (size_t i = 0; i < isConnected.size(); i++) {
            if (visited[i] == -1) {
                visited[i] = ++rtn;
            }
            dfs(i, visited, isConnected, rtn);
        }
        return rtn;
    }
};class Solution {
    void dfs(size_t idx, vector<int>& visited, vector<vector<int>>& isConnected, int rtn) {
        for (size_t i = 0; i < isConnected.size(); i++) {
            if (isConnected[idx][i] == 1 && visited[i] == -1) {
                visited[i] = rtn;
                dfs(i, visited, isConnected, rtn);
            }
        }
    }
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        vector<int> visited(isConnected.size(), -1);
        int rtn = 0;

        for (size_t i = 0; i < isConnected.size(); i++) {
            if (visited[i] == -1) {
                visited[i] = ++rtn;
            }
            dfs(i, visited, isConnected, rtn);
        }
        return rtn;
    }
};