
dwarfs = ["Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"]

def roll_call_dwarves(dwarfs):
   for i in range(len(dwarfs)):
       print(f"{i + 1}. {dwarfs[i]}")
   
def summon_captain_planet(calls):
    """Capitalizes each element and adds an exclamation point."""
    result_list = [scream.capitalize() + '!' for scream in calls]
    return result_list

# Example usage:
result_list = summon_captain_planet(calls=["earth", "wind", "fire", "water", "heart"])
print(result_list)


def long_planeteer_calls(words):
    for word in words:
        if len(word) > 4:
            return True
    return False

    
soups = ["tomato soup", "cheddar", "oyster crackers", "gouda"]

def find_the_cheese(snacks):
    cheese=["cheddar","gouda","camembert"]
    for i in snacks:
        if i in cheese:
            return i

print(find_the_cheese(snacks=["crackers", "gouda", "thyme"]))

