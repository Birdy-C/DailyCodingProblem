'''
This problem was asked Microsoft.

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.
'''
'''
A simpler way to solve is to keep track of a remainder string. This string will represent the leftover text that couldn't be used in the previous readN() operation. Then all we'd need to do is call read7() until we have the desired n length. To make sure we handle the edge case of being end of file, we also need to exit if the call to read7() results in a text that's less than five characters:
'''
class Reader:
    def __init__(self):
        self.remainder = ''

    def readN(self, n):
        result = self.remainder
        text = None

        while len(result) < n and (text is None or len(text) >= 5):  // why 5
            text = read7()
            result += text

        self.remainder = result[n:]

        return result[:n]
