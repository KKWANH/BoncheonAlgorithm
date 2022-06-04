class Solution {
public:
    bool isSubsequence(string s, string t) {
        auto si = s.begin();
        for (auto ti = t.begin(); ti != t.end(); ti++) {
            if (*ti == *si) {
                si++;
            }
        }
        return si == s.end();
    }
};