import heapq
import time

def ADAWalking(R, C, h, grid):
    
    # initialize the distance matrix
    distance = [[float('inf')] * C for _ in range(R)]
    distance[0][0] = 0

    # priority queue (min-heap) to process cells in increasing order of time taken
    pq = [(0, 0, 0, 0)]  # time, spiky cell count, row, col

    # keep track of visited states
    visited = set()

    # possible movements (right, down, left, up)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # dijkstra's algo
    while pq:
        time, spiky_count, row, col = heapq.heappop(pq)

        # track how many spiky cells have been stepped on
        state = (row, col, spiky_count)
        
        if state in visited:
            continue
        
        visited.add(state)
        distance[row][col] = min(distance[row][col], time)  # update shortest time
        
        # explore all directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # skip if out of bounds
            if not (0 <= new_row < R and 0 <= new_col < C):
                continue
            
            # identify the type of cell
            cell_type = grid[new_row][new_col]
            new_time = time
            new_spiky = spiky_count
            
            # handle casessss
            if cell_type == 0:  # rocky cell
                continue
            if cell_type == 1:  # empty cell
                new_time += 1
            elif 2 <= cell_type <= 5:  # meuddy cells
                new_time += cell_type
            elif cell_type == -1:  # teleport cell
                new_time += 1
            elif cell_type == -2:  # spiky cell
                if spiky_count >= h:
                    continue  # cannot step on more spiky cells
                new_time += 1
                new_spiky += 1

            # if the new state hasn't been visited add it to the priority queue
            if (new_row, new_col, new_spiky) not in visited:
                heapq.heappush(pq, (new_time, new_spiky, new_row, new_col))
        
        if grid[row][col] == -1:

            # move to the farthest teleport cell in the row aka right
            for j in range(C-1, col, -1):
                if grid[row][j] == -1:
                    if (row, j, spiky_count) not in visited:
                        heapq.heappush(pq, (time + 1, spiky_count, row, j))
                    break

            # ove to the farthest teleport cell in the row aka left
            for j in range(0, col):
                if grid[row][j] == -1:
                    if (row, j, spiky_count) not in visited:
                        heapq.heappush(pq, (time + 1, spiky_count, row, j))
                    break
            
            # move to the farthest teleport cell in the column aka downward
            for i in range(R-1, row, -1):
                if grid[i][col] == -1:
                    if (i, col, spiky_count) not in visited:
                        heapq.heappush(pq, (time + 1, spiky_count, i, col))
                    break

            # move to the farthest teleport cell in the column aka upward
            for i in range(0, row):
                if grid[i][col] == -1:
                    if (i, col, spiky_count) not in visited:
                        heapq.heappush(pq, (time + 1, spiky_count, i, col))
                    break

    return [[-1 if d == float('inf') else d for d in row] for row in distance]

def main():
    """
    Reads input, processes multiple test cases, and prints the results.
    """
    I = int(input())  # Number of test instances

    for _ in range(I):
        R, C, h = map(int, input().split())  # Read grid dimensions and max spiky steps
        grid = [list(map(int, input().split())) for _ in range(R)]  # Read the grid
        
        # Compute the shortest time matrix
        result = ADAWalking(R, C, h, grid)

        # Print the result as a matrix
        for row in result:
            print(" ".join(map(str, row)))

""" def test():
    
    print("\nTest Case 1:")
    R1, C1, h1 = 2, 5, 0
    grid1 = [
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1]
    ]
    expected1 = [
        [0, -1, 4, 5, 6],
        [1, 2, 3, -1, 7]
    ]
    result1 = ByteADAWalking(R1, C1, h1, grid1)
    print("Expected:")
    for row in expected1:
        print(" ".join(map(str, row)))
    print("Got:")
    for row in result1:
        print(" ".join(map(str, row)))
    
    print("\nTest Case 3:")
    R3, C3, h3 = 2, 5, 1
    grid3 = [
        [1, -2, 5, 1, 1],
        [3, -2, 1, -2, 1]
    ]
    expected3 = [
        [0, 1, 6, 7, 8],
        [3, 4, 5, -1, 9]
    ]
    result3 = ByteADAWalking(R3, C3, h3, grid3)
    print("Expected:")
    for row in expected3:
        print(" ".join(map(str, row)))
    print("Got:")
    for row in result3:
        print(" ".join(map(str, row)))
"""

""" def test_execution_time(R, C, h, grid):
    Measures the execution time of ByteADAWalking.
    start_time = time.time()
    result = ByteADAWalking(R, C, h, grid)
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.6f} seconds")

    return result

# Example usage:
if __name__ == "__main__":
    R, C, h = 2, 5, 0
    grid = [
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1]
    ]
    result = test_execution_time(R, C, h, grid)

    # Print result grid
    for row in result:
        print(" ".join(map(str, row)))
"""
if __name__ == "__main__":

    main()
    #test()