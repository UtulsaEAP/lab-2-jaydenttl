def telephone():
    phone_number = int(input())

    area_code = (phone_number // 10000000)
    first_three = ((phone_number // 10000) %1000)
    last_four = (phone_number %10000)


    print (('('+str(area_code)+') '+ str(first_three)+'-'+str(last_four)))

   # print (str(area_code))
if __name__ == "__main__":
    telephone()