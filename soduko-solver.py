numeric_range = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def isValid(rows, row, col, look):
    for i in range(0, 9):
        if rows[i][col] == look:
            return 0
        if rows[col][i] == look:
            return 0
        if rows[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == look:
            return 0
    return 1


def solve(rows):
    for i in range(0, 9):
        for j in range(0, 9):
            if rows[i][j] == '.':
                for look in numeric_range:
                    if isValid(rows, i, j, look):
                        rows[i][j] = look

                        if solve(rows):
                            return 1
                        else:
                            rows[i][j] = '.'
                return 0
    return 1


if __name__ == "__main__":
    fileRead = open("mySampleInputFile.txt", "r+")

    count = 9
    rows = []

    while(count):
        new_data = fileRead.readline().replace("\n", "")
        column = list(new_data.split(" "))

        rows.append(column)

        count -= 1

    solve(rows)
    print(rows)

    fileRead.close()
