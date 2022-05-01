class StringManipulation:
    @staticmethod
    def countVowelsMy(string: str) -> int:
        count = 0
        vowels = {'A', 'E', 'O', 'U', 'I', 'a', 'e', 'o', 'u', 'i'}
        for ch in string:
            if ch in vowels:
                count += 1
        return count

    @staticmethod
    def countVowels(string: str) -> int:
        if string == None: # In below, we assume all the inputs won't be None
            return 0
        count = 0
        vowels = 'aeiou' # Use set is better because it is faster to check item
        for ch in string.lower(): # return lowcased string
            if vowels.find(ch) != -1: # str.index() raises error if ch is not in the string
                count += 1
        return count

    @staticmethod
    def reverseStr(string: str) -> str:
        reversed = ''
        for i in range(len(string)-1, -1, -1):
            reversed += string[i]   # This operation creates a new string in memory each time, O(n)
        return reversed             # In Java, use StringBuilder interface

    @staticmethod
    def reverseStr2(string: str) -> str:
        return string[::-1] # Pythonic way

    @staticmethod
    def reverseStr3(string: str) -> str:
        reversed_list = [string[i] for i in range(len(string)-1, -1, -1)]
        return ''.join(reversed_list)

    @staticmethod
    def reverseStr4(string: str) -> str:
        return ''.join(reversed(string))

    @staticmethod
    def reverseOrderOfWords(string: str):
        words = string.strip().split(' ')
        return ' '.join(reversed(words))

    @staticmethod
    def areRotations(string1: str, string2: str) -> bool:
        # Using two pointers is one way
        # An elegant way is to double the string1 and check if sting2 is contained
        # But it uses more space when the strings are very long
        return len(string1) == len(string2) and string2 in string1+string1

    @staticmethod
    def removeDuplicates(string):
        output = []
        seen = set()
        for ch in string:
            if ch not in seen:
                seen.add(ch)
                output.append(ch)
        return ''.join(output)

    @staticmethod
    def getMostRepeatedChar(string):
        # if we do not have access to hash table, we can use the ASCII/Unicode number
        # use ord(ch) and chr()
        frequencies = {}
        for ch in string:
            frequencies[ch] = frequencies.get(ch, 0) + 1

        max_count = 0
        result = None
        for ch, count in frequencies.items():
            if count > max_count:
                max_count = count
                result = ch
        return result

    @staticmethod
    def capitalize(string):
        words = string.split() # if separator is not provided, all whitespaces are used as splitors.
        for i in range(len(words)):
            words[i] = words[i].capitalize()
        return ' '.join(words)

    @staticmethod
    def isAnagram(string1, string2): # sorting
        # Time Complexity O(n log n)
        if string1 == None or string2 == None or len(string1) != len(string2):
            return False
        # lower the case O(n); sort O(n log n); check equality O(n)
        return sorted(string1.lower()) == sorted(string2.lower()) # case insensitive

    @staticmethod
    def isAnagram2(string1, string2): # hash table
        # Time Complexity O(n)
        if string1 == None or string2 == None or len(string1) != len(string2):
            return False
        string1 = string1.lower()
        string2 = string2.lower()

        frequencies = {}
        for ch in string1:
            frequencies[ch] = frequencies.get(ch, 0) + 1

        for ch in string2:
            if frequencies.get(ch) and frequencies[ch] > 0:
                    frequencies[ch] -= 1
            else:
                return False
        return True

    @staticmethod
    def isPalindrome(string):
        return string == ''.join(reversed(string)) # O(n)

    @staticmethod
    def isPalindrome(string): # two pointers
        l, r = 0, len(string)-1
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True
