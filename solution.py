def validate_date(date: str) -> str:
    
    pass

from solution import validate_date

def validate_date(date):
    d, m, y = map(int, date.split())
    
    
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        leap_year = True
    else:
        leap_year = False
    
    
    if m < 1 or m > 12:
        return "Fecha incorrecta"
    
    
    if m in [1, 3, 5, 7, 8, 10, 12]:
        if d < 1 or d > 31:
            return "Fecha incorrecta"
    elif m in [4, 6, 9, 11]:
        if d < 1 or d > 30:
            return "Fecha incorrecta"
    elif leap_year and m == 2:
        if d < 1 or d > 29:
            return "Fecha incorrecta"
    elif not leap_year and m == 2:
        if d < 1 or d > 28:
            return "Fecha incorrecta"
    
    return "Fecha correcta"