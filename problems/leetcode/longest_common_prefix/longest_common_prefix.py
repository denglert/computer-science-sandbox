#!/usr/bin/env python


def longest_commont_prefix(string_list):

    if not string_list:
        return ''

    for i,c1 in enumerate(string_list[0]):

        for str in string_list[1:]:

            str_len = len(str)
            
            if i >= str_len:
                return string_list[0][:i]

            if c1 != str[i]:
                return string_list[0][:i]

    return string_list[0]

 
    


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


string_list = ["flow","flowi","flowe"]
lcp = longest_commont_prefix(string_list)

print("String list:")
print(string_list)
print(lcp)



string_list = ["dog","racecar","car"]
lcp = longest_commont_prefix(string_list)

print("String list:")
print(string_list)
print(lcp)


string_list = ["aa","a"]
lcp = longest_commont_prefix(string_list)

print("String list:")
print(string_list)
print(lcp)
