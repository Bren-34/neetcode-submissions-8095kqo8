class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            length = len(word)
            encoded += str(length) + '#' + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            # 1. find the '#'
            while s[j] != '#':
                j += 1

            # 2. get the length
            length = int(s[i:j])

            # 3. move to start of word
            j += 1

            # 4. extract word
            word = s[j:j + length]
            decoded.append(word)

            # 5. move i forward
            i = j + length

        return decoded