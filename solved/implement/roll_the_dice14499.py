"""
주사위 굴리기
2 초	512 MB
문제
크기가 N×M인 지도가 존재한다. 지도의 오른쪽은 동쪽, 위쪽은 북쪽이다. 이 지도의 위에 주사위가 하나 놓여져 있으며, 주사위의 전개도는 아래와 같다. 지도의 좌표는 (r, c)로 나타내며, r는 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 개수이다. 

  2
4 1 3
  5
  6
주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는 (x, y) 이다. 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.

지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.

주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램을 작성하시오.

주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

입력
첫째 줄에 지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20), 주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1), 그리고 명령의 개수 K (1 ≤ K ≤ 1,000)가 주어진다.

둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다. 지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0이다.

마지막 줄에는 이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.

출력
이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력한다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

예제 입력 1 
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2
예제 출력 1 
0
0
3
0
0
8
6
3
예제 입력 2 
3 3 1 1 9
1 2 3
4 0 5
6 7 8
1 3 2 2 4 4 1 1 3
예제 출력 2 
0
0
0
3
0
1
0
6
0
예제 입력 3 
2 2 0 0 16
0 2
3 4
4 4 4 4 1 1 1 1 3 3 3 3 2 2 2 2
예제 출력 3 
0
0
0
0
예제 입력 4 
3 3 0 0 16
0 1 2
3 4 5
6 7 8
4 4 1 1 3 3 2 2 4 4 1 1 3 3 2 2
예제 출력 4 
0
0
0
6
0
8
0
2
0
8
0
2
0
8
0
2
Input:
5 4 1 2 20
4 4 3 5 
0 6 8 4 
0 3 1 0 
7 6 6 4 
0 3 3 7 
1 4 4 1 2 2 1 3 4 2 1 3 2 4 1 4 2 2 2 4 

Output:
0
0
4
0
4
0
0
0
6
0
0
6
0
0
3
6
3


Expected:
0
0
4
0
4
0
0
0
4
0
0
4
0
0
3
0
3
"""

import sys
input = sys.stdin.readline

class Dice:
    
    def __init__(self, N, M, current_x, current_y):
        self.dice = [0,0,0,0,0,0]
        self.current_x = current_x
        self.current_y = current_y        
        self.N = N
        self.M = M
    
    def set_map(self, map):
        self.map = map
        
    def is_dice_out(self, x, y):
        return (x >= self.M or x < 0 or y >= self.N or y < 0) 
    
    def roll(self, cmd):
        # 명령 확인.
        if cmd == 1:
            x = self.current_x + 1
            y = self.current_y
        elif cmd == 2:
            x = self.current_x - 1
            y = self.current_y
        elif cmd == 3:
            x = self.current_x
            y = self.current_y - 1            
        elif cmd == 4:
            x = self.current_x
            y = self.current_y + 1
        
        if self.is_dice_out(x, y):   
            return
        
        self.current_x = x
        self.current_y = y
        # print(f"현재 위치: x:{self.current_x}, y:{self.current_y}")
        # dice 변경            
        if cmd == 1:            
            # swap
            self.dice[1], self.dice[2], self.dice[3], self.dice[5] = \
                self.dice[5], self.dice[1], self.dice[2], self.dice[3]
        elif cmd == 2:
            self.dice[1], self.dice[2], self.dice[3], self.dice[5] = \
                self.dice[2], self.dice[3], self.dice[5], self.dice[1]
        elif cmd == 3:  
            self.dice[0], self.dice[2], self.dice[4], self.dice[5] = \
                self.dice[5], self.dice[0],self.dice[2], self.dice[4]
        elif cmd == 4:            
            self.dice[0], self.dice[2], self.dice[4], self.dice[5] = \
                self.dice[2], self.dice[4],self.dice[5], self.dice[0]
                
        # 바닥확인
        if self.map[y][x] == 0:
            self.map[y][x] = self.dice[5]
        else:
            self.dice[5] = self.map[y][x]
            self.map[y][x] = 0
        
        print(self.dice[2])


def sol():
    N, M, x, y, K = map(int, input().rstrip().split(" "))
    dice = Dice(N, M, y, x) # 반대로 입력해야 함.
    
    board = [list(map(int, input().rstrip().split(" "))) for _ in range(N)]    
    dice.set_map(board)
    
    for cmd in map(int, input().rstrip().split(" ")):    
        dice.roll(cmd)
        

if __name__ == "__main__":
    sol()
        
        
        
    