class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [[p, s] for p, s in zip(position, speed)]
        sorted_pair = sorted(pair, reverse=True)

        


        def eta(p,s):
            return (target-p)/s

        stack = []
        stack.append(eta(sorted_pair[0][0], sorted_pair[0][1]))

        for p,s in sorted_pair:
            
            latest = eta(p,s)
            # print(p,s,latest)

            if latest > stack[-1]:
                stack.append(latest)
        
        return len(stack)