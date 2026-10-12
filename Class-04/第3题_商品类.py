class Commodity:
    def __init__(self, name, cost, price):
        self.name = name
        self._cost = cost
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < self._cost:
            print("售价不能低于成本价！")
            return
        self._price = value

    @classmethod
    def get_discount_rate(cls, origin_price, sell_price):
        return sell_price / origin_price

    def __repr__(self):
        return (
            f"Commodity(名称={self.name},成本={self._cost},"
            f"售价={self._price})"
        )


commodity1 = Commodity("笔记本", 30, 50)
commodity2 = Commodity("鼠标", 20, 40)
commodity1.price = 25
commodity2.price = 32

print(commodity1)
print(commodity2)
print(f"折扣率：{Commodity.get_discount_rate(40, commodity2.price)}")
