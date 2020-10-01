
class Icecream(object):
    def __init__(self, flavor, style, container, toppings="None"):
        self.flavor = flavor
        self.style = style
        self.container = container
        self.toppings = toppings
    def serve(self):
        print("ENJOY!")
if __name__ == "__main__":
    icecream = Icecream("Chocolate", "Scoop", "Cone", "Almonds")
    print(icecream.flavor, icecream.style, icecream.container,
     icecream.toppings)
    icecream.serve()