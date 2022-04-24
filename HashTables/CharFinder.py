
class CharFinder:
    # Find the First Non-repeated Character
    def findFirstNonRepeatedChar(self, string):
        map = {}
        for ch in string:
            #if ch in map:
            #    map[ch] += 1
            #else:
            #    map[ch] = 1

            #map[ch] = map[ch] + 1 if ch in map else 1

            count = map.get(ch, 0)
            map[ch] = count + 1

        for ch in string:
            if map[ch] == 1:
                return ch

        return None

    # Find the first repeated character
    def findFirstRepeatedChar(self, string):
        map = set()
        for ch in string:
            if ch in map:
                return ch
            map.add(ch)
        return None

if __name__ == '__main__':
    finder = CharFinder()
    char = finder.findFirstNonRepeatedChar('a green apple')
    print(char)
    char = finder.findFirstRepeatedChar('a green apple')
    print(char)
