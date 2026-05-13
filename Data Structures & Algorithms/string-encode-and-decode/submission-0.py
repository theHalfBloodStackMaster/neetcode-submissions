class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        encodedString = ""
        for string in strs:
            encodedString += str(len(string)) + "#" + string
        
        return encodedString

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        decodedStrings = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decodedStrings.append(s[i:j])
            i = j


        return decodedStrings
