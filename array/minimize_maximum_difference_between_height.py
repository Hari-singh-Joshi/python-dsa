def min_height_difference(arr):
    arr.sort()  # Sort the array
    
    # Calculate K dynamically based on the difference between the minimum and maximum elements
    K = (arr[-1] - arr[0]) // 2
    
    # Calculate the initial difference between the tallest and shortest towers
    min_height = arr[0] + K
    max_height = arr[-1] - K
    initial_diff = max_height - min_height
    
    # Try to adjust the height of each tower and update the minimum difference
    for i in range(len(arr) - 1):
        height_add = arr[i] + K
        height_subtract = arr[i + 1] - K
        new_min = min(min_height, height_subtract)
        new_max = max(max_height, height_add)
        new_diff = new_max - new_min
        initial_diff = min(initial_diff, new_diff)
    
    return initial_diff

# Example usage:
arr = [1, 5, 8, 10]
print(min_height_difference(arr))
