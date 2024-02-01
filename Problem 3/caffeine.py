
def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''

    six_hours = float(caffeine_mg / 2)
    twelve_hours = float(six_hours / 2)
    twentyfour_hours = float(twelve_hours / 4)

    print (str('After 6 hours: '+f'{six_hours:.2f}'+' mg'))
    print (str('After 12 hours: '+f'{twelve_hours:.2f}'+' mg'))
    print (str('After 24 hours: '+f'{twentyfour_hours:.2f}'+' mg'))
if __name__ == "__main__":
    caffeine()