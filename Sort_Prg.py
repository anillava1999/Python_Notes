##  Sort a list  ##
''' Create a function in Python that accepts two parameters. The first will be a list of numbers. The second parameter will be a string that can be one of the following values: asc, desc, and none.

If the second parameter is “asc,” then the function should return a list with the numbers in ascending order. If it’s “desc,” then the list should be in descending order, and if it’s “none,” it should return the original list unaltered. '''


def sort_func():
    print("Enter the number of values for List")
    lst_values = int(input())
    print(lst_values)

    lst= []
    for i in range(lst_values):
        val = int(input("Enter the value"))
        lst.append(val)
    print(lst)


    print('''Choose any one option in below options
        1) Asc
        2) Desc
        3) None ''')
    answer = input()

    if(answer=='Asc'):
        print("Ascending Order")
        lst.sort()
    elif (answer=='Desc'):
        print("Descending Order")
        lst.sort(reverse=True)
    else:
        print("Orginal Order")

    print(lst)


    

