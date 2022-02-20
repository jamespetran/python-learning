def fruits_into_baskets(fruits):
    window_start = 0
    # initial index of window is 0
    max_length = 0
    # initial max window_length = 0
    fruit_frequency = {}
    # dictionary containing the fruits

    # try to extend the range [window_start, window_end]
    for window_end in range(len(fruits)):
        # trying different window ends by range() index
        right_fruit = fruits[window_end]
        # setting the right end fruit to the fruit item at index window_end
        if right_fruit not in fruit_frequency:
            # checking if right fruit is contained withing the dictionary
            fruit_frequency[right_fruit] = 0
            # if not contained: then add it with frequency value = 0
        fruit_frequency[right_fruit] += 1
        # add 1 to frequency of this fruit

    # shrink the sliding window, until we are left with '2' fruits in the fruit
    # frequency dictionary

    # now what in the world if a frequency dictionary
    # https://docs.python.org/3/tutorial
    # brb

    # ok

        while len(fruit_frequency) > 2:
            # this runs while there are more than 2 fruits in the dictionary
            left_fruit = fruits[window_start]
            # grab the fruit contained at the start of the window
            fruit_frequency[left_fruit] -= 1
            # remove that fruit occurrence from the dictionary
            if fruit_frequency[left_fruit] == 0:
                # check to see if that made the frequency fall to zero
                del fruit_frequency[left_fruit]
                # if frequency == 0 then delete it from the dictionary
            window_start += 1
            # shrink the window
        max_length = max(max_length, window_end-window_start + 1)
        # check if max length has changed -> assign it to maximum of ( prev value OR window_length + 1)
    return max_length
    # return the max length value once the
    # for window_end in range(len(fruits)):
    # has run through the whole fruits[] list beginning to end


def main():
    print("maximum number of fruits: "
          + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("maximum number of fruits: "
          + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
