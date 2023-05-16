# 121ms, beats 16%
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s1 = set()
            s2 = set()
            s3 = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in s1:
                    return False
                else: s1.add(board[i][j])
                # print(s2)
                if board[j][i] != '.' and board[j][i] in s2:
                    return False
                else: s2.add(board[j][i])
            r = i//3
            c = i%3
            for m in range(r*3,r*3+3):
                for n in range(c*3,c*3+3):
                    if board[m][n] != '.' and board[m][n] in s3:
                        return False
                    else: s3.add(board[m][n])
                    # print(s3)
        return True
