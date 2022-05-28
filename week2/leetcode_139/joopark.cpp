bool wordBreak(string s, vector<string>& wordDict) {
    vector<bool> dp(s.size() + 1, false); // 부분 문자열의 시작점 위치에 부분 문자열이 들어가도 되는지의 여부를 담고 있음
    dp[0] = true; // 인덱스 0부터 탐색을 하는데 부분 문자열이 실제로 존재하던 존재하지 않던 탐색해야 하므로 true 삽입
    set<string> wordset;
    
    for (int i = 0; i < wordDict.size(); i++) {
        wordset.insert(wordDict[i]);
    }
    
    for (int i = 1; i <= s.size(); i++) { // 문자열의 길이만큼 순회 (1 ~ size)
        for (int j = i - 1; j >= 0; j--) { // 문자열의 길이가 주어질 때 역방향으로 순회하여 부분 문자열을 조합해 냄
            // 기본 시간복잡도 : O(N^2)지만 문자열 최대 길이가 그렇게 길지 않아 용인되는 듯
            if (dp[j]) { // 부분 문자열의 시작점이 true라면 (초기값의 시작점은 0이며 true임) 비교를 함. 그렇지 않으면 비교 생략
                if (wordset.find(s.substr(j, i - j)) != wordset.end()) { // 해당 부분 문자열이 기존 딕셔너리에 있다면
                    dp[i] = true; // 새 부분 문자열의 좌표가 될 지점으로 이어지는 라인이 있다는 뜻이며 j의 루프는 돌 필요가 없음.
                    break;
                }
            }
        }
    }
    return dp[s.size()];
}