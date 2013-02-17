the_numbers_of_fibonnaci = [1, 1]

for i in range(0, 20):
    try:
        print the_numbers_of_fibonnaci[i]
    except IndexError:
        the_result = the_numbers_of_fibonnaci[0] + the_numbers_of_fibonnaci[1]
        the_numbers_of_fibonnaci = the_numbers_of_fibonnaci[:1] + [the_result]
        print the_result
