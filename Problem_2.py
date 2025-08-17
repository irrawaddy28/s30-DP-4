'''
1043 Parition Array for Maximum Sum
https://leetcode.com/problems/partition-array-for-maximum-sum/description/

Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.


Example 1:
Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]

Example 2:
Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83

Example 3:
Input: arr = [1], k = 1
Output: 1

Constraints:
1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length

Solution:
1. Recursion
Recursively try every partition of size up to k starting at index i. For each partition, we find the maximum in that subarray and add its contribution. We return the maximum among all such possible partitioned sums.
https://youtu.be/C-wjwRek6K0?t=3557
Time: O(k^N), Space: O(N) (N = no. of elements in array)

2. DP
Use a bottom-up DP 1d-array to track max sum up to each index. Thus, dp[i] = max sum (due to partitioning) up to index i. For every index i, we check all partitions of size up to k ending at i (thus start and end index pair of each partition are = <start, end> = <i, i> (len 1), <i-1,i> (len 2), <i-2,i>, ..., <i- (K-1),i> (len K). We calculate the contribution from the max element and update dp[i] accordingly.
https://youtu.be/C-wjwRek6K0?t=3892
Time: O(Nk), Space: O(N) (N = no. of elements in array)

'''

def maxSumAfterPartitioning_Recursion(arr, k):
    def recurse(arr, index, tot):
        nonlocal max_tot
        if index == N:
            max_tot = max(max_tot, tot)
            return

        for j in range(index, index+k):
            if j < N:
                l = j+1-index # len of subarray <= k
                this = max(arr[index:j+1])*l
                recurse(arr, j+1, tot+this)

    if not arr:
        return 0
    N = len(arr)
    max_tot = 0
    recurse(arr, 0, 0)
    return max_tot

def maxSumAfterPartitioning_DP(arr, k):
    if not arr:
        return 0
    N = len(arr)
    dp = [0]*N
    dp[0] = arr[0]
    for end in range(1, N):
        max_ele = arr[end] # last element of partition
        for ptn_len in range(1,k+1): # 1 <= len of partition <= k
            start = end - ptn_len + 1 # 1st ele of partition
            # Partition = arr[start] ... arr[end] = arr[start:end+1]
            if start < 0: # invalid partition
                continue
            dp_ind = start - 1
            if start >= 0:
                max_ele = max(max_ele, arr[start])
            if dp_ind >= 0:
                dp[end] = max(dp[end], dp[dp_ind] + ptn_len * max_ele)
            else:
                dp[end] = max(dp[end], ptn_len * max_ele)
    return dp[-1]

def run_maxSumAfterPartitioning():
    tests = [([1,15,7,9,2,5,10],3,84),
             ([1,4,1,5,7,3,6,1,9,9,3],4,83),
    ]
    for test in tests:
        arr, k, ans = test[0], test[1], test[2]
        print(f"\nArray = {arr}")
        print(f"k = {k}")
        for method in ['recur', 'dp']:
            if method == 'recur':
                max_sum = maxSumAfterPartitioning_Recursion(arr, k)
            elif method == 'dp':
                max_sum = maxSumAfterPartitioning_DP(arr, k)
            print(f"Method {method}: {max_sum}")
            success = (ans == max_sum)
            if not success:
                print('Failed')
                return

run_maxSumAfterPartitioning()