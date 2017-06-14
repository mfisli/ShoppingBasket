#shoppingBasket.py
# takes in an item, a quanity, and a cost
# Allows CRUD operation on the shopping list 

#todo: change item to dict eg {'apple': [1,0.99]}
# add pretty shopping list print out 
# add update function 
# add delete function 
import ast

class Record(object):

	def __init__(self, shopping_list = {}, total = 0.00):
		print("Init record")
		self.shopping_list = shopping_list	
		self.total = total    

def show_cmds():
	print(
"c = create new item \n\
r = read current shop record\n\
u = update existing item\n\
d = delete existing item\n\
s = save current shop record\n\
x = exit")


def is_valid_quanity():
	while True:
		quanity = input("Enter item quanity: ")
		try:
   			val = int(quanity)
		except ValueError:
   			print("That is not a valid quanity.")
   			continue
		return val

def is_valid_name():
	while True:
		name = input("Enter item name: ")
		try:
			float(name)
			print("Name cannot be a number.")
			continue
		except ValueError:
			# remove whitespace and make lower case
			return name.strip(' ').capitalize()

def is_valid_price():
	while True:
		quanity = input("Enter item price: ")
		try:
   			val = float(quanity)
		except ValueError:
   			print("That is not a valid price.")
   			continue
		return val

def create_item():
	print("Creating new item. ")
	key = is_valid_name()
	quanity = is_valid_quanity()
	price = is_valid_price()
	record.shopping_list[key] = [quanity, price]

def read_items():
	if len(record.shopping_list) != 0:
		print("Reading and calculating items.")
		# print(">>>", record.shopping_list.items(), "of len" , len(record.shopping_list))	
		total = 0.00
		print(30 * "_")
		print("|{:10}{:10}{:10}|".format('Name','Quantity','Price'))
		print(30 * "_")								
		for item in record.shopping_list.items():
			name = item[0]
			quantity = item[1][0]
			price = item[1][1]
			total += price * quantity
			print("|{:<10}{:<10}{:<10}|".format(name,quantity,price))
		print(30 * "_")
		print("Total: ${}\n".format(total))
	else:
		print("No items.")	

def save_to_file():
	print("Saving to file.")
	target_file = open("data.txt", "w")
	#print(target_file)
	target_file.write(str(record.shopping_list))
	target_file.close()

def load_last_shop():
	user_input = input("Load last shop record? (y/n)")
	if user_input != 'n':
		print("Loading last shop.")
		target_file = open("data.txt", "r")
		shopping_list_raw = target_file.read()
		shopping_list = ast.literal_eval(shopping_list_raw)
		record.shopping_list = shopping_list
		# print(">>>type: ", type(record.shopping_list))
		# print(">>>print last shop:", record.shopping_list)
		target_file.close()

def update_item():
		print("Updating exiting item.")
		read_items()
		key = input("Update which item? ")
		print("Keys:", record.shopping_list.keys())
		if key in record.shopping_list.keys():
			print("Update", key)
			quanity = is_valid_quanity()
			price = is_valid_price()
			record.shopping_list[key] = [quanity, price]
		else:
			print("Unable to find", key, "in record.")


###############################################################################
# Main
###############################################################################
print("Starting shoppingBasket.py")
done_shopping = False 
shopping_list = {}
total = 0.00
record = Record(shopping_list, 0.00)

load_last_shop()
show_cmds()
while not done_shopping:
	user_cmd = input("Command? ")
	if user_cmd == 'c':
		create_item()
	elif user_cmd == 'r':
		# print(">>>type: ", type(record.shopping_list))
		# print(">>>load before r:",record.shopping_list)
		read_items()			
	elif user_cmd == 'u':
		update_item()
	elif user_cmd == 'd':
		print("Deleting exiting item.")
	elif user_cmd == 'l':
		load_last_shop()
	elif user_cmd == 's':
		save_to_file()
	elif user_cmd == 'x':
		print("Done shopping.")
		done_shopping = True
		if len(record.shopping_list) != 0:
			#print("List is not empty",shopping_list)
			read_items()
		user_cmd = input("Save current shop record? (y/n)")
		if user_cmd != 'n':
			save_to_file()
	else:
		print("Sorry, I do not understand that command.")
		show_cmds()
print("Thank you. Come again.")


# if user_cmd == "done":
	# 	break
	# else:
	# 	shopping_list.append(create_item())



