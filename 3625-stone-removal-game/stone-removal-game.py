class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove =10
        turn=0 #odd=alice, even=bob
        while n>=remove:
            n=n-remove
            remove-=1
            turn+=1



        return True if turn%2==1 else False
        