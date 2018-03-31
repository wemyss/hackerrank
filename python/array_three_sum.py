# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# ******************** SOLUTION BELOW ********************

class Solution:
    def threeSum(self, S):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        S.sort()
        result = []
        # Example starting position
        #  a  b            c
        # [1, 2, 3, 4,..., n]
        # Move b and c towards each other until sum is found or they meet
        for a in range(0, len(S)-2):
            if a > 0 and S[a] == S[a-1]:
                continue

            b = a+1
            c = len(S)-1

            while b < c:
                if S[a] + S[b] + S[c] > 0:
                    c -= 1
                elif S[a] + S[b] + S[c] < 0:
                    b += 1
                else:
                    result.append([S[a],S[b],S[c]])
                    tmp = S[b]
                    while S[b] == tmp and b < c:
                        b += 1
        return result

