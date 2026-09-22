shopper_name = "Stella White"
apple_price = 2.00
banana_price = 4.00
kiwi_price = 1.00
steak_price = 13.00
chicken_price = 5.00

num_of_apple = 5
num_of_banana = 3
num_of_kiwi = 6
num_of_steak = 1
num_of_chicken = 2

total_apple = apple_price * num_of_apple
total_banana = banana_price * num_of_banana
total_kiwi = kiwi_price * num_of_kiwi
total_steak = steak_price * num_of_steak
total_chicken = chicken_price * num_of_chicken
total_price = total_apple + total_banana + total_kiwi + total_steak + total_chicken

total_items = num_of_apple + num_of_banana + num_of_kiwi + num_of_steak + num_of_chicken
average_price = total_items / total_items
print(f"{shopper_name.title()}: Total price: ${total_price}, average price per item: ${average_price}")