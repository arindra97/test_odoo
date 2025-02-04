# Create function find Bilangan Prima return true | false
def logic_bilangan_prima(number):
    """
    This Python function checks if a given number is a prime number or not.
    
    :param number: The function `logic_bilangan_prima` checks if a given number is a prime number. It
    follows the logic below:
    :return: The function `logic_bilangan_prima` returns a boolean value - `True` if the input number is
    a prime number, and `False` if it is not a prime number.
    """
    # check if number less than 1 return false ['bukan bilangan prima']
    if number <= 1:
        return False
    # check if number is 2 return true ['bilangan prima']
    if number == 2:
        return True
    # check if number modulus 2 is zero (even number) return false ['bukan bilangan prima']
    if number % 2 == 0:
        return False
    # looping number for checking bilangan prima
    for i in range(3, number , 2):
        # check if number modulus looping number is zero (it means the number can divide) return false ['bukan bilangan prima']
        if number % i == 0:    
            return False
    # if number cannot divide with number in looping return true ['bilangan prima']
    return True

# Apps / implementation
# check 1 number
print(logic_bilangan_prima(2))
print(logic_bilangan_prima(4))
print(logic_bilangan_prima(5))
print(logic_bilangan_prima(23))
print("==============")

# check prime number between 1-20 with detail
n = 20
for i in range (1, n+1):
    result = "Bilangan Prima" if logic_bilangan_prima(i) else "Bukan Bilangan Prima"
    print('bilangan %d' %i + ' adalah %s' %result)

print("==============")
# check summary prime number between 1-20
bil_prima = []
for i in range (1, n):
    if logic_bilangan_prima(i):
        bil_prima.append(i) 

print('Bilangan Prima', bil_prima)