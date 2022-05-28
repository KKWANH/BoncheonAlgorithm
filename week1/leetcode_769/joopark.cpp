/*
이 문제에서 배열 인덱스와 값의 성격이 같기 때문에 별도로 정렬을 할 필요는 없습니다.
그래서 인덱스에 대한 값이 인덱스와 동일하면 해당 값은 이동시킬 필요가 없으며 인덱스에 대한 값이 다르다면 값을 이동시켜야 합니다.

여기서 인덱스에 대한 값은 이 값이 실제로 이동되어야 하는 위치를 나타냅니다.
그러면 특정 범위가 형성되는데 이 범위 내에 있는 값들은 하나의 chunk를 이룰 수 있습니다.

하지만 이렇게 산정된 chunk는 다른 chunk랑 겹치게 될 수 있으므로 해당 chunk와 겹치는지 판단하는 로직이 들어가야 합니다.
겹치는 chunk는 하나의 chunk로 판단하여 총 chunk의 개수를 구합니다.
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        vector<bool> check(arr.size(), false);
        int group = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (i == arr[i]) {
                if (check[i] != true) {
                    check[i] = true;
                    group++;
                }
            } else {
                bool same_group = false;
                if (i < arr[i]) {
                    for (int j = i; j <= arr[i]; j++) {
                        if (check[j] == true) {
                            same_group = true;
                        }
                        check[j] = true;
                    }
                    if (same_group == false) {
                        group++;
                    }
                }
            }
        }
        return group;
    }
};