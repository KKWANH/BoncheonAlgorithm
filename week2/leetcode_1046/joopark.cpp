class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        multimap<int, int> pq;
        for (size_t i = 0; i < stones.size(); i++) {
            pq.insert(make_pair(stones[i], 0));
        }
        while (pq.size() > 1) {
            auto iter1 = pq.rbegin();
            auto iter2 = pq.rbegin();
            iter2++;
            int newvalue = -1;
            if (iter1->first > iter2->first) {
                newvalue = iter1->first - iter2->first;
            } else if (iter1->first < iter2->first) {
                newvalue = iter2->first - iter1->first;
            };
            pq.erase(--iter1.base());
            pq.erase(--iter2.base());
            if (newvalue != -1) {
                pq.insert(make_pair(newvalue, 0));
            }
        }
        return pq.begin()->first;
    }
};