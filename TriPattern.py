"""Create lower triangular, upper triangular 
and pyramid containing the "*" character."""

# 1.Lower Triangle
def lower_triangular(n):
    for i in range(1, n + 1):
        print("* " * i)

lower_triangular(5)


# 2.Upper Triangle
def upper_triangular(n):
    for i in range(n, 0, -1):
        print("* " * i)

upper_triangular(5)

# 3.Pyramid
def pyramid(n):
    for i in range(1, n+1):
        print(" " * (n - i) + "* " * (i))

pyramid(5)