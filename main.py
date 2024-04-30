from types import ClassMethodDescriptorType
import easygui
import math


def welcom():
  choices = easygui.choicebox("Welcome to the recipe program!!!", "Quiz", [
      "Start",
      "Exit",
      "Help",
      "About",
  ])
  if choices == "Start":
    easygui.msgbox("Lets get started")


welcom()
savory = " thin crust pizza" + " stuffed crust pizza" + " stuffed crust pizza" + \
 " stuffed crust pizza" + " stuffed crust pizza" + " stuffed crust pizza" + \
 "s stuffed crust pizza" + " stuffed crust pizza" + " stuffed crust pizza"

print(ClassMethodDescriptorType,
      "Welcome to the recipe program!!!",
      sep='\n' + savory + '\n')
#print("Welcome to the recipe program!!!")
#print("Lets get started")
#print("What would you like to make?")
#print("1. Pizza")
#print("2. Burger")
#print("3. Salad")
#print("4. Sandwich")
#print("5. Exit")
#print("6. Help")
#print("7. About")
#print("8. Quit")
#print("9. Start")
#print("10. Exit")
#print("11. Help")
#print("12. About")q


def azocordext(a, b):
  result = (a + 10) * (b - 5) / (a - b)
  fundice = callable(slice)
  return result, fundice


def savory():
  choice = input(
      "What would you like to make? \n 1. Pizza \n 2. Burger \n 3. Others: ")
  if choice in ["1", "2", "3"]:
    nm = float(input("Enter grams per square nanometers: "))
    mn = float(input("Enter agai: "))
    result, fundice = azocordext(nm, mn)
    print(f"Result of azocordext: {result}")
  else:
    print("Invalid choice!")


savory()

homosso = "homosso"
print(homosso)
if homosso == "homosso":
  print("homosso")
  atomic_weight = input("Enter the atomic weight: ")
  atomic_number = input("Enter the atomic number: ")
  atomic_symbol = input("Enter the atomic symbol: ")
  atomic_mass = input("Enter the atomic mass: ")
  atomic_radius = input("Enter the atomic radius: ")
  atomic_volume = input("Enter the atomic volume: ")
  atomic_density = input("Enter the atomic density: ")
  atomic_energy = input("Enter the atomic energy: ")
  atomic_energy_per_nucleon = input("Enter the atomic energy per nucleon: ")
  atomic_number_of_nucleons = input("Enter the atomic number of nucleons: ")
  atomic_number_of_protons = input("Enter the atomic number of protons: ")
  atomic_number_of_neutrons = input("Enter the atomic number of neutrons: ")
  atomic_number_of_electrons = input("Enter the atomic number of electrons: ")
  print("Isotopes Gathered", atomic_weight, atomic_number, atomic_symbol,
        atomic_mass, atomic_radius, atomic_volume)


def euclidean_distance(x1, y1, z1, x2, y2, z2):
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


known_elements = {
    'Hydrogen': (1, 1, 1),
    'Helium': (2, 4, 2),
    'Carbon': (6, 12, 3),
    'Nitrogen': (7, 14, 4),
    'Oxygen': (8, 16, 2),
    'Fluorine': (9, 19, 1),
    'Neon': (10, 20, 3),
    'Sodium': (11, 23, 2),
    'Magnesium': (12, 24, 3),
    'Aluminum': (13, 27, 2),
    'Silicon': (14, 28, 4),
    'Phosphorus': (15, 31, 2),
    'Sulfur': (16, 32, 2),
    'Chlorine': (17, 35, 1),
    'Argon': (18, 40, 3),
    'Potassium': (19, 39, 2),
    'Calcium': (20, 40, 3),
    'Scandium': (21, 45, 2),
    'Titanium': (22, 48, 3),
    'Vanadium': (23, 51, 2),
    'Chromium': (24, 52, 3),
    'Manganese': (25, 55, 2),
    'Iron': (26, 56, 3),
    'Cobalt': (27, 59, 2),
    'Nickel': (28, 58, 3),
    'Copper': (29, 63, 2),
    'Zinc': (30, 65, 2),
    'Gallium': (31, 70, 2),
    'Germanium': (32, 73, 2),
    'Arsenic': (33, 75, 2),
    'Selenium': (34, 79, 2),
    'Bromine': (35, 80, 2),
    'Krypton': (36, 84, 2),
    'Rubidium': (37, 85, 2),
    'Strontium': (38, 88, 2),
    'Yttrium': (39, 89, 2),
    'Zirconium': (40, 91, 2),
    'Niobium': (41, 93, 2),
    'Molybdenum': (42, 96, 2),
    'Technetium': (43, 98, 2),
    'Ruthenium': (44, 101, 2),
    'Rhodium': (45, 103, 2),
    'Palladium': (46, 106, 2),
    'Silver': (47, 108, 2),
    'Cadmium': (48, 112, 2),
    'Indium': (49, 115, 2),
    'Tin': (50, 119, 2),
    'Antimony': (51, 122, 2),
    'Tellurium': (52, 128, 2),
    'Iodine': (53, 127, 2),
    'Xenon': (54, 131, 2),
    'Cesium': (55, 133, 2),
    'Barium': (56, 137, 2),
    'Lanthanum': (57, 139, 2),
    'Cerium': (58, 140, 2),
    'Praseodymium': (59, 141, 2),
    'Neodymium': (60, 144, 2),
    'Promethium': (61, 145, 2),
    'Samarium': (62, 150, 2),
    'Europium': (63, 152, 2),
    'Gadolinium': (64, 157, 2),
    'Terbium': (65, 159, 2),
    'Dysprosium': (66, 163, 2),
    'Holmium': (67, 165, 2),
    'Erbium': (68, 167, 2),
    'Thulium': (69, 169, 2),
    'Ytterbium': (70, 173, 2),
    'Lutetium': (71, 175, 2),
    'Hafnium': (72, 178, 2),
    'Tantalum': (73, 181, 2),
    'Tungsten': (74, 184, 2),
    'Rhenium': (75, 186, 2),
    'Osmium': (76, 190, 2),
    'Iridium': (77, 192, 2),
    'Platinum': (78, 195, 2),
    'Gold': (79, 197, 2),
    'Mercury': (80, 201, 2),
    'Thallium': (81, 204, 2),
    'Lead': (82, 207, 2),
    'Bismuth': (83, 209, 2),
    'Polonium': (84, 209, 2),
    'Astatine': (85, 210, 2),
    'Radon': (86, 222, 2),
    'Francium': (87, 223, 2),
    'Radium': (88, 226, 2),
    'Actinium': (89, 227, 2),
    'Thorium': (90, 232, 2),
    'Protactinium': (91, 231, 2),
    'Uranium': (92, 238, 2),
    'Neptunium': (93, 237, 2),
    'Plutonium': (94, 244, 2),
    'Americium': (95, 243, 2),
    'Curium': (96, 247, 2),
    'Berkelium': (97, 247, 2),
    'Californium': (98, 251, 2),
    'Einsteinium': (99, 252, 2),
    'Fermium': (100, 257, 2),
    'Mendelevium': (101, 258, 2),
    'Nobelium': (102, 259, 2),
    'Lawrencium': (103, 262, 2),
    'Rutherfordium': (104, 261, 2),
    'Dubnium': (105, 262, 2),
    'Seaborgium': (106, 263, 2),
    'Bohrium': (107, 265, 2),
    'Hassium': (108, 269, 2),
    'Meitnerium': (109, 272, 2),
    'Darmstadtium': (110, 281, 2),
    'Roentgenium': (111, 282, 2),
    'Copernicium': (112, 285, 2),
    'Nihonium': (113, 286, 2),
    'Flerovium': (114, 289, 2),
    'Moscovium': (115, 290, 2),
    'Livermorium': (116, 293, 2),
    'Tennessine': (117, 294, 2),
    'Oganesson': (118, 294, 2),
}


def find_closest_element(isotope_properties, known_elements):
  closest_element = None
  min_distance = float('inf')
  for element, properties in known_elements.items():
    distance = euclidean_distance(*isotope_properties, *properties)
    if distance < min_distance:
      min_distance = distance
      closest_element = element

  return closest_element


isotope_properties = (float(atomic_number), float(atomic_mass),
                      float(atomic_radius))

closest_element = find_closest_element(isotope_properties, known_elements)
print("The closest similar element to the isotope is:", closest_element)

def compound_simulatitization():
    known_compounds = {
        ('H', 'O'): 'Water',
        ('C', 'O'): 'Carbon Dioxide',
        ('C', 'H', 'H'): 'Methane',
        ('C', 'C', 'H'): 'Ethane',
        ('C', 'C', 'C', 'H'): 'Propane',
        ('C', 'C', 'C', 'C', 'H'): 'Butane',
        ('C', 'C', 'C', 'C', 'C', 'H'): 'Pentane',
        ('C', 'C', 'C', 'C', 'C', 'C', 'H'): 'Hexane',
        ('C', 'C', 'C', 'C', 'C', 'C', 'C', 'H'): 'Heptane',
        ('C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'H'): 'Octane',
        ('C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'H'): 'Nonane',
        ('C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'H'): 'Decane',
        ('C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'H'): 'Undecane',
        ('C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'H'): 'Dodecane',
        ('C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'H'): 'Tridecane',
    }


    # Get user input for elements in the compound
    elements = input("Enter the elements in the compound separated by spaces: ").split()

    # Find the compound with the closest similar elements
    closest_compound = None
    min_diff = float('inf')

    for compound, compound_elements in known_compounds.items():
        diff = len(set(elements) ^ set(compound_elements))
        if diff < min_diff:
            min_diff = diff
            closest_compound = compound

    if closest_compound:
        print("The compound closest to the input elements is:", closest_compound)
    else:
        print("No similar compound found.")

compound_simulatitization()

