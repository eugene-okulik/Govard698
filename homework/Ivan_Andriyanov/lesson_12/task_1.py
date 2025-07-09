class Flower:
    def __init__(self, name, price, freshness, color, stem_length, lifespan):
        self.name = name
        self.price = price
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.lifespan = lifespan


class Rose(Flower):
    def __init__(self, name, price, freshness, color, stem_length, lifespan):
        super().__init__(name, price, freshness, color, stem_length, lifespan)


class Lily(Flower):
    def __init__(self, name, price, freshness, color, stem_length, lifespan):
        super().__init__(name, price, freshness, color, stem_length, lifespan)


class Bouquet:
    def __init__(self):
        self.flowers = []  # Список цветов

    def add_flower(self, flower):
        self.flowers.append(flower)

    def get_total_price(self):
        return sum(flower.price for flower in self.flowers)

    def average_lifespan(self):
        if not self.flowers:
            return 0
        return sum(f.lifespan for f in self.flowers) / len(self.flowers)

    def sort_by(self, parameter):
        self.flowers.sort(key=lambda f: getattr(f, parameter))

    def find_by(self, parameter, value):
        return [f for f in self.flowers if getattr(f, parameter) == value]


rose = Rose("Роза", 100, 9, "красный", 40, 7)
lily = Lily("Лилия", 120, 8, "белый", 35, 6)


bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(lily)


print("Стоимость:", bouquet.get_total_price())
print("Увядание:", bouquet.average_lifespan())
