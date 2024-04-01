### Simplest approach

class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = "π".join(strs)
        print(encoded)
        return encoded
        

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = s.split('π')
        print(decoded)
        return decoded
        
        
codec = Codec()
codec.decode(codec.encode(strs=["","HI"]))


##### Approach that takes into consideration any character 

class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        print(''.join(f'{len(string)}#{string}' for string in strs))
        return ''.join(f'{len(string)}#{string}' for string in strs)
        
        

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        res, i = [], 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1 
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        print(res)
        return res


codec = Codec()
codec.decode(codec.encode(strs=["","HI","There"]))     
                
