
def simple_stats():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    
    prod = float(num1 * num2 * num3 * num4)
    avg = float((num1 + num2 + num3 + num4)/4)

    #fprod = float(num1 * num2 * num3 * num4)
    #favg = float((num1 * num2 * num3 * num4)/4)

    print(f'{prod:.0f}' , f'{avg:.0f}')
    print(f'{prod:.3f}' , f'{avg:.3f}')

    #print( int prod int avg)
    #print( float prod float avg)
if __name__ == "__main__":
    simple_stats()