'''
Name: Jayden Ly
Started: 2/1/24
Last Edited: 2/8/24 11:49 AM
'''
def right_arrow():
    base_char = input()
    head_char = input()

    row1 = '      ' + head_char
    row2 = base_char*6 + head_char*2
    row3 = base_char*6 + head_char*3

    print(row1)
    print(row2)
    print(row3)
    print(row2)
    print(row1)

if __name__ == "__main__":
    right_arrow()