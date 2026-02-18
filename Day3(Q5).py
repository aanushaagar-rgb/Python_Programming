numbers = [1,2,3,4,5]

for i in range(len(numbers)-1):
    if numbers[i+1]!=numbers[i]+1:
        print("Not in matural progression")
        break
    else:
        print("In natural progression")