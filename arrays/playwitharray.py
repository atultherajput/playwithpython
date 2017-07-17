def listdemo():
    l = [5,4,3,2]
    for x in reversed(l):
        print (x)

'''Output:
2
3
4
5
'''
    l                                                       #[5, 4, 3, 2]
    reversed(l)                                     #<list_reverseiterator object at 0x7f1ebcf83a58>
    list(reversed(l))                             #[2, 3, 4, 5]
    l                                                       #[5, 4, 3, 2]
    l.reverse()
    l                                                       #[2, 3, 4, 5]

    l[-1]                                                 #5
    l                                                       #[2,3,4,5]

    l.pop()                                             #5
    l                                                       #[2,3,4]
    l.pop(1)                                           #3
    l                                                       #[2,4]

    l= range(10,-1,-1)
    l                                                       #range(10, -1, -1)
    l = list(l)
    l                                                       #[10,9,8,7,6,5,4,3,2,1,0]

    range(len(l))                                   #range(0, 11)
    list(range(len(l)))                           #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    reversed(list(range(len(l))))          #<list_reverseiterator object at 0x7f1ebcf83a58>
    list(reversed(list(range(len(l)))))  #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    l.reverse()
    l                                                         #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    a = list(range(11,16,1))
    a                                                        #[11, 12, 13, 14, 15]
    l.append(a)
    l                                                          #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12, 13, 14, 15]]
    l.append(16)                                      #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12, 13, 14, 15],16]

    b = list(range(17,21))
    b                                                         #[17,18,19,20]
    l.extend(b)
    l                                                           #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12, 13, 14, 15], 16, 17, 18, 19, 20]

    del l[6]
    l                                                            #[0, 1, 2, 3, 4, 5, 7, 8, 9, 10, [11, 12, 13, 14, 15], 16, 17, 18, 19, 20]

    c=[6]*3
    c                                                           #[6,6,6]
    l.insert(6,c)
    l                                                           #[0, 1, 2, 3, 4, 5, [6, 6, 6], 7, 8, 9, 10, [11, 12, 13, 14, 15], 16, 17, 18, 19, 20]

    l.insert(7,6)
    l                                                            #[0, 1, 2, 3, 4, 5, [6, 6, 6], 6, 7, 8, 9, 10, [11, 12, 13, 14, 15], 16, 17, 18, 19, 20]

    l.remove(6)
    l                                                            #[0, 1, 2, 3, 4, 5, [6, 6, 6], 7, 8, 9, 10, [11, 12, 13, 14, 15], 16, 17, 18, 19, 20]


###Loop
def loopdemo():
    print("Result of first loop")
    counter = 0
    while counter <= 5:
        print (counter),
        counter += 1
    else:
        print ("loop exited normally")
    # Here "else" is executed Output: 0 1 2 3 4 5 loop exited normally

    print("Result of second loop")
    for i in range(5):
      print (i),
      if i > 3:
       break
    else:
      print ("loop exited normally")
    # Here "else" is not executed because "break" happen Output: 0 1 2 3 4
loops()
