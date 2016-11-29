def main():
    groceries = ['apples', 'granola', 'eggs', 'milk']
    moreGroceries = ['bread', 'bacon', 'turkey']
    # groceries.append(moreGroceries[1])
    print(groceries)
    # groceries.extend(moreGroceries)
    print(groceries)
    groceries.insert(0, moreGroceries)
    print("After insert",groceries)
    # groceries.remove(moreGroceries)
    groceries[0].remove('bread')
    print('groceries after remove',groceries)
    #remove uses given value, pop uses index

    print( groceries.pop(0))
    print("groceries after pop {}".format(groceries))

    # print(groceries.clear())
    print(groceries.index('milk'))
    milkIndex = groceries.index('milk')
    print(groceries.pop(milkIndex))
    print(groceries)
    groceries.append('milk')
    groceries.insert(1, 'milk')
    print(groceries)
    print(groceries.count('milk'))
    groceries.sort()
    print('Sorted', groceries)
    groceries.reverse()
    print(groceries)







if __name__ == '__main__': main()