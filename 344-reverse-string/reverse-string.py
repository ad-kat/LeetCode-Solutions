class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=len(s)
        h=l//2
        i=0
        while i<h:
            tmp=s[i]
            s[i]=s[l-1-i]
            s[l-1-i]=tmp
            i+=1
        


        