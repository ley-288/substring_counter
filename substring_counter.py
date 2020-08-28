
def longestUniqueSubsttr(string):
    #create variables.use a set to store last position
    already_counted = {}
    maximum_length_of_sub = 0
    start_of_string = 0
    #pass through string
    for end in range(len(string)):

        #if already seen
        if string[end] in already_counted:
            #move to next letter after already counted string
            start = max(start_of_string, already_counted[string[end]] + 1)

            #update the counted to = that of substring
        already_counted[string[end]] = end
        #update max length to equal end minus start + 1
        maximum_length = max(maximum_length_of_sub, end - start_of_string + 1)
    return maximum_length_of_sub


string = "bbbbb"
print("In: ", string)
length = longestUniqueSubsttr(string)
print("Out: ", length)