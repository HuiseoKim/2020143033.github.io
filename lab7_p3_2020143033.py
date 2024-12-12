class list_D2(list):
    def __init__(self, input_list):
        # Check if the input is a 2D list
        if not isinstance(input_list, list) or not all(isinstance(inner, list) for inner in input_list):
            raise ValueError("[ERROR]: list is not 2D.")
        
        # Check if any inner elements are lists (3D or higher)
        if any(isinstance(element, list) for inner in input_list for element in inner):
            raise ValueError("[ERROR]: list is not 2D.")
        
        # Check if all inner lists have the same length
        if len(set(len(inner) for inner in input_list)) > 1:
            raise ValueError("[ERROR]: inner lists are not same in length.")

        super().__init__(input_list)

    def __str__(self):
        # Return the dimensions as a string
        return f"list_2D: {len(self)}*{len(self[0])}"

    def transpose(self):
        # Return a new list_D2 instance with transposed values
        transposed = [[self[j][i] for j in range(len(self))] for i in range(len(self[0]))]
        return list_D2(transposed)

    def __matmul__(self, other):
        # Ensure the number of columns in self equals the number of rows in other
        if len(self[0]) != len(other):
            raise ValueError("[ERROR]: [a][b]*[c][d] not b==c.")

        # Matrix multiplication
        result = []
        for row in self:
            new_row = []
            for col in range(len(other[0])):
                value = sum(row[k] * other[k][col] for k in range(len(other)))
                new_row.append(value)
            result.append(new_row)

        return list_D2(result)

    def avg(self):
        # Compute the average value of all elements
        total_elements = sum(len(row) for row in self)
        total_sum = sum(sum(row) for row in self)
        return total_sum / total_elements