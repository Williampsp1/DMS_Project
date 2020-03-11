#!/usr/bin/env python3

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
names_out = open('./data/names_out.tsv', 'w')
counter = 0
for x in f_name:
    names_out.write(str(counter + 1) + '\t' +\
            x + '\t' +  l_name[counter]+ '\t' + address[counter] + '\t' + \
            cities[counter] + '\t' + zipcodes[counter] + '\n')
    counter += 1
names_out.close()        
