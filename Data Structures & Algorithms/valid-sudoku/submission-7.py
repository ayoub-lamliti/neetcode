class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        start_row = 0
        start_columns = 0
        rows = []
        columns = [[] for _ in range(9)]
        list_board = list()
        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n.isdigit():
                    rows.append(n)
                    columns[j].append(n)
            if len(rows) != len(set(rows)):
                return False
            rows.clear()
        for col in columns:
            if len(col) != len(set(col)):
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
            for t in [n for n in list_board if n.isdigit()]:
                if len(t) != len(set(t)):
                    return False
            start_row += 3
            start_columns = 0
        return True