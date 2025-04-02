
source = input('Enter the word you want to search from(Make sure there are no spaces): ')
target = input('Your Target: ')


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
            if i not in found:
                found.append(i)
            if len(found) == len(tgt):
                psbl_windows.append(word)
                add = False
                word = ''
                found.clear()

        elif add == True and len(found) != len(tgt):
            word+=i
        elif add == True and len(found) == len(tgt):

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

print(f'Smallest part : {windows}, Length : {least_count}')



# Another method:

'''from collections import Counter

def min_anagram_window(source: str, target: str) -> int:
    if not source or not target:
        return -1

    target_counter = Counter(target)
    required = len(target_counter)
    window_counts = {}
    formed = 0

    l = 0
    min_length = float("inf")

    # Expand the window with the right pointer
    for r, char in enumerate(source):
        window_counts[char] = window_counts.get(char, 0) + 1

        # If the current character is in target and count matches target's count, increment formed
        if char in target_counter and window_counts[char] == target_counter[char]:
            formed += 1

        # When we have a valid window, try to shrink it
        while l <= r and formed == required:
            # Update the answer if this window is smaller
            current_window_length = r - l + 1
            if current_window_length < min_length:
                min_length = current_window_length

            # Try to remove the left character from the window
            left_char = source[l]
            window_counts[left_char] -= 1
            if left_char in target_counter and window_counts[left_char] < target_counter[left_char]:
                formed -= 1
            l += 1

    return min_length if min_length != float("inf") else -1

# Example test cases:

print(min_anagram_window("mybalu", "mybalu"))  # Expected output: 4 ("banc")
print(min_anagram_window("aaabdabcefaecbef", "abc")) # Expected output: 3 ("bca")
'''