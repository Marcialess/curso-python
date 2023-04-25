words = " Las Cadenas de texto son iterables "

word = ' '
for letters in words:
    if letters != ' ':
        word += letters
    else:
        print(word)
        word = ' '

        for letters in words:
         if letters != ' ':
             word += letters
         else:
            print(word)
            break
         word = ' '

        animal_list = ['perro','gato','ardilla','ganso']
        for animal in animal_list:
           print(animal)

           list1 = range(2,3)
           print(list1)

        #    for number_list in range(1,100,5):
        #       print(number_list)
         

        for num_tabla in range(1, 11):
            for num_nul in range(1,11):
                 result = num_tabla * num_nul
                 print(f'{num_tabla} X {num_nul} = {result}')
                 
           