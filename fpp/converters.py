weight_1 = int(input("What's your weight? "))

def lbs_to_kgs(weight):
    new_weight = weight * 0.45
    print(f"Your weight in kgs is {new_weight}")

def kgs_to_lbs(weight):
    return weight / 0.45


def talk(message):
    print(message)

lbs_to_kgs(weight_1)