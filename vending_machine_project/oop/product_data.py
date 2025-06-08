class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self):
        return self.stock > 0

    def purchase(self):
        if self.is_available():
            self.stock -= 1
            return True
        return False

    def restock(self, qty):
        self.stock += qty

product_list = [
    Product("아이시스", 800, 15),
    Product("아쿠아 제로", 2000, 7),
    Product("레몬워터", 1800, 4),
    Product("옥수수 수염차", 1600, 11),
    Product("콘트라베이스", 2200, 5),
    Product("트레비", 1300, 3),
    Product("펩시 제로", 1100, 12),
    Product("펩시", 1100, 9),
    Product("칠성사이다 제로", 1300, 6),
    Product("칠성사이다", 1300, 13),
    Product("망고", 1200, 22),
    Product("립톤 아이스티", 1200, 12),
    Product("사과에이드", 1100, 15),
    Product("포도에이드", 1100, 10),
    Product("레쓰비", 900, 19),
    Product("가나", 900, 20),
    Product("핫식스 제로", 1300, 18),
    Product("밀키스", 1100, 16),
    Product("핫식스", 1300, 21),
    Product("레쓰비 라떼", 1200, 17),
    Product("게토레이", 1000, 14),
    Product("코코포도", 1000, 6),
    Product("잔치집 식혜", 1000, 8)
]
