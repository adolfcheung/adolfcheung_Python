#a3_q2_t3

def number_to_digitLis_reversed_order(num):
   digits = []
   while num != 0:
       digits.append(num % 10)
       num //= 10
   return digits


def numbers_to_digitLis_original_order(num):
   reversed_digits = number_to_digitLis_reversed_order(num)
   n = len(reversed_digits)
   original_digits = []
   for i in range(0, n):
      original_digits.append(reversed_digits[n-i-1])
   return original_digits


def is_lucky_number(num):
    digits = numbers_to_digitLis_original_order(num)

    num_str = str(num)    #Convert num into a string so that it is ordered.
    count = j = 0
    k=len(num_str)

    #Count digit 0 to 9 one by one
    #Count digit 0
    for b in num_str:
        if b == "0":
            count +=1
    x = 0
    y = count
    if count<=k and count != 0:    #Count cannot be 0 because the least frequency does not include zero.
        j = 0    #This can find the digit with least frequency
        k = count    #This can find the frequency of the digit
    count = 0    #Reset count to 0

    #Count digit 1
    for b in num_str:
        if b == "1":
            count +=1
    if count>=y:
        x = 1    #This can find the digit with most frequency
        y =count    #This can find the frequency of the digit
    if count<=k and count != 0:
        j = 1
        k = count
    count = 0

    #Count digit 2
    for b in num_str:
        if b =="2":
            count +=1
    if count>=y:
        x = 2
        y =count
    if count<=k and count != 0:
        j = 2
        k = count
    count = 0

    #Count digit 3
    for b in num_str:
        if b =="3":
            count +=1
    if count>=y:
        x = 3
        y =count
    if count<=k and count != 0:
        j = 3
        k = count
    count = 0

    #Count digit 4
    for b in num_str:
        if b =="4":
            count +=1
    if count>=y:
        x = 4
        y =count
    if count<=k and count != 0:
        j = 4
        k = count
    count = 0

    #Count digit 5
    for b in num_str:
        if b =="5":
            count +=1
    if count>=y:
        x = 5
        y =count
    if count<=k and count != 0:
        j = 5
        k = count
    count = 0

    #Count digit 6
    for b in num_str:
        if b =="6":
            count +=1
    if count>=y:
        x = 6
        y =count
    if count<=k and count != 0:
        j = 6
        k = count
    count = 0

    #Count digit 7
    for b in num_str:
        if b =="7":
            count +=1
    if count>=y:
        x = 7
        y =count
    if count<=k and count != 0:
        j = 7
        k = count
    count = 0

    #Count digit 8
    for b in num_str:
        if b =="8":
            count +=1
    if count>=y:
        x = 8
        y =count
    if count<=k and count != 0:
        j = 8
        k = count
    count = 0

    #Count digit 9
    for b in num_str:
        if b =="9":
            count +=1
    if count>=y:
        x = 9
        y = count
    if count<=k and count != 0:
        j = 9
        k = count

    lucky_number=abs(x*y-j*k)

    if lucky_number%10 == 6:
        return True
    else:
        return False

def count_jumping_scheme(num):
    list_1 = [1, 3, 5]
    
    if num == 2:
        return 1
    
    elif num == 3:
        return 3

    elif num == 4:
        return 5
    
    else:
        for a in range(5, num+1):
            b = list_1[a-4] + list_1[a-3]
            list_1.append(b)
        return list_1[len(list_1)-1]

number = int(input())
num_of_schemes = count_jumping_scheme(number)
if is_lucky_number(num_of_schemes):
    print("Yes")
else:
    print("No")
