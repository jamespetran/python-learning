#Given a string with lowercase letters only, if you are allowed to replace 
# no more than ‘k’ letters with any letter, find the length of the longest 
# substring having the same letters after replacement.

# Example 1:
#
# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# 
# 
# Example 2:
#
# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
# 
# 
# Example 3:
#
# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

def substr_replace(str, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    ## initialize all with 0:
        ## start of the sliding window
        ## maximum length of letters
        ## maximum repeated letters
    frequency_map = {}
    ## initialize the frequency dictionary
    
    for window_end in range(len(str)):
        ## run thru a for loop from index 0 to len(str)
        right_char = str[window_end]
        if right_char not in frequency_map:
            ## if the value in str at index [window_end]
            ## has not been encountered before, add it to freq 
            ## map and set init value= 0
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        ## +1 to freq_map for right_char
        max_repeat_letter_count = max(
            max_repeat_letter_count, frequency_map[right_char])
        ## see if frequency_map[right_char] occurs more than previous 
        ## max_r_l, if so, assign to max_r_l

# Current window size is from window_start to window_end, overall we have a letter 
# which is repeating 'max_repeat_letter_count' times, this means we can have a window 
# which has one letter repeating 'max_repeat_letter_count' times and the remaining 
# letters we should replace. If the remaining letters are more than 'k', it is the 
# time to shrink the window as we are not allowed to replace more than 'k' letters
## the if is checking if the window.length - max_r_l is more than k
## if yes: 
    ## work in from left at window_start
    ## remove left char from freq_map
    ## move window_start right one value as well
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = str[window_start]
            frequency_map[left_char] -= 1
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

def main():
    print(substr_replace("aabccbb", 2))
    print(substr_replace("abbcb", 1))
    print(substr_replace("abccde", 1))


main()
