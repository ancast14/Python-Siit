#declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine)

my_list = [7,8,9,2,3,1,4,10,5,6]

#afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)

my_list_sort = my_list[:]
my_list_sort.sort()
print(my_list_sort)
print(my_list)

#afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)

my_list_reversed = my_list[:]
my_list_reversed.sort(reverse = True)
print(my_list_reversed)
print(my_list)

#afișează o listă ce conține numerele pare din lista ordonată (folosind slice)

my_list_evens = my_list_sort[1::2]
print(my_list_evens)

#afișează o listă ce conține numerele impare din lista ordonată (folosind slice)

my_list_odds = my_list_sort[::2]
print(my_list_odds)

#afișează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice)

my_list_div3 = list(filter(lambda x: (x % 3 == 0), my_list))
print(my_list_div3)
print(my_list)