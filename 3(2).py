#Розв’язання нелінійного рівняння комбінованим методом
def f(x):
    return 3*x**4 + 4*x**3 - 12*x**2 - 5

def df(x):
    return 12*x**3 + 12*x**2 - 24*x

def bisection_method(a, b, tolerance):
    while (b - a) / 2 > tolerance:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2

def newton_method(x0, tolerance, max_iterations):
    x = x0
    for i in range(max_iterations):
        if abs(f(x)) < tolerance:
            return x
        x = x - f(x) / df(x)
    raise Exception("Не вдалося знайти розв'язок з заданою точністю та кількістю ітерацій")

intervals = [(-2, -1), (0, 1)]

bisection_tolerance = 0.0001

max_iterations = 100

roots = []

for interval in intervals:
    a, b = interval
    initial_guess = (a + b) / 2 
    bisection_result = bisection_method(a, b, bisection_tolerance)
    newton_result = newton_method(bisection_result, bisection_tolerance, max_iterations)
    roots.append(newton_result)

print("Знайдені корені:")
for i, root in enumerate(roots, start=1):
    print(f"Корінь {i}: {root:.4f}")
