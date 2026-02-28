# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:]

category1 = categories[0:11]
category2 = categories[13:]

bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

print(candy1) 
print(candy2) 
print(dry_goods) 
print(category1) 
print(category2) 
print(bubblegum_price) 
print(chocolate_price) 
print(pasta_price) 

message_1 = ( "We have " + candy1 + " for " + bubblegum_price + " in the " + category1)
message_2 = ( "We have " + candy2 + " for " + chocolate_price + " in the " + category1)
message_3 = ( "We have " + dry_goods + " for " + pasta_price + " in the " + category2)

print(message_1)       
print(message_2)
print(message_3)
