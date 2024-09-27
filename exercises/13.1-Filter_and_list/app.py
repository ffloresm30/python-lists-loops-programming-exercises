all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

def filter_function(name):
    # Update here
    return name[0].lower() == "r"
    
resulting_names = list(filter(filter_function, all_names))

print(resulting_names)

