#завдання в модулі 4.2
#Виклич визначену раніше функцію за допомогою жіночого імені та прізвища. Все ще ок? Що ми могли б змінити?
def customized_hello(first_name, last_name):
    print("Hello Mrs %s %s" % (first_name, last_name))

customized_hello("Julia", "Helen")

def customized_hello(first_name, last_name, gender_prefix='Mr'):
    print(f"Hello {gender_prefix} {first_name} {last_name}!")

customized_hello("John", "Cleese")
customized_hello("Clara", "Cleese", "Ms")

#вправа
#Уяви, що ти забув/ла про ще дві позиції в списку покупок і тобі знову потрібно йти в магазин. Зміни список покупок, ввівши „серветки” та “туалетний папір”, а потім викличи функцію.
shopping_items = [
    "яйця",
    "булочка",
    "сир фета",
    "масло",
    "помідор"
]
shopping_items.append("napkings")
shopping_items.append("toilet paper")
print(shopping_items)
def shopping(items):
    shopping_cart = "Koszyk zawiera: "
    for item in items:
        shopping_cart += item + ','
    return shopping_cart

basket = shopping(shopping_items)
print(basket)
def shopping(items, payment='card', shop='local'):
    pass


#Вправа
#Перевір, чи наведену вище функцію можна викликати, надавши лише один аргумент після ключа, тобто payment, і забувши про shop
shopping_items = [
    "яйця",
    "булочка",
    "сир фета",
    "масло",
    "помідор"]

def shopping(items, payments="card", shop="local"):
    pass

#вправа до підтеми Різні типи аргументів в мод 4.2
#Перша з них, fun_default, має приймати позиційні або іменовані аргументи. Друга, fun_positional, лише позиційні. Третя, fun_keyword, тільки іменовані. Щоб перевірити, чи правильно оголошені друга та третя функції, вистачить тільки замінити типи аргументів навпаки, тобто fun_keyword, прийматиме лише позиційні аргументи.
def shopping(items, *, payment='card', shop='local'):
    return None
  


#ми можемо визвати цю функцію, так як робили раніше, надавши лише один обов’язковий аргумент:
print(shopping(shopping_items, payment="cash"))
#або
basket = shopping(shopping_items, payment="cash")
print(basket)

basket = shopping(shopping_items)
print(basket)
