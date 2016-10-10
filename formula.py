def f_to_c(f):
    """returns Farenheit temperature in Celcius

    >>> f_to_c(85)
    29.444444444444443

    >>> f_to_c(-20)
    -28.88888888888889

    >>> f_to_c(85)
    -17.77777777777778
    
    """
    return(f-32)*5/9.0

print(f_to_c)

def c_to_f(c):
    """returns Celcius temperature in Farenheit

    >>> c_to_f(0)
    32.0
    
    >>> c_to_f(1.5)
    34.7

    >>> c_to_f(32)
    89.6
    
    """
    return (c*9.0/5)+32

print c_to_f

