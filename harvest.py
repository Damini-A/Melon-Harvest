############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = [] #creates empty list of all melon types

    musk = MelonType('musk', 1998, "green", True, True, "Muskmelon")
    musk.add_pairing("mint") # musk.pairing
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, "orange", True, False, "Casaba")
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, "green", True, False, "Crenshaw")
    cren.add_pairing("proscuitto")
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, "yellow", True, True, "Yellow Watermelon")
    yw.add_pairing("ice-cream")
    all_melon_types.append(yw)

    return all_melon_types #returns a list
    # all_melon_types = [musk, cas, cren, yw]

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # for the number of items in the pairings list:
    # if it's 1, add to list
    # if it's more than 1, "/n + self.pairings"


    for melon in melon_types: # take second index from this
        print(f"{melon.name}pairs with")
        for eachpairing in melon.pairings:
            print(f"{eachpairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Return a dictionary whose keys are reporting codes (as strings) and whose values
    # are the appropriate melon type instance for that reporting code

    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon

    # for each_melon in melon_types, 
    # cast each_melon code into a string?
    # reporting_code = melon_dict[] str(each_melon) 
    # for key, value in melon_types.items():
        # # make key melon_types[0], the code
        # # make value rest of stuff[0:]?
        # 

    return melon_dict


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



print(make_melon_types())