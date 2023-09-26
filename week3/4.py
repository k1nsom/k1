class node():#对节点进行定义。
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

def createlist(n):#创建一个新的链表。
    if n<=0:
        return False
    if n==1:
        return node(1)
    else:
        root = node(1)
        tmp = root
        for i in range(2, n+1):
            tmp.next = node(i)
            tmp = tmp.next
    return root

def printlist(head):#打印链表
    p = head
    while p != None:
        print(p.value)
        p = p.next
    return head
def listlen(head):#打印链表的长度
    c = 0
    p = head
    while p != None:
        c = c + 1
        p = p.next
    return c

def insert(head,n):#完成插入的功能
    if n<1 or n>listlen(head)+1:
        return head
    p = head
    for i in range(1,n-1):
        p = p.next
    a = input("enter a value:")
    t = node(value = int(a))
    if n == 1:
        t.next = head
        head = t
        return head
    t.next = p.next
    p.next = t
    return head
def modify(head):#要修改的值。
    n = int(input("enter the index to modify"))
    if n<0 or n>listlen(head):
        return head
    p = head
    m = int(input("enter the number you want"))
    for i in range(0,n-1):
        p = p.next
    p.value = m
    return head


def findlist(head):#完成查找的功能
    p = head
    a = input("enter a number to search")
    t = int(a)
    while p != None:
        print(p.value)
        if p.value == t:
            return "find it"
        else:
            p = p.next
    return "not find"

def dellist(head,n):#完成删除的功能
    if n < 1 or n > listlen(head):
        return head
    elif n == 1:
        head = head.next
        return head
        # print(head.value)
    else:
        p = head
        for i in range(1,n-1):
            p = p.next
        q = p.next
        p.next = q.next
    return head
def main():
    print("Create a linklist")
    head = createlist(7)
    printlist(head)
    print("-----------------")
    n1 = input("enter the index to insert")
    n1 = int(n1)
    head = insert(head,n1)
    printlist(head)
    print("-----------------")
    n2 = input("Enter the index to delete")
    n2 = int(n2)
    head = dellist(head,n2)
    head = printlist(head)
    print("----------------")
    myfind = findlist(head)
    print(myfind)
    change = modify(head)
    head = printlist(change)

if __name__=="__main__":
    main()