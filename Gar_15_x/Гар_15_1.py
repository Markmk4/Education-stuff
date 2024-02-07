class Soda:
    def __init__(self, additive):
        self.additive = additive

    def show_my_drink(self):
        print(self.additive)

lemonade=Soda("lemon")
lemonade.show_my_drink()