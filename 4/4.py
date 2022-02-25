from math import ceil
largestPalindrome = 0

for i in range(998):
    for j in range(998):
        num = i*j
        strnum = str(num)
        half = ceil(len(strnum)/2)
        if strnum[:half] == (strnum[::-1][:half]) and num > largestPalindrome:
            largestPalindrome = num

print(largestPalindrome)