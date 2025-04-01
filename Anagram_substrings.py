
source = 'adobecodebanc'
target = 'abc'

def str_to_lst(word):
    letters = []
    i = 0
    while i < len(word):
        letters.append(str(word)[i])
        i += 1
    return letters

def find_window(src, tgt):
    word = ''
    add = False
    found = []
    psbl_windows = []
    for i in src:
        if i in tgt:
            add = True
            word += i
            found.append(i)
            if len(found) == 3:
                psbl_windows.append(word)
                add = False
                word = ''
                found.clear()

        elif add == True and len(found) != 3:
            word+=i
        elif add == True and len(found) == 3:

            add = False
            psbl_windows.append(word)
            word = ''
            found.clear()

    return psbl_windows



windows = find_window(str_to_lst(source), str_to_lst(target))
least_count = 0
count = 0
for window in windows:
    if count == 0:
        least_count = len(window)
    else:
        if least_count > len(window):
            least_count = len(window)
    count += 1


print(f'Smallest part : {windows[count-1]}, Length : {least_count}')

