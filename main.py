import toppings
from toppings import Topping
from toppings import print_pizza_dict
from guldheds_pizzeria_menu import guldheds_pizzeria_menu
from enum import Flag, auto

class DemonstrationOptions(Flag):
    WHOLE_MENU = auto()
    VEGETARIAN = auto()
    SEA_FOOD = auto()
    MEAT = auto()
    PESCETARIAN = auto()

ALL_OPTIONS = ~DemonstrationOptions(0)

options = DemonstrationOptions(0)

"""
uncomment those options you want to demonstrate

note: if you want to print everything, you can also just uncomment ALL_OPTIONS
"""

#options |= DemonstrationOptions.WHOLE_MENU
#options |= DemonstrationOptions.VEGETARIAN
#options |= DemonstrationOptions.SEA_FOOD
#options |= DemonstrationOptions.MEAT
#options |= DemonstrationOptions.PESCETARIAN
options |= ALL_OPTIONS

if __name__ == "__main__":
    if options & DemonstrationOptions.WHOLE_MENU:
        print("printar hela pizzamenyn:\n")
        print_pizza_dict(guldheds_pizzeria_menu)
        print("-------")
    if options & DemonstrationOptions.VEGETARIAN:
        print("printa alla vegetariska alternativ:\n")
        non_vegetarian = toppings.meat | toppings.seafood
        vegetarian_options = {name:pizza for name, pizza in guldheds_pizzeria_menu.items() if not pizza & non_vegetarian}
        print_pizza_dict(vegetarian_options)
        print("-------")
    if options & DemonstrationOptions.SEA_FOOD:
        print("printa alla fisk-och skaldjursalternativ:\n")
        seafood_options = {name:pizza for name, pizza in guldheds_pizzeria_menu.items() if pizza & toppings.seafood}
        print_pizza_dict(seafood_options)
        print("-------")
    if options & DemonstrationOptions.MEAT:
        print("printa alla köttalternativ:\n")
        meat_options = {name:pizza for name, pizza in guldheds_pizzeria_menu.items() if pizza & toppings.meat}
        print_pizza_dict(meat_options)
        print("-------")
    if options & DemonstrationOptions.PESCETARIAN:
        print("printa alla pescetarianska alternativ:\n")
        pescetarian_options = {name:pizza for name, pizza in guldheds_pizzeria_menu.items() if not pizza & toppings.meat}
        print_pizza_dict(pescetarian_options)
        print("-------")
