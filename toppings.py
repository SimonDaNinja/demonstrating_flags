from enum import Flag, auto

class Topping(Flag):
    LETTUCE             = auto()
    FRESH_TOMATOES      = auto()
    CUCUMBER            = auto()
    ONION               = auto()
    FRIGGITELLO         = auto()
    SAUCE               = auto()
    TOMATO_SAUCE        = auto()
    CHEESE              = auto()
    KEBAB_MEAT          = auto()
    FRIES               = auto()
    WHITE_CHEESE        = auto()
    HAM                 = auto()
    PINEAPPLE           = auto()
    CHAMPIGNONS         = auto()
    BELL_PEPPER         = auto()
    OLIVES              = auto()
    GREEK_OLIVES        = auto()
    ARTICHOKES          = auto()
    MOZARELLA           = auto()
    SUN_DRIED_TOMATOES  = auto()
    GORGONZOLA          = auto()
    ARUGULA             = auto()
    PESTO               = auto()
    BANANA              = auto()
    NUTS                = auto()
    CURRY               = auto()
    CHICKEN             = auto()
    GROUND_MEAT         = auto()
    PIRI_PIRI           = auto()
    GARLIC              = auto()
    BACON               = auto()
    EGGS                = auto()
    JALAPENOS           = auto()
    SALAMI              = auto()
    GARLIC_SAUCE        = auto()
    BEEF_TENDERLOIN     = auto()
    BEARNAISE_SAUCE     = auto()
    TACO_SAUCE          = auto()
    SPICY_SAUSAGE       = auto()
    ITALIAN_DI_PARMA    = auto()
    SHRIMP              = auto()
    TUNA                = auto()
    MUSSELS             = auto()
    CRAYFISH_TAILS      = auto()

meat = Topping.KEBAB_MEAT |\
       Topping.HAM |\
       Topping.CHICKEN |\
       Topping.GROUND_MEAT |\
       Topping.BACON |\
       Topping.SALAMI |\
       Topping.BEEF_TENDERLOIN |\
       Topping.SPICY_SAUSAGE |\
       Topping.ITALIAN_DI_PARMA

seafood = Topping.SHRIMP |\
          Topping.TUNA |\
          Topping.MUSSELS |\
          Topping.CRAYFISH_TAILS

dairy = Topping.CHEESE |\
        Topping.WHITE_CHEESE |\
        Topping.MOZARELLA |\
        Topping.GORGONZOLA

topping_to_str = {
    Topping.LETTUCE             : "isbergssallad",
    Topping.FRESH_TOMATOES      : "tomater",
    Topping.CUCUMBER            : "gurka",
    Topping.ONION               : "l??k",
    Topping.FRIGGITELLO         : "peperoni",
    Topping.SAUCE               : "s??s",
    Topping.TOMATO_SAUCE        : "tomats??s",
    Topping.CHEESE              : "ost",
    Topping.KEBAB_MEAT          : "kebabk??tt",
    Topping.FRIES               : "pommes",
    Topping.WHITE_CHEESE        : "vitost",
    Topping.HAM                 : "skinka",
    Topping.PINEAPPLE           : "ananas",
    Topping.CHAMPIGNONS         : "champinjoner",
    Topping.BELL_PEPPER         : "paprika",
    Topping.OLIVES              : "oliver",
    Topping.GREEK_OLIVES        : "grekiska oliver",
    Topping.ARTICHOKES          : "kron??rtskockor",
    Topping.MOZARELLA           : "mozarella",
    Topping.SUN_DRIED_TOMATOES  : "soltorkade tomater",
    Topping.GORGONZOLA          : "gorgonzola",
    Topping.ARUGULA             : "ruccola",
    Topping.PESTO               : "pesto",
    Topping.BANANA              : "banan",
    Topping.NUTS                : "n??tter",
    Topping.CURRY               : "curry",
    Topping.CHICKEN             : "kyckling",
    Topping.GROUND_MEAT         : "k??ttf??rs",
    Topping.PIRI_PIRI           : "piri piri",
    Topping.GARLIC              : "vitl??k",
    Topping.BACON               : "bacon",
    Topping.EGGS                : "??gg",
    Topping.JALAPENOS           : "jalape??os",
    Topping.SALAMI              : "salami",
    Topping.GARLIC_SAUCE        : "vitl??kss??s",
    Topping.BEEF_TENDERLOIN     : "oxfil??",
    Topping.BEARNAISE_SAUCE     : "bearnaises??s",
    Topping.TACO_SAUCE          : "tacos??s",
    Topping.SPICY_SAUSAGE       : "stark korv",
    Topping.ITALIAN_DI_PARMA    : "italiensk di parma",
    Topping.SHRIMP              : "r??kor",
    Topping.TUNA                : "tonfisk",
    Topping.MUSSELS             : "musslor",
    Topping.CRAYFISH_TAILS      : "kr??ftstj??rtar"
}

assert(len(Topping) == len(topping_to_str)), "Number of elements in topping_to_str does not match the number of toppings"

def pizza_to_str(pizza):
    topping_strings = [string for topping, string in topping_to_str.items() if pizza & topping]
    if len(topping_strings) > 1:
        return ", ".join(topping_strings[:-1]) + " och " + topping_strings[-1]
    return topping_strings[0] if topping_strings else ""

def print_pizza_dict(pizza_dict):
    for pizza_name, pizza in pizza_dict.items():
        print(f"{pizza_name}:\n{pizza_to_str(pizza)}\n")

