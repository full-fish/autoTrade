
bought_list_current_price = [1,2,3]
bought_list =['a','b','c']
code = 'b'
bought_list_current_price.pop(bought_list.index(code))  # index로 나온건 숫자 1
bought_list.remove(code)
print(bought_list, bought_list_current_price)