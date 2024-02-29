"""
문제
요즘 민규네 동네에서는 스타트링크에서 만든 PS카드를 모으는 것이 유행이다.

PS카드는 PS(Problem Solving)분야에서 유명한 사람들의 아이디와 얼굴이 적혀있는 카드이다. 각각의 카드에는 등급을 나타내는 색이 칠해져 있고, 다음과 같이 8가지가 있다.

전설카드
레드카드
오렌지카드
퍼플카드
블루카드
청록카드
그린카드
그레이카드
카드는 카드팩의 형태로만 구매할 수 있고, 카드팩의 종류는 카드 1개가 포함된 카드팩, 카드 2개가 포함된 카드팩, ... 카드 N개가 포함된 카드팩과 같이 총 N가지가 존재한다.

민규는 카드의 개수가 적은 팩이더라도 가격이 비싸면 높은 등급의 카드가 많이 들어있을 것이라는 미신을 믿고 있다. 따라서, 민규는 돈을 최대한 많이 지불해서 카드 N개 구매하려고 한다. 카드가 i개 포함된 카드팩의 가격은 Pi원이다.

예를 들어, 카드팩이 총 4가지 종류가 있고, P1 = 1, P2 = 5, P3 = 6, P4 = 7인 경우에 민규가 카드 4개를 갖기 위해 지불해야 하는 금액의 최댓값은 10원이다. 2개 들어있는 카드팩을 2번 사면 된다.

P1 = 5, P2 = 2, P3 = 8, P4 = 10인 경우에는 카드가 1개 들어있는 카드팩을 4번 사면 20원이고, 이 경우가 민규가 지불해야 하는 금액의 최댓값이다.

마지막으로, P1 = 3, P2 = 5, P3 = 15, P4 = 16인 경우에는 3개 들어있는 카드팩과 1개 들어있는 카드팩을 구매해 18원을 지불하는 것이 최댓값이다.

카드 팩의 가격이 주어졌을 때, N개의 카드를 구매하기 위해 민규가 지불해야 하는 금액의 최댓값을 구하는 프로그램을 작성하시오. N개보다 많은 개수의 카드를 산 다음, 나머지 카드를 버려서 N개를 만드는 것은 불가능하다. 즉, 구매한 카드팩에 포함되어 있는 카드 개수의 합은 N과 같아야 한다.

입력
첫째 줄에 민규가 구매하려고 하는 카드의 개수 N이 주어진다. (1 ≤ N ≤ 1,000)

둘째 줄에는 Pi가 P1부터 PN까지 순서대로 주어진다. (1 ≤ Pi ≤ 10,000)

출력
첫째 줄에 민규가 카드 N개를 갖기 위해 지불해야 하는 금액의 최댓값을 출력한다.

예제 입력 1 
4
1 5 6 7
예제 출력 1 
10
예제 입력 2 
5
10 9 8 7 6
예제 출력 2 
50
예제 입력 3 
10
1 1 2 3 5 8 13 21 34 55
예제 출력 3 
55
예제 입력 4 
10
5 10 11 12 13 30 35 40 45 47
예제 출력 4 
50
예제 입력 5 
4
5 2 8 10
예제 출력 5 
20
예제 입력 6 
4
3 5 15 16
예제 출력 6 
18
"""

import sys
input = sys.stdin.readline

def main():
    N = int(input().rstrip('\n')) # 1 <= N <= 10000
    values = [0] + list(map(int,input().rstrip("\n").split(" "))) # 1 <= P_i <= 10000
    dp = [0] * (N+1)
    # 1 6 9 6 # => # 1 6 9 12
    # 3 7 8 9 10 => # 3 7 10 14 
    # 1 2 4 4 5 => 만약 dp 문제로 바꿔 매 순간의 최대로 바꾼다면, 
    # dp list에서 2개를 골라 합이 최대가 되게끔 하는 것이다. 예) 2 2 1장을 뽑는다고 함은, 4장일 때 최댓값과 1장일 때를 더한 것임.
    # 2, 3, 3, 5가 최대라면, (이건 근데 5가 이미 최대이기에 2, 3, 3, 2, 3을 뽑는 것임) 8번째와 5번째, 10번째와 3번째를 뽑는 것이 같음.
    # 5, 7, 11, 13이 최대라면, 12, 24뽑아도 최대, 18, 18 뽑아도 최대일 것이다.

    dp[1] = values[1]

    for i in range(2,N+1): # 합이 N이 되는 두 자연수의 집합에서 dp합 중 최대를 구하면 됨.
        dp[i] = max([dp[j]+dp[i-j] for j in range(1, (i// 2 + 1))] + [values[i]])        
    
    print(dp[N])
        

if __name__ == '__main__':
    main()











