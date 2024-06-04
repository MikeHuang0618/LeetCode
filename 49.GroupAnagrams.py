'''
Coder: Mike Huang
Date: 2024/02/15

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 104
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
'''

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = {}

        for s in strs:
            sorted_str = ''.join(sorted(s))
            
            if sorted_str in group_map:
                group_map[sorted_str].append(s)
            else:
                group_map[sorted_str] = [s]
            print(group_map)
        optimized_double_list = list(group_map.values())
        return optimized_double_list


if __name__ == '__main__':
    solution = Solution()

    print(solution.groupAnagrams(["stop","pots","reed","","tops","deer","opts",""]))