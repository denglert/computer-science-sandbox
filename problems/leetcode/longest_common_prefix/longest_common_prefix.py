#!/usr/bin/env python





def longest_commont_prefix(string_list):

    i = 0

    isCharMatch = True

    str_lens = [len(str) in string_list]


    while isCharMatch and i < min(str_lens):
            

        s = string_list[0][i]

        for str in string_list[1:]:

            if str[i] != s:
                isCharMatch = False
                break

        i += 1
    
    return string_list[0][:i-1]


string_list = ["flower","flow","flight"]
lcp = longest_commont_prefix(string_list)

print("String list:")
print(string_list)
print(lcp)


string_list = ["gazorpa","gazorpu","gazolba"]
lcp = longest_commont_prefix(string_list)

print("String list:")
print(string_list)
print(lcp)

