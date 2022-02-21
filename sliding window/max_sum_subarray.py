

def max_sub_array_of_size_k(k, arr):
    max_sum, window_sum = 0, 0
    window_start = 0

    # for item(at index Window_end), for max index value of len(arr)
    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add the next element
        # slide the window, no need ot slide if we've not hit the required window size of 'k'
        if window_end >= k-1:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead
    return max_sum


def main():
    print("Maximum sum of a subarray of size 3: " +
          str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size 2: " +
          str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
