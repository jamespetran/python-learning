#  Given a string, find the length of the longest substring, which has all distinct characters.
# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring with distinct characters is "abc".

# are provided comments
# are my own inferred comments

def non_repeat_substring(str1):
    window_start, max_length = 0, 0
    # initialize the beginning of the window and the max length = 0
    char_index_map = {}
    # initialize the dictionary for the substring values

    # try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        # loop through all substrings in str1
        right_char = str1[window_end]
        # assign str1 character at index [window_end] to right_char
        # if the map already contains the right_char, shrink the window
        # from the beginning
        # so that we have only one occurrence of 'right_char'
        if right_char in char_index_map:
            # (this is tricky?) in the current window we will not have any
            # 'right_char' after its previous index and if 'window_start'
            # is already ahead of the last index of 'right_char',
            # we'll keep 'window_start'

            # basically if right_char is already contained within the dictionary,
            # move the window_start value forward by one.
            # if right_char is not contained in the dictionary,
            # keep window start where it is
            window_start = max(window_start, char_index_map[right_char] + 1)
        # insert right_char into the map
        char_index_map[right_char] = window_end
        # remember the max length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print("Length of the longest substring: " +
          str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abcvndjsakcdeplm")))


main()
