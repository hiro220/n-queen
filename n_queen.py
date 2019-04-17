# coding;utf-8

import sys
import numpy as np
from copy import deepcopy

class nQueen:

    def __init__(self, n):
        self.N = n
        self.board = [[True for i in range(self.N)] for j in range(self.N)]
        self.result = []
        if self.loop(0):
            self.printResult()
        else:
            print("Don't found")

    def setQueen(self, x, y):
        """boardの(x, y)にqueenを置く．queenをself.boardに置ける場所を更新する."""
        for i, gyo in enumerate(self.board):
            if i == y:
                self.board[y] = gyo and [False for j in range(self.N)]     # 行をすべてFalseにする
            else:
                gyo[x] = False                      # 列をFalseにする
                # 斜め列をFalseにする．
                i = y - i
                if 0 <= x - i < self.N:                  
                    gyo[x-i] = False
                if 0 <= x + i < self.N:
                    gyo[x+i] = False

    def loop(self, y):
        board = deepcopy(self.board)        # 詰んだときに元に戻せるようboardをコピー
        if y == self.N:
            return True                     # 探索完了
        # 現在指定されている行yについて，置ける場所を探索
        for x in range(self.N):
            if self.board[y][x]:
                self.setQueen(x, y)
                if self.loop(y+1):          # この位置で完成できたか
                    self.result.append([x, y])
                    return True
            # 探索失敗なのでboard情報を戻す
            self.board = deepcopy(board)
        return False                        # 探索失敗

    def printResult(self):
        result = [['N' for j in range(self.N)] for i in range(self.N)]
        result = np.array(result)
        for x, y in self.result:
            result[y][x] = 'Q'
        print(result)
        
if __name__=='__main__':
    try:
        N = int(sys.argv[1])
    except IndexError:
        print("コマンドライン引数を指定してください．\nex) python n-queen.py 4")

    nQueen(N)