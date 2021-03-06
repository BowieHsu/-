#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    def permuteUnique(self,num):
        ras = []
        ras.append(num[:])
        num.sort()
        print self.dfs(num)
        if(self.dfs(num)):
            ras.append(num)
        return ras
    #next_permutation
    def dfs(self,num):
        if len(num) < 2:
            return num
        partition = -1
        for i in range(len(num) - 2, -1, -1):
            if num[i] < num[i + 1]:
                partition = i
                break
        if partition == -1:
            return num
        for i in range(len(num) - 1, partition, -1):
            if num[i] > num[partition]:
                num[i], num[partition] = num[partition], num[i]
                break
        num[partition + 1:] = num[partition + 1:][::-1]
        return num

instance = Solution()
r = [1,1,2]
print instance.permuteUnique(r)