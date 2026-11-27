class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            alive = True
            while stack and a < 0 and stack[-1] > 0:
                if abs(a) > stack[-1]:
                    stack.pop()
                elif abs(a) < stack[-1]:
                    alive = False
                    break
                else:
                    alive = False
                    stack.pop()
                    break
            if alive:
                stack.append(a)
        
        return stack
                
