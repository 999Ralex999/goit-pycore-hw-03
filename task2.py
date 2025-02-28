import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or max <= min or quantity > (max - min + 1):
        return []
    
    return sorted(random.sample(range(min, max + 1), quantity))

print(get_numbers_ticket(0, 100, 5))
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(10, 20, 5)) 