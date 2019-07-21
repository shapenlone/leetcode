#_*_utf-8_*_

#add two Numbers
#Input:(2->4->3) + (5->6->7)
#Ouput:7->0->8

class Solution(object):
    def addTwoNumbers(self,l1,l2):
        """
        :type l1:ListNode
        :type l2:ListNode
        :rtype:ListNode
        """
        if l1 is None and l2 is None:
            return None
        l3 = 0
        result = []
        while l1 is not None or l2 is not None:
            r=(l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + l3
            l3 = r //10
            r= r %10
            result.append(r)
            l1 = l1.next
            l2 = l2.next
        return result

class ListNode(object):
    def __init__(self,v,n):
        self.val = v
        self.next = n

def buildNodeList(l:list):
    result =None
    length = len(l)
    if length == 1:
        return ListNode(l[0],None)
    for i in range(length-1,-1,-1):
        node = ListNode(l[i],result)
        result = node
    return result
    


if __name__ == "__main__":
     # 中文
     s = Solution()
     h = s.addTwoNumbers(buildNodeList([2,4,3]),buildNodeList([5,6,4]))
     print(h)
    


