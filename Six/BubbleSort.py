'''
冒泡排序
题目内容：
冒泡排序是一种简单的排序算法。它重复地遍历要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。遍历数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。
已知输入为一个列表，列表中的元素都为整数，我们定义冒泡排序函数为bubbleSort，将列表中的元素按从小到大进行排序后得到一个新的列表并输出，给出程序主体如下：
'''

def bubbleSort(alist):
    length = int(len(alist))
    for a in range(length):
        for b in range(0, length-a-1):
            if alist[b] > alist[b+1]:
                temp = alist[b]
                alist[b] = alist[b+1]
                alist[b+1] = temp
    return alist

alist=list(map(int,input().split()))
print(bubbleSort(alist))