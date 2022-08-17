import math
from termcolor import colored

print(colored("""
     A
    /\ 
 c /  \ b
  /____\ 
B   a   C
""", "cyan"))
print(colored('Please insert the value of the following sides and angles. '
              'Leave blank if they were not given. Give the angle in degree.', 'cyan'))
a = input(colored('a = ', 'blue')) or False
b = input(colored('b = ', 'blue')) or False
c = input(colored('c = ', 'blue')) or False
A = input(colored('∠A = ', 'blue')) or False
B = input(colored('∠B = ', 'blue')) or False
C = input(colored('∠C = ', 'blue')) or False

if a and b and C:
    a = float(a)
    b = float(b)
    C = float(C)
    try:
        cc = (a ** 2) + (b ** 2) - (2 * a * b * math.cos(math.radians(C)))
        c1 = math.sqrt(cc)
        cosA = ((b ** 2) + (c1 ** 2) - (a ** 2)) / (2 * b * c1)
        cosB = ((a ** 2) + (c1 ** 2) - (b ** 2)) / (2 * a * c1)
        A1 = math.degrees(math.acos(cosA))
        B1 = math.degrees(math.acos(cosB))
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c1, 2)}\n'
                      f'∠A = {round(A1, 2)}, ∠B = {round(B1, 2)}, ∠C = {round(C, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif b and c and A:
    b = float(b)
    c = float(c)
    A = float(A)
    try:
        aa = (b ** 2) + (c ** 2) - (2 * b * c * math.cos(math.radians(float(A))))
        a1 = math.sqrt(aa)
        cosB = ((float(a1) ** 2) + (float(c) ** 2) - (float(b) ** 2)) / (2 * float(a1) * float(c))
        cosC = ((float(a1) ** 2) + (float(b) ** 2) - (float(c) ** 2)) / (2 * float(a1) * float(b))
        B1 = (math.degrees(math.acos(cosB)))
        C1 = float(math.degrees(math.acos(cosC)))
        print(colored(f'\nAnswers:\na = {round(a1, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A, 2)}, ∠B = {round(B1, 2)}, ∠C = {round(C1, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif a and c and B:
    a = float(a)
    c = float(c)
    B = float(B)
    try:
        bb = (float(a) ** 2) + (float(c) ** 2) - (2 * float(a) * float(c) * math.cos(math.radians(float(B))))
        b1 = math.sqrt(bb)
        cosA = ((float(b1) ** 2) + (float(c) ** 2) - (float(a) ** 2)) / (2 * float(b1) * float(c))
        cosC = ((float(a) ** 2) + (float(b1) ** 2) - (float(c) ** 2)) / (2 * float(a) * float(b1))
        A1 = math.degrees(math.acos(cosA))
        C1 = math.degrees(math.acos(cosC))
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b1, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A1, 2)}, ∠B = {round(B, 2)}, ∠C = {round(C1, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif a and b and c:
    a = float(a)
    b = float(b)
    c = float(c)
    cosA = ((float(b) ** 2) + (float(c) ** 2) - (float(a) ** 2)) / (2 * float(b) * float(c))
    cosB = ((float(a) ** 2) + (float(c) ** 2) - (float(b) ** 2)) / (2 * float(a) * float(c))
    cosC = ((float(a) ** 2) + (float(b) ** 2) - (float(c) ** 2)) / (2 * float(a) * float(b))
    try:
        A1 = math.degrees(math.acos(cosA))
        B1 = math.degrees(math.acos(cosB))
        C1 = math.degrees(math.acos(cosC))
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A1, 2)}, ∠B = {round(B1, 2)}, ∠C = {round(C1, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif a and b and A:
    a = float(a)
    b = float(b)
    A = float(A)
    try:
        sinB = (math.sin(math.radians(float(A)))*float(b))/float(a)
        B = math.degrees(math.asin(sinB))
        C = 180 - (float(A)+float(B))
        c = (math.sin(math.radians(float(C)))*float(b))/sinB
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A, 2)}, ∠B = {round(B, 2)}, ∠C = {round(C, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif a and b and B:
    a = float(a)
    b = float(b)
    B = float(B)
    try:
        sinA = (math.sin(math.radians(float(B)))*float(a))/float(b)
        A = math.degrees(math.asin(sinA))
        C = 180 - (float(A)+float(B))
        c = (math.sin(math.radians(float(C)))*float(a))/sinA
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A, 2)}, ∠B = {round(B, 2)}, ∠C = {round(C, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif a and c and A:
    a = float(a)
    c = float(c)
    A = float(A)
    try:
        sinC = (math.sin(math.radians(float(A)))*float(c))/float(a)
        C = math.degrees(math.asin(sinC))
        B = 180 - (float(A)+float(C))
        b = (math.sin(math.radians(float(B)))*float(c))/sinC
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A, 2)}, ∠B = {round(B, 2)}, ∠C = {round(C, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif a and c and C:
    a = float(a)
    c = float(c)
    C = float(C)
    try:
        sinA = (math.sin(math.radians(float(C)))*float(a))/float(c)
        A = math.degrees(math.asin(sinA))
        B = 180 - (float(A)+float(C))
        b = (math.sin(math.radians(float(B)))*float(a))/sinA
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A, 2)}, ∠B = {round(B, 2)}, ∠C = {round(C, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif b and c and B:
    b = float(b)
    c = float(c)
    B = float(B)
    try:
        sinC = (math.sin(math.radians(float(B)))*float(c))/float(b)
        C = math.degrees(math.asin(sinC))
        A = 180 - (float(B)+float(C))
        a = (math.sin(math.radians(float(A)))*float(c))/sinC
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A, 2)}, ∠B = {round(B, 2)}, ∠C = {round(C, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif b and c and C:
    b = float(b)
    c = float(c)
    C = float(C)
    try:
        sinB = (math.sin(math.radians(float(C)))*float(b))/float(c)
        B = math.degrees(math.asin(sinB))
        A = 180 - (float(B)+float(C))
        a = (math.sin(math.radians(float(A)))*float(b))/sinB
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A, 2)}, ∠B = {round(B, 2)}, ∠C = {round(C, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif A and B and a:
    A = float(A)
    B = float(B)
    a = float(a)
    try:
        b = (math.sin(math.radians(float(B)))*float(a))/math.sin(math.radians(float(A)))
        C = 180.0 - (float(A)+float(B))
        c = (math.sin(math.radians(float(C)))*float(a))/math.sin(math.radians(float(A)))
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A, 2)}, ∠B = {round(B, 2)}, ∠C = {round(C, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif A and B and b:
    A = float(A)
    B = float(B)
    b = float(b)
    try:
        a = (math.sin(math.radians(float(A)))*float(b))/math.sin(math.radians(float(B)))
        C = 180 - (float(A)+float(B))
        c = (math.sin(math.radians(float(C)))*float(b))/math.sin(math.radians(float(B)))
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A, 2)}, ∠B = {round(B, 2)}, ∠C = {round(C, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif A and B and c:
    A = float(A)
    B = float(B)
    c = float(c)
    try:
        C = 180 - (float(A) + float(B))
        a = (math.sin(math.radians(float(A)))*float(c))/math.sin(math.radians(float(C)))
        c = (math.sin(math.radians(float(C)))*float(a))/math.sin(math.radians(float(A)))
        b = (math.sin(math.radians(float(B))) * float(c)) / math.sin(math.radians(float(C)))
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A, 2)}, ∠B = {round(B, 2)}, ∠C = {round(C, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif B and C and a:
    B = float(B)
    C = float(C)
    a = float(a)
    try:
        A = 180 - (float(B) + float(C))
        b = (math.sin(math.radians(float(B)))*float(a))/math.sin(math.radians(float(A)))
        c = (math.sin(math.radians(float(C)))*float(a))/math.sin(math.radians(float(A)))
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A, 2)}, ∠B = {round(B, 2)}, ∠C = {round(C, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif B and C and b:
    B = float(B)
    C = float(C)
    b = float(b)
    try:
        c = (math.sin(math.radians(float(C)))*float(b))/math.sin(math.radians(float(B)))
        A = 180 - (float(B)+float(C))
        a = (math.sin(math.radians(float(A)))*float(b))/math.sin(math.radians(float(B)))
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A, 2)}, ∠B = {round(B, 2)}, ∠C = {round(C, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif B and C and c:
    B = float(B)
    C = float(C)
    c = float(c)
    try:
        b = (math.sin(math.radians(float(B)))*float(c))/math.sin(math.radians(float(C)))
        A = 180 - (float(B)+float(C))
        a = (math.sin(math.radians(float(A)))*float(c))/math.sin(math.radians(float(C)))
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A, 2)}, ∠B = {round(B, 2)}, ∠C = {round(C, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif A and C and a:
    A = float(A)
    C = float(C)
    a = float(a)
    try:
        c = (math.sin(math.radians(float(C)))*float(a))/math.sin(math.radians(float(A)))
        B = 180 - (float(A)+float(C))
        b = (math.sin(math.radians(float(B)))*float(a))/math.sin(math.radians(float(A)))
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A, 2)}, ∠B = {round(B, 2)}, ∠C = {round(C, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif A and C and b:
    A = float(A)
    C = float(C)
    b = float(b)
    try:
        B = 180 - (float(A) + float(C))
        a = (math.sin(math.radians(float(A)))*float(b))/math.sin(math.radians(float(B)))
        c = (math.sin(math.radians(float(C)))*float(b))/math.sin(math.radians(float(B)))
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A, 2)}, ∠B = {round(B, 2)}, ∠C = {round(C, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))

elif A and C and c:
    A = float(A)
    C = float(C)
    c = float(c)
    try:
        a = (math.sin(math.radians(float(A)))*float(c))/math.sin(math.radians(float(C)))
        B = 180 - (float(A)+float(C))
        b = ((math.sin(math.radians(float(B)))*float(c))/math.sin(math.radians(float(C))))
        print(colored(f'\nAnswers:\na = {round(a, 2)}, b = {round(b, 2)}, c = {round(c, 2)}\n'
                      f'∠A = {round(A, 2)}, ∠B = {round(B, 2)}, ∠C = {round(C, 2)}', 'green'))
    except Exception as e:
        print(colored(f'{e}', 'red'))
