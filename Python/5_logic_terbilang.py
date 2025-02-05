def terbilang_pecahan_uang(number, sep=''):
    """
    This Python function converts a numerical amount into an Indonesian text representation for
    currency.
    
    :param number: The function `terbilang_pecahan_uang` is designed to convert a numerical value into
    an Indonesian text representation. It breaks down the number into groups of three digits and
    converts each group into words
    :param sep: The `sep` parameter in the `terbilang_pecahan_uang` function is used as a separator to
    split the input number. The function will split the input number based on the provided separator
    (either a comma or a period) to process it accordingly
    :return: The function `terbilang_pecahan_uang` returns the Indonesian word representation of a given
    number in currency format, with the specified separator.
    """
    
    separator = ['.',',']
    if sep not in separator:
        return "Harap gunakan koma atau titik sebagai pemisah"

    # The `number_str` list is used to store the Indonesian words for numbers from 0 to 10. 
    number_str = [
            '', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh',
            'delapan', 'sembilan', 'sepuluh'
        ]
    
    # Used to store the Indonesian words that represent the numerical suffixes for different positions in a number
    number_suffixes = [
            'belas', 
            'puluh', 
            'ratus', 
            'ribu', 
            'juta', 
            'miliar',
            'triliun'
        ]
    
    # Splitting the input numerical based on separator
    num = number.split(sep)
    length_num = len(num)

    # create empty list to store the Indonesian word representations of the
    # numerical amount after processing each group of digits in the input number.
    terbilang = []

    # This part of the code is responsible for converting each group of digits in the input number
    # into their Indonesian text representation. Here's a breakdown of what the code snippet does:
    for x in num:
        length_group = len(x)
        for y in x:
            if int(y):
                # Add the Indonesian words for numbers and add suffixes ratus
                if length_group == 3:
                    terbilang.append(number_str[int(y)])
                    terbilang.append(number_suffixes[2])
                # Add suffixes belas
                elif length_group == 2 and int(y) == 1:
                    terbilang.append(number_suffixes[0])
                # Add the Indonesian words for numbers and add suffixes puluh
                elif length_group == 2 and int(y) != 1:
                    terbilang.append(number_str[int(y)])
                    terbilang.append(number_suffixes[1])
                else:
                # Add the Indonesian words for numbers
                    terbilang.append(number_str[int(y)])
            length_group -= 1

        # Add suffixes Triliun
        if length_num == 5:
            terbilang.append(number_suffixes[6])
        # Add suffixes Miliar
        elif length_num == 4:
            terbilang.append(number_suffixes[5])
        # Add suffixes Juta
        elif length_num == 3:
            terbilang.append(number_suffixes[4])
        # Add suffixes Ribu
        elif length_num == 2:
            terbilang.append(number_suffixes[3])
        length_num -= 1

    # fix index belas
    new_list = [i for i, x in enumerate(terbilang) if x == "belas"]
    for indeks in sorted(new_list, reverse=True):
        kata_belas = terbilang.pop(indeks)
        terbilang.insert(indeks + 1, kata_belas)

    # convert array into string
    terbilang_str = " ".join(terbilang)

    # fix bilangan satu ratus -> seratus, satu belas -> sebelas
    terbilang_str_fix = terbilang_str.replace("satu ratus", "seratus")
    terbilang_str_fix = terbilang_str_fix.replace("satu belas", "sebelas")
    return terbilang_str_fix

pecahan_uang = '2.311.000'
pecahan_uang_2 = '123.456.789'
print(f"Rp {pecahan_uang} \nTerbilang: {terbilang_pecahan_uang(pecahan_uang, ".")}")
print(f"Rp {pecahan_uang_2} \nTerbilang: {terbilang_pecahan_uang(pecahan_uang_2, ".")}")

def terbilang_angka(number):
    """
    The function `terbilang_angka` converts a given number into its Indonesian word representation.
    
    :param number: The `number` parameter in the `terbilang_angka` function is expected to be a string
    representing a number. The function converts this number into its Indonesian word representation
    :return: The function `terbilang_angka` takes a number as input and converts it into its Indonesian
    word representation. The function returns a string that represents the input number in Indonesian
    words.
    """
    number_str = [
            'nol', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh',
            'delapan', 'sembilan'
        ]
    
    terbilang = []
    for x in number:
        terbilang.append(number_str[int(x)])

    return " ".join(terbilang)


angka = '10234567890'
print(f"Angka {angka} \nTerbilang: {terbilang_angka(angka)}")