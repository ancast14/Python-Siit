#sa se scrie o functie care primeste un numar nedefinit de parametri si sa se calculeze suma parametrilor care reprezinta numere intregi sau reale

def sum_of_nums(*args, **kwargs):

    total = 0
    for num in args:
        if type(num) == int or type(num) == float:
            total += num
    return total

print(sum_of_nums(1, 5, -3, "abc", [12, 56, "cad"]))
print(sum_of_nums())
print(sum_of_nums(2, 4, "abc", param_1=2))
print(sum_of_nums(3, 5.8, "aaa"))

#sa se scrie o functie recursiva care primeste ca parametru un numar intreg si returneaza:
    #suma tuturor numerelor de la [0, n]
    #suma numerelor pare de la [0, n]
    #suma numerelor impare de la [0, n]

def get_sum(n):
    if n == 0:
        return (0, 0, 0)
    else:
        total_sum, even_sum, odd_sum = get_sum(n-1)
        sum_of_all = n+ total_sum
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n
        return(sum_of_all, even_sum, odd_sum)

print(get_sum(7))
print(get_sum(8))

#sa se scrie o functie care citeste de la tastatura si returneaza valoarea daca aceasta este un numar intreg, altfel returneaza valoarea 0

def show_int_num():
    try:
        a = int(input("a = "))
    except ValueError:
        a = 0
        return a
    print(a)

show_int_num()
print(show_int_num())

