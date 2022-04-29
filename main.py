def file_worker(file_name: str):
    cook_book = {}
    cook_book_lst = []
    with open(file_name, 'r', encoding='utf-8') as file:

        for line in file:
            cook_book_lst.append(line.strip('\n'))
        while '' in cook_book_lst:
            cook_book_lst.remove('')

        def ingred_work(cook_book_lst):
            key_dish = cook_book_lst[0]
            cook_book[cook_book_lst[0]] = []
            del cook_book_lst[0]
            vol = int(cook_book_lst[0])
            del cook_book_lst[0]
            count = 0
            for element_cook_book_lst in cook_book_lst:
                if count != vol:
                    count += 1
                    el = element_cook_book_lst.split(' | ')

                    def dict_create(**structure):
                        cook_book[key_dish].append(structure)

                    dict_create(ingredient_name=el[0],
                                quantity=el[1],
                                measure=el[2])
            # print(len(cook_book_lst))
            del cook_book_lst[0: vol]
    while len(cook_book_lst) != 0:
        ingred_work(cook_book_lst)

    # Задача №2 при совпадении ингредиентов количество в нем суммируется
    dishes_dict = {}
    dishes_list = ['Омлет', 'Фахитос', 'Фахитос']
    def get_shop_list_by_dishes(dishes_list, person_count):
        for num_dish, dish in enumerate(dishes_list):
            for id, ingred in enumerate(cook_book[dish]):
                if ingred['ingredient_name'] not in dishes_dict:
                    def dict_parametr(**structure):
                        dishes_dict[ingred['ingredient_name']] = structure
                    dict_parametr(measure=ingred['measure'],
                                  quantity=(int(ingred['quantity']))*person_count)
                else:
                    dishes_dict[ingred['ingredient_name']]['quantity'] += \
                        int(cook_book[dish][id]['quantity'])*person_count

    get_shop_list_by_dishes(dishes_list, 3)

    print(cook_book) #Итог решения Задача №1
    print(dishes_dict) #Итог решения Задача №2
    return cook_book

file_worker('recept.txt')



