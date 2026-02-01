class Solution:
    def merge(self, num1, m, num2, n):
        i,j,k = m-1,n-1,m+n-1
        while j >= 0:
            if i >= 0 and num1[i] > num2[j]:
                num1[k] = num1[i]
                i -= 1
            else:
                num1[k] = num2[j]
                j -= 1
            k -= 1
if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    sol = Solution()
    sol.merge(nums1, 3, nums2, 3)
    print(nums1)