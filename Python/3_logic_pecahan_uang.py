# Logic Function Pecahan Uang with manual convert 
def pecahan_uang(number:int, lang='id') :
    # validate number is int
    try:
        number = int(number)
    except:
        if not isinstance(number, int):
            return "tolong masukkan angka" 
    
    # convert number into string, for reserve the string
    str_number = str(number)
    # reserve number for grouping 3 digit from backward
    reserve_number = str_number[::-1]
    # slice string 3 digit from backward
    digit_group = [reserve_number[i:i+3] for i in range(0,len(reserve_number),3)]
    # join the string and reserve again
    if lang == 'id':
        return ".".join(digit_group[::-1])
    elif lang == 'en':
        return ",".join(digit_group[::-1])
    
# Logic Pecahan Uang with formatted string 
def pecahan_uang_2(number:int, lang='id'):
    # validate number is int
    try:
        number = int(number)
    except:
        if not isinstance(number, int):
            return "tolong masukkan angka" 
    
    formatted_number = "{:,}".format(number)
    if lang == 'id':
        return formatted_number.replace(',', '.')
    elif lang == 'en':
        return formatted_number

print(pecahan_uang(1999000))
print(pecahan_uang(2999000, 'en'))
print(pecahan_uang('seratusribu'))

print(pecahan_uang_2(3999999000))
print(pecahan_uang_2(299999000, 'en'))
print(pecahan_uang_2('seratusribu'))