# 786. K-th Smallest Prime Fraction

"""
You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

Example 1:

Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.
Example 2:

Input: arr = [1,7], k = 1
Output: [1,7]
"""

from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        new_arr = [(x/y, x, y) for x in arr for y in arr if (x!=y and x<y)]
        new_arr.sort(key=lambda x: (x[0], x[1], x[2]), reverse=False)
        ans = [new_arr[k-1][1], new_arr[k-1][2]]
        return ans


"""
Đánh giá qua giải thuật trên:
- Ngắn gọn, dễ hiểu, dễ đọc
- Sử dụng List Comprehension để giải
- Tuy nhiên độ phức tạp là O(n^2 log(n)) do phải sắp xếp

Cách khác:
- Priority Queue -> O(k log(n))
- Binary Search -> O(len(max) log(n))
"""
