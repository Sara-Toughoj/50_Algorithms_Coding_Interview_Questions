def longestSubstring(str):
    str_length = len(str)

    if str_length <= 1:
        return str_length

    max_length = 1
    temp_string = str[0]
    temp_string[1]

    print(temp_string)

    # pointer = 1
    #
    # while pointer <= len(str)-1:
    #     if str[pointer] in temp_string:
    #         print()



print(longestSubstring("Hello"))
