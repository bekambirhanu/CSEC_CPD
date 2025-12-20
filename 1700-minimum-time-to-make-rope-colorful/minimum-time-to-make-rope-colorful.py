class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors+= '1'
        result= 0
        stack= []
        l= len(colors)
        for i in range(l):
            if(len(stack)>0 and colors[i] != stack[-1]):
                n= len(stack)
                k= i-n
                max_num= max(neededTime[k:i])
                total= sum(neededTime[k:i]) - max_num
                result+= total
                stack.clear()
            stack.append(colors[i])
            # if(i==l-1 and len(stack)>1):
            #     total= sum(neededTime[-1:-(len(stack)+1)])
            #     result+= total
        return result