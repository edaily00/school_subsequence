def is_subsequence(string_1, string_2):
    length_1 = len(string_1)
    length_2 = len(string_2)

    if length_1 == 0:
        return True

    elif length_2 == 0 and length_1 > 0:
        return False

    elif string_1[length_1-1] == string_2[length_2-1]:
        string_1 = string_1.replace(string_1[length_1-1], "")
        string_2 = string_2.replace(string_2[length_2-1], "")
        return is_subsequence(string_1, string_2)

    elif string_1[length_1-1] != string_2[length_2-1]:
        string_2 = string_2.replace(string_2[length_2-1], "")
        return is_subsequence(string_1, string_2)






