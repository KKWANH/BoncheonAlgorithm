# 시간을 계속 증가시켜 가면서, 특정 시간에 각각의 심사자들이 심사할 수 있는 max 인원을 모두 더해서, 그 수가 주어진 사람과 같으면 된다! 
# 라고 생각했답니다.
# 물론 효율성 통과를 못함..! 이게 왜 이분탐색일까요..?!?!

def solution(n, times):
    for sec in range(9999999):
        totalSum = 0
        for j in times:
            totalSum += sec // j
        if totalSum == n:
            return sec