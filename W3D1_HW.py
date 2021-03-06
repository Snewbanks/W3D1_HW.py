places = [' ', 'Argentina', '  ', 'San Diego',
          '', '   ', '', 'Boston', 'New York']
new_places = list(filter(str.strip, places))
print(new_places)

authors = ["Connor Milliken", "Victor aNisimov",
           "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]
sortlist = sorted(sorted(authors), key=lambda n: n.split()[1])
print(sortlist)


places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]
temp = list(map(lambda t: f"{t[0]} {(9/5)*t[1] + 32}", places))
print(temp)


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def num_of_iters(num):
    for i in range(num):
        print(f'{i+1}: {fib(i)}')


num_of_iters(10)
