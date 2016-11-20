a=[3,2,1,5,2,4,6,9]


def compare(array):
    for i in array:
        count=0
        for j in range(0,len(array),1):
            if i==array[j]:
               count=count+1
        print str(i) + 'number' + str(count)

compare(a)

def swap(array):
    for j in range(0, len(array)-1,1):
        for i in range(0, len(array)-1, 1):
            if array[i]>array[i+1]:
                tempe=array[i+1]
                array[i+1]=array[i]
                array[i]=tempe

    print array
swap(a)