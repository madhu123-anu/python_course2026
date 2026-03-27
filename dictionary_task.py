#EXERCISE
#1 dictionary update
my_dict={"name":"python","age":25}
my_dict["city"]="west godavari"
print(my_dict)

#2 dictionary access
product_info={"name":"laptop","brand":"dell","price":1200}
i=product_info["price"]
print(i)

#3 dictionary removal
my_dict={"name":"python","age":30,"city":"bhimavaram"}
my_dict2={"name":"john","age":30}
result=my_dict.update(my_dict2)
print(my_dict2)

#4 dictionary keys
my_dict={"name":"python","age":25,"city":"rajahmudhry"}
result=my_dict.keys()
print(result)

#5 dictionary values
my_dict={"name":"python","age":25,"city":"tanuku"}
result=my_dict.values()
print(result)

#EX1 dictionary update
my_list={"name":"hari","age":30,"city":"hyd"}
new_list={"name":"sreenu","age":25,"city":"tanuku"}
my_list.update(new_list)
print(my_list)

#EX2 dictionary access
my_list={"name":"hari","age":30,"city":"hyd"}
result=my_list["name"]
print(result)

#EX3 dictionary removal
my_list={"name":"hari","age":30,"city":"hyd"}
result=my_list.pop("city")
print(result)

#EX4 dictionary keys
my_dict={"name":"python","age":25,"city":"rajahmudhry"}
result=my_dict.keys()
print(result)

#EX5 dictionary values
my_dict={"name":"python","age":25,"city":"tanuku"}
result=my_dict.values()
print(result)
