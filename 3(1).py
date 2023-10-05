#Розв’язання нелінійного рівняння методом Ньютона: 
def f(x):
    return 3*x**4 + 4*x**3 - 12*x**2 - 5

def df(x):
    return 12*x**3 + 12*x**2 - 24*x

def newton_method(initial_guess, tolerance):
    x = initial_guess
    while abs(f(x)) >= tolerance:
        x = x - f(x) / df(x)
    return x

initial_guess = -2.0  

tolerance = 0.0001

roots = []
while True:
    try:
        root = newton_method(initial_guess, tolerance)
        roots.append(root)
        
        initial_guess = root + 0.5  
    except:
        break

print("Знайдені корені:")
for i, root in enumerate(roots, start=1):
    print(f"Корінь {i}: {root:.4f}")
