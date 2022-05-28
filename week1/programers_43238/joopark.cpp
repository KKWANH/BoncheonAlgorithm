/*
가능성이 있는 숫자를 고른 다음 이분탐색으로 유효한 숫자를 찾아나갑니다.

여기서 유효한 숫자를 찾는것에 대해 유의해야 하는데
저는 문제에서 주어진 `long long` 타입을 그대로 사용하였는데 오버플로우 문제로 시간을 허비하였었습니다.

비교적 큰 숫자를 다뤄도 오버플로우 걱정이 없는 언어가 부러웠습니다. (파이썬갓)

저는 유효한 숫자를 찾기 위해 주어진 심사대 시간들의 최소공배수를 구했습니다.
*/

#include <iostream>
#include <vector>

using namespace std;

size_t gcd(size_t a, size_t b) {
    if (a == 0UL) {
        return b;
    } else {
        return gcd(b % a, a);
    }
}

size_t lcm(size_t a, size_t b) {
    return (a > b) ? ((a / gcd(a, b)) * b) : ((b / gcd(a, b)) * a); // overflow 방지
}

long long solution(int n, vector<int> times) {
    // 1. times의 최소공배수 고르기
    size_t lcm_of_times = times[0];
    for (size_t i = 1; i < times.size(); i++) {
        lcm_of_times = lcm(lcm_of_times, times[i]);
    }
    // 2. 이분 탐색으로 최소 시간 찾기
    size_t start = 0UL;
    size_t end = lcm_of_times;
    while ((end - start) > 1UL) {
        size_t half = (end - start) / 2UL;
        size_t target = start + half;
        size_t tmp = 0;
        for (size_t i = 0; i < times.size(); i++) {
            tmp += target / times[i];
        }
        if (tmp >= n) {
            end = end - half;
        } else {
            start = start + half;
        }
    }
    return end;
}