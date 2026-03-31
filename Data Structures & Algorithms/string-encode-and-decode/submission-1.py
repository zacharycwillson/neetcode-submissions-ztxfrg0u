class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += string + '🤣'
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        string_word = ""
        for letter in s:
            if letter == '🤣':
                decoded_list.append(string_word)
                string_word = ""
            else:
                string_word += letter
        return decoded_list

