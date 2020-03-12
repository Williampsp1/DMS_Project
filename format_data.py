#!/usr/bin/env python3
import random

names_file = open('./data/names.txt', 'r')
f_name = []
l_name = []

address_file = open('./data/addresses.txt', 'r')
address = []
cities = []
zipcodes = []

# Create customer data -----

# add names
for line in names_file:
    temp = line.strip('\n').split(' ')
    f_name.append(temp[0])
    l_name.append(temp[1])

for line in address_file:
    if line[0].isdigit():
        address.append(line.strip('\n'))
    else:
        cities.append(line.strip('\n').split(' ')[-2])
        zipcodes.append(line.strip('\n').split(' ')[-1])

# write names
names_out = open('./data/cust_out.tsv', 'w')
counter = 0
for x in f_name:
    names_out.write(str(counter + 1) + '\t' +\
            x + '\t' +  l_name[counter]+ '\t' + address[counter] + '\t' + \
            cities[counter] + '\t' + zipcodes[counter] + '\n')
    counter += 1
names_out.close()

online_id = 200
oo_out = open('./data/online_order.tsv', 'w')
# Online order -----
for x in f_name:
    oo_out.write(str(online_id) + '\t'  +str(round(random.uniform(1,200), 2)) + '\n')
    online_id += 1

oo_out.close()


# Games ----
game_id = 3500
g_out = open('./data/game_out.tsv', 'w')
g_titles = open('./data/game_titles.txt', 'r')
g_lis = []

genres = ['horror', 'arcade', 'first-person shooter', 'RPG', 'action', 'adventure', \
        'platformer', 'mmo']
for line in g_titles:
    g_lis.append(line.strip('\n'))

for x in g_lis:
    ran = random.randint(0,7)
    g_out.write(str(game_id) + '\t' + x + '\t' + str(round(random.uniform(1,60), 2)) + \
            '\t' + genres[ran]+ '\n') 
    game_id +=1

g_out.close()

# Locales  ----
locale_id = 240
locale_out = open('./data/locale_out.tsv', 'w')
locales = open('./data/locales.txt', 'r')

for line in locales:
    temp_a = line.split(',')[0]
    temp_c = line.split(',')[1].strip(' ')
    temp_z = line.split(' ')[-1].strip('\n')
    locale_out.write(str(locale_id) + '\t' + temp_c + '\t' + temp_a + '\t' + temp_z + '\n' )
    locale_id += 1
locale_out.close()

# employee ----
e_id = 6000
f_name_e = []
l_name_e = []
e_names = open('./data/e_names.txt', 'r')
e_names = open('./data/e_names.txt', 'r')
e_out = open ('./data/employee_out.tsv', 'w')
for line in e_names:
    temp = line.strip('\n').split(' ')
    f_name_e.append(temp[0])
    l_name_e.append(temp[0])

counter = 0
for line in e_names:
    e_out.write(str(e_id) + '\t' + str(round(random.uniform(30000,50000), 2)) + \
            '\t' + f_name_e[counter] + '\t' + l_name_e[counter] + '\n')
    e_id +=1
    counter +=1

e_out.close()

# manager ------
spec = ['retro games', 'fighting games', 'used games', 'new games', 'PC games', \
        'console games', 'horror games', 'hand-held consoles']
man_out = open('./data/manager_out.tsv', 'w')
e_id = 6000
for i in range(0,50):
    ran = random.randint(0,7)
    man_out.write(spec[ran] + '\t' + str(e_id) + '\n')
    e_id += 1
print(e_id)

# cashier -------
register_id = 8888
cash_out = open('./data/cashier_out.tsv', 'w')
for i in range(50,100):
    cash_out.write(str(register_id) + '\t' + str(e_id) + '\n')
    e_id +=1
cash_out.close()

# Relationships
# Places -------

online_id = 200
counter = 0
places_out = open('./data/places_out.tsv', 'w')
dates = ['2020-02-26', '2020-01-18', '2020-03-6', '2020-03-7', '2020-03-8', '2020-04-25',
        '2020-10-26', '2020-11-26', '2020-12-20']
for i in range(1,101):
    ran = random.randint(0,8)
    places_out.write(str(online_id) + '\t' + str(i) + '\t' + dates[ran] + '\n')
    online_id +=1
places_out.close()


# Purchases

purchases_out = open('./data/purchases_out.tsv', 'w')
dates = ['2020-02-26', '2020-01-18', '2020-03-6', '2020-03-7', '2020-03-8', '2020-04-25',
        '2020-10-26', '2020-11-26', '2020-12-20']

locale_ids = [240, 241, 242, 243, 244, 245]
game_id = 3500
for i in range(1,101):
    ran = random.randint(0,8)
    ran2 = random.randint(0,5)
    purchases_out.write(str(i) + '\t' + str(game_id) + '\t' + dates[ran] + '\t' +\
            str(locale_ids[ran2]) + '\n')
    game_id +=1
purchases_out.close()


# has items ---
online_id = 200
game_id = 3500

has_items = open('./data/has_items.tsv', 'w')
for i in range(1, 101):
    has_items.write(str(online_id) + '\t' + str(game_id) + '\n')
    game_id += 1
    online_id += 1
has_items.close()


# holds items ----
game_id = 3500
locale_ids = [240, 241, 242, 243, 244, 245]
holds_items = open('./data/holds_items.tsv', 'w')

for i in range(1,101):
    ran = random.randint(0,5)
    ran2 = random.randint(1,50)
    holds_items.write(str(locale_ids[ran]) + '\t' + str(game_id) + '\t' + str(ran2) + '\n')
    game_id +=1
holds_items.close()

# works at ---
e_id = 6000
locale_ids = [240, 241, 242, 243, 244, 245]
works_at = open('./data/works_at.tsv', 'w')
for i in range(1,101):
    ran = random.randint(0,5)
    works_at.write(str(e_id) + '\t' + str(locale_ids[ran]) + '\n')
    e_id += 1
works_at.close()

# sale -----
# entered manually
