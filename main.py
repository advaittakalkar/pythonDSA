# print("programming asaan hai")
# variable -- ctrl + /  -- comment

length = 100 #variable is saved in RAM
# print(id(length))  # output - 140715523596168  RAM memory address where the variable is stored
breadth = 200
print(id(length),id(breadth))  # 140715523596168 140715523599368

length1 = 500
breadth1 = 500
# see the address in output for same values of variables
print(id(length1), id(breadth1))  #2819907959728 2819907959728   --> same address for different variables with same values
# dono variable same object ko points kar rahe hai


length_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistry = "Advait"
is_home = True
print(length_of_land, bricks_cost_per_piece, labour_mistry, is_home)

print(type(length_of_land), type(bricks_cost_per_piece), type(labour_mistry), type(is_home))


##########################################################print##################################################################################

