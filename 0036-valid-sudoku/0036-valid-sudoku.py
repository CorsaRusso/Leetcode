class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_boxes = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                cur_num = board[i][j]
                
                # check rows
                if cur_num in rows[i]:
                    return False
                else:
                    rows[i].add(cur_num)
                
                # check columns
                if cur_num in cols[j]:
                    print("IN COL")
                    return False
                else:
                    cols[j].add(cur_num)
                
                # check sub_boxes
                sub_box_num = i // 3 + (j // 3) * 3
                if cur_num in sub_boxes[sub_box_num]:
                    print("In Sub Box")
                    return False
                else:
                    sub_boxes[sub_box_num].add(cur_num)
        return True
        
        