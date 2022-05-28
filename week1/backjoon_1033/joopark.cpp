/*
칵테일 재료 간 비율을 맵(딕셔너리)에 저장합니다.

여기서 유의해야 할 점이 있는데
  만약 (a-b) 와 (b-c) 간의 관계는 바로 (a-b-c) 로 바꿀 수 있는데
  (a-b), (c-d)와의 관계는 서로 독립적이기 때문에 (b-c)를 이용할 때 저는 실수를 했습니다.

예를 들어 (a-b), (c-d) 각 관계를 알고 있을 때 (b-c)를 바로 이용하면
  독립적인 (a-b), (c-d)를 계산해 하나로 합쳐야 합니다.
  
이 부분의 구현이 까다롭다고 생각해 저는 (a-b) 관계를 알게 될 때
  (c-d)는 잠시 무시하고 (b-c)를 이용해 (a-b-c) 관계를 만듭니다.
  
이후 (c-d) 관계를 이용해 (a-b-c-d) 관계를 유추합니다.

이후 관계들 간의 숫자의 최대공약수를 이용해 숫자들을 나눠 관계들 간의 최소 숫자를 구합니다.
*/

#include <iostream>
#include <map>
#include <vector>
#include <set>

size_t gcd(size_t a, size_t b) {
  if (b == 0) {
    return a;
  }
  return gcd(b, a % b);
}

int main(void) {
  std::map<int, size_t> result;
  std::set< std::vector<int> > assoc;
  size_t loop;

  std::cin >> loop;

  for (size_t i = 0; i < loop - 1; i++) {
    int a, b;
    size_t p, q;
    std::cin >> a >> b >> p >> q;
    size_t g = gcd(p, q);
    p /= g;
    q /= g;
    std::vector<int> tmp;
    tmp.push_back(a);
    tmp.push_back(b);
    tmp.push_back(p);
    tmp.push_back(q);
    assoc.insert(tmp);
  }
  while (assoc.empty() == false) {
    for (auto iter_assoc = assoc.begin(); iter_assoc != assoc.end();) {
      int a = iter_assoc->at(0);
      int b = iter_assoc->at(1);
      size_t p = iter_assoc->at(2);
      size_t q = iter_assoc->at(3);
      if (result.empty()) {
        result[a] = p;
        result[b] = q;
        iter_assoc = assoc.erase(iter_assoc);
      } else if ((result.find(a) != result.end()) && (result.find(b) == result.end())) {
        size_t b_a = result[a];
        for (auto iter = result.begin(); iter != result.end(); iter++) {
          iter->second = iter->second * p;
        }
        result[b] = b_a * q;
        iter_assoc = assoc.erase(iter_assoc);
      } else if ((result.find(a) == result.end()) && (result.find(b) != result.end())) {
        size_t b_b = result[b];
        for (auto iter = result.begin(); iter != result.end(); iter++) {
          iter->second = iter->second * q;
        }
        result[a] = b_b * p;
        iter_assoc = assoc.erase(iter_assoc);
      } else {
        iter_assoc++;
      }
    }
  }

  size_t g = result.begin()->second;
  for (auto iter = result.begin(); iter != result.end(); iter++) {
    g = gcd(g, iter->second);
  }
  for (auto iter = result.begin(); iter != result.end(); iter++) {
    result[iter->first] = result[iter->first] / g;
  }
  for (auto iter = result.begin(); iter != result.end(); iter++) {
    std::cout << iter->second << " ";
  }
  return 0;
}