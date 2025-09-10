list = [1,2,3,4,5,1,2,3,4,5,5,2,2,3,4,5,1,2,3,4,5]
for i in range (len(list)-1):
    if list[i] == list[i+1]:
        print("False!")
        break
else:
    print("True!")