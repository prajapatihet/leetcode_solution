class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        lstLeft,lstRight= [0]*n,[0]*n
        stack=[]
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                lstLeft[i] = -1
            else:
                lstLeft[i] = stack[-1]
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                lstRight[i] = n
            else:
                lstRight[i] = stack[-1]
            stack.append(i)
        max_area=0
        for i in range(n):
            max_area = max(max_area,heights[i]*(lstRight[i]-lstLeft[i]-1))
        return max_area