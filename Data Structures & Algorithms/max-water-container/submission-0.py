class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        max_volumn = 0

        

        while left < right:

            if min(height[left], height[right]) * (right - left) > max_volumn:
                max_volumn = min(height[left], height[right]) * (right - left)
            
            if height[left] < height[right]:
                left += 1
            
            elif height[left] > height[right]:
                right -= 1
            
            else:
              right -= 1
            

        
        return max_volumn



            
        