class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""  # Initialize an empty string to store the merged result
        remainder = ""  # Initialize an empty string to store any remaining characters

        # Check if the length of word1 is less than the length of word2
        if len(word1) < len(word2):
            remainder = word2[len(word1):]  # Store the remaining characters of word2
        # Check if the length of word2 is less than the length of word1
        elif len(word2) < len(word1):
            remainder = word1[len(word2):]  # Store the remaining characters of word1

        # Iterate over the smaller of the two word lengths
        for i in range(min(len(word1), len(word2))):
            ans += word1[i]  # Append character from word1 to the result string
            ans += word2[i]  # Append character from word2 to the result string

        # Append any remaining characters (from the longer word) to the result string
        ans += remainder

        return ans  # Return the merged result

#       Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
