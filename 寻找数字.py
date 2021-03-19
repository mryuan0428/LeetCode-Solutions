# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input()
    l = len(s)
    
    res = []
    i = 0
    while i < l:
        if s[i].isdigit():
            j = i + 1
            while j < l:
                if s[j].isdigit():
                    j += 1
                else: break
            res.append(int(s[i:j]))
            i = j + 1
        else:
            i += 1
    res.sort()
    for num in res:
        print(num)



