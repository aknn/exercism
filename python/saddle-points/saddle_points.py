def saddle_points(matrix):
    if not matrix:
        return []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Check for irregular matrix
    for row in matrix:
        if len(row) != num_cols:
            raise ValueError("irregular matrix")

    saddle_points_list = []

    for r in range(num_rows):
        row_max = max(matrix[r])
        for c in range(num_cols):
            if matrix[r][c] == row_max:
                # Check if it's the minimum in its column
                column_values = [matrix[i][c] for i in range(num_rows)]
                if matrix[r][c] == min(column_values):
                    saddle_points_list.append({"row": r + 1, "column": c + 1})

    return saddle_points_list