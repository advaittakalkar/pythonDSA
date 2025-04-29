def plus_one(input):
    str_digit = ""
    for i in input:
        str_digit = str_digit + str(i)

    final_num = int(str_digit) + 1
    my_list = []
    for i in str(final_num):
        my_list.append(int(i))
    print(my_list)



if __name__=="__main__":
    input = [1,2,3]
    plus_one(input)