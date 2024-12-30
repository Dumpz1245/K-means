
target=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 's']
transactions = {
    100: ['a', 'c', 'd', 'f', 'g', 'i', 'm', 'p'],
    200: ['a', 'b', 'c', 'f', 'i', 'm', 'o'],
    300: ['c', 'f', 'h', 'j', 'o'],
    400: ['b', 'c', 'j', 'k', 's', 'p'],
    500: ['a', 'c', 'e', 'f', 'l', 'm', 'n', 'p']
}
counter=0
target_keys=[]
flag=False
for t in target:
    counter=0
    flag=False
    target_keys.clear()
    for keys in transactions:
        for values in transactions[keys]:
            if t == values:
                counter+=1
                target_keys.append(keys)
    if(counter>=3):
        print(target_keys," : "+t)
        counter=0
        
        