# Write function longest_consecutive_sequence(nums). Given unsorted list of integers, return length of longest run of consecutive integers (order doesn't matter in input, gaps in list allowed elsewhere).

def longest_consecutive_sequence(nums):
    nums.sort()
    seq_len = 1
    max_len = 1

    i = 0
    while i < len(nums):
        if (i + 1) < len(nums):
            if nums[i + 1] == nums[i] + 1:
                seq_len += 1
                max_len = max(seq_len, max_len)
            else:
                seq_len = 1

        i += 1

    return max_len

print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2])) # -> 4, sequence is 1,2,3,4
print(longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])) # -> 9
print(longest_consecutive_sequence([1, 2, 3, 10, 11, 12, 13, 14]))