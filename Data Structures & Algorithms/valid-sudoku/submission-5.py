class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        start_row = 0
        start_columns = 0
        count = 0
        list_board = list()
        for row in board:
            _list = [n for n in row if n.isdigit()]
            if len(_list) != len(set(_list)):
                return False
        i = 9
        for index in range(i):
            numbers = list()
            for row in board:
                if row[index].isdigit():
                    numbers.append(row[index])
            if len(numbers) != len(set(numbers)):
                return False
        while start_row < 9:
            stop_row = start_row + 3
            three_columns = board[start_row:stop_row]
            while start_columns < 9:
                stop_columns = start_columns + 3
                list_temp = [
                    "".join([n for n in num[start_columns:stop_columns] if n.isdigit()])
                    for num in three_columns
                ]
                list_board.append("".join(list_temp))
                start_columns += 3
            temp = [n for n in list_board if n.isdigit()]
            for t in [n for n in list_board if n.isdigit()]:
                if len(t) != len(set(t)):
                    return False
            start_row += 3
            start_columns = 0
        return True