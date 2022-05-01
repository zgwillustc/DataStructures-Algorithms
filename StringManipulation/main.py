from String import StringManipulation

string1 = 'hello'
string2 = ''
string3 = 'Trees are beautiful'
string4 = '   Trees are beautiful   '
string5 = 'ohell'
string6 = 'llohe'
string7 = '   tREeS   aRe      beAuTIFuL   '
string8 = 'lHoLE'
string9 = 'madam'

def main():
    print('Find the number of vowels:')
    print('\tString:', string1)
    print('\tNumber of vowels:', StringManipulation.countVowels(string1))
    print('\tString:', string2)
    print('\tNumber of vowels:', StringManipulation.countVowels(string2))
    print('\tString:', string3)
    print('\tNumber of vowels:', StringManipulation.countVowels(string3))

    print('\nReverse the string:')
    print('\tString:', string1)
    print('\t', StringManipulation.reverseStr(string1))
    print('\tString:', string2)
    print('\t', StringManipulation.reverseStr2(string2))
    print('\tString:', string3)
    print('\t', StringManipulation.reverseStr3(string3))

    print('\nReverse the order of words:')
    print('\tString:', string1)
    print('\t', StringManipulation.reverseOrderOfWords(string1))
    print('\tString:', string2)
    print('\t', StringManipulation.reverseOrderOfWords(string2))
    print('\tString:', string4)
    print('\t', StringManipulation.reverseOrderOfWords(string4))

    print('\nTwo strings are rotations:')
    print('\tStrings:', string1, string5)
    print('\t', StringManipulation.areRotations(string1, string5))
    print('\tStrings:', string5, string6)
    print('\t', StringManipulation.areRotations(string5, string6))
    print('\tStrings:', string1, string2)
    print('\t', StringManipulation.areRotations(string1, string2))

    print('\nRemove duplicates:')
    print('\tString:', string1)
    print('\t', StringManipulation.removeDuplicates(string1))
    print('\tString:', string2)
    print('\t', StringManipulation.removeDuplicates(string2))
    print('\tString:', string3)
    print('\t', StringManipulation.removeDuplicates(string3))

    print('\nMost repeated character:')
    print('\tString:', string1)
    print('\t', StringManipulation.getMostRepeatedChar(string1))
    print('\tString:', string2)
    print('\t', StringManipulation.getMostRepeatedChar(string2))
    print('\tString:', string3)
    print('\t', StringManipulation.getMostRepeatedChar(string3))

    print('\nCapitalize the first letter of each word:')
    print('\tString:', string1)
    print('\t', StringManipulation.capitalize(string1))
    print('\tString:', string2)
    print('\t', StringManipulation.capitalize(string2))
    print('\tString:', string7)
    print('\t', StringManipulation.capitalize(string7))

    print('\nCheck if two strings are anagrams using sorting:')
    print('\tString:', string1, string5)
    print('\t', StringManipulation.isAnagram(string1, string5))
    print('\tString:', string2, string2)
    print('\t', StringManipulation.isAnagram(string2, string2))
    print('\tString:', string5, string8)
    print('\t', StringManipulation.isAnagram(string5, string8))

    print('\nCheck if two strings are anagrams using histogramming:')
    print('\tString:', string1, string5)
    print('\t', StringManipulation.isAnagram2(string1, string5))
    print('\tString:', string2, string2)
    print('\t', StringManipulation.isAnagram2(string2, string2))
    print('\tString:', string5, string8)
    print('\t', StringManipulation.isAnagram2(string5, string8))

    print('\nCheck if the string is palindrome:')
    print('\tString:', string1)
    print('\t', StringManipulation.isPalindrome(string1))
    print('\tString:', string2)
    print('\t', StringManipulation.isPalindrome(string2))
    print('\tString:', string9)
    print('\t', StringManipulation.isPalindrome(string9))

    print('\nCheck if the string is palindrome using two pointers:')
    print('\tString:', string1)
    print('\t', StringManipulation.isPalindrome(string1))
    print('\tString:', string2)
    print('\t', StringManipulation.isPalindrome(string2))
    print('\tString:', string9)
    print('\t', StringManipulation.isPalindrome(string9))


if __name__ == '__main__':
    main()
