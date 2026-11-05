from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

print("List :", all_thing_is_obj(ft_list))
print("Tuple :", all_thing_is_obj(ft_tuple))
print("Set :", all_thing_is_obj(ft_set))
print("Dict :", all_thing_is_obj(ft_dict))
print("Brian is in the kitchen :", all_thing_is_obj("Brian"))
print("Toto is in the kitchen :", all_thing_is_obj("Toto"))
print("Int :", all_thing_is_obj(10))