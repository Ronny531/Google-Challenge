from itertools import combinations
from itertools import permutations


listofnum = [3,1,4,1,5,9]
listofnum = set(listofnum)




def solution(L):
    # Your code here
    #L = set(L)
    print(L)
    listofcombos = []

    newlist = []
    count = len(L)+2
    for i in range(0, len(L)+1):
        #for subset in combinations(l, i):

        while count > 0:
            for subset in permutations(L, count):
                newlist.append(subset) 
                #print(subset)
            count -= 1

    #print(newlist[0])
    evennewerlist = []
    string = ''
    for item in newlist:
        for i in item:
            string = string+str(i)
        
        evennewerlist.append(int(string))
        string = ''
    #print(evennewerlist)

    evennewerlist = sorted(evennewerlist, reverse=True)
    #print(evennewerlist)
    counter = 0
    highestnum=0
    for num in evennewerlist:
        if num%3==0:
            highestnum = num
            #print(highestnum)
            break
        elif counter == len(evennewerlist)-1:
            break
        else:
            continue
    return highestnum



L = [3, 1, 4, 1]

#print(solution([3, 1, 4, 1]))
print(solution(L))
