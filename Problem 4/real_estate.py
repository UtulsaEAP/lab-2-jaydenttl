
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    
    difference = int(current_price-last_month_price)
    mortgage = float((current_price * 0.051) / 12)

    print('This house is $' + str(current_price) + '. The change is $' + str(difference) + ' since last month.')
    print('The estimated monthly mortgage is $' + (f'{mortgage:.2f}') + '.')
if __name__ == "__main__":
    real_estate()