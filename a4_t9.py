print("Table file:")

# user inpts file name
file_name = input()

# return how many tables defined in a file.
dict_2 = {}
with open(file_name) as file_Obj:
    obj_list = file_Obj.readlines()

with open(file_name) as file_Obj:     # handle the third exceptional case
    for line in file_Obj:
        x  = line.rstrip()
        x = x.split(" ")
        dict_2[x[0]] = int(x[1])

print(f'Imported {len(obj_list)} table(s).')

dict_1 = {}    # create an empty dictionry to record the booking information
count = 1 # define count
count_2  = 0
avoid_duplicate_record = 0

r = False
while True:
    a= input()    # user continously enters commands.

    # book – request a booking
    if "Book|" in a:
        c = a.split("|")    # splits a string into a list where separator is "|"
        c.append("Pending")
        c[0] = avoid_duplicate_record
        avoid_duplicate_record += 1
        c = tuple(c)    # convert the list into a tuple such that the keys in the dictionary are iterable
        for d in dict_1.keys():
            if c[3] in d:
                count += 1
        print(f'Added booking. The ticket code for {c[3]} is {count}.')
        if count == 1:    # If this is the first booking of a particular day, this booking will be stored in dict_1 where the value will be 1.
            dict_1[c]=1
        elif count >= 2:    # If this is not the first booking of a particular day, this booking will be stored in dict_1 where the value will be count.
            dict_1[c]=count
            count = 1    # reset count to 1
        
    # Exit - termininate the program
    if a == "Exit":
        print("Bye")
        break    

    # ListBookings
    if "ListBookings" in a:
        if dict_1 == {}:    #If there is no booking in the system
            print("No booking.")
        else:
            print("Booking(s):")
            for e, f in dict_1.items():
                if "Pending" in e:
                     print(f'{e[1]}, {e[2]}, {e[3]} (Ticket {f}), {e[4]}, {e[5]}.')
                else:
                   print(f'{e[1]}, {e[2]}, {e[3]} (Ticket {f}), {e[4]}, Assigned table(s): {e[5]}.') 

    # AllocateTable
    if "AllocateTable" in a:
        c = a.split("|")
        i = c[3].split(" ")
        n = False
        
        for g in dict_1.keys():     # handle the second exceptional case
            for m in i:
                if g[5] in m and g[3] == c[1]:
                    print("Error: One or more tables allocated to another booking.")
                    n = True

        if n == False:            
            for g, h in dict_1.items():    # locate the booking to be allocated table(s) to
                if int(c[2]) == h and c[1] == g[3]:    # the ticket code and date must be idtentical to the booking record

                    for o in i:    # handle the third exceptional case
                        p = dict_2[o]
                        count_2 += p    # count_2 is the number of seats the allocated tables provide
                    if count_2 < int(g[4]):
                        print("Error: Not enough seats for this booking.")

                    elif g[5] != "Pending":    # handle the first exceptional case
                        print("Error: Table(s) already allocated to this booking.")

                    else:
                        i = c[3].split(" ")    # split the string so that table numbers can be sorted.
                        i.sort()    # sort the table numbers
                        i = str(i)
                        i = i.replace("[", "")    # remove "["
                        i = i.replace("]", "")    # remove "]"
                        i = i.replace("'", "")    # remove "'"
                        j = g    # copy g
                        j = list(j)    #convert j into a list such that j can support item assignment
                        j[5] = i
                        j = tuple(j)    #convert j into a tuple as tuple is hashable
                        dict_1 = {j if k == g else k:l for k,l in dict_1.items()}    # update the booking where the new booking is accompanied by assigned tables while the ordering is preserved
                        print(f'Allocated table(s). {g[3]} (Ticket {h}): {i}.')
                        break

        count_2 = 0
        
    if "ListTableAllocation" in a:
        c = a.split("|")
        print(f'Table(s) on {c[1]}:')
        
        for q in dict_2.keys():
            r  = False
            for g, h in dict_1.items():    # locate the bookings on a particular dinning date
                if c[1] == g[3] and q in g[5]:    # match the dinning date
                    print(f'{q}: Ticket {h}')    # print the ticket code if that table is booked
                    r = True
            if r != True:
                print(f'{q}: Available')    # print "Available" if that book is not yet booked
