# def my_shiny_new_decorator(function_to_decorate):
#     # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
#     # получая возможность исполнять произвольный код до и после неё.
#     def the_wrapper_around_the_original_function():
#        print("Я - код, который отработает до вызова функции")
#        function_to_decorate() # Сама функция
#        print("А я - код, срабатывающий после")
#     # Вернём эту функцию
#     return the_wrapper_around_the_original_function


# def stand_alone_function():
#     print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")

# stand_alone_function = my_shiny_new_decorator(stand_alone_function)

# stand_alone_function()




# @my_shiny_new_decorator
# def another_stand_alone_function():
#     print("Оставь меня в покое")

# another_stand_alone_function()


# def bread(func):
#     def wrapper():
#        print()
#        func()
#        print("<\______/>")
#     return wrapper

# def ingredients(func):
#      def wrapper():
#          print("#помидоры#")
#          func()
#          print("~салат~")
#      return wrapper

# @ingredients
# def sandwich(food="--ветчина--"):
#      print(food)

# sandwich()

# def decorate_func(func):
#     def wrapper():
#         print("вызывается первым")
#         func()
#         print("Вызывается после")
#     return wrapper

# @decorate_func
# def print_func():
#     print("сама функция")

# print_func()

# Декорирование методов

# def method_friendly_decorator(method_to_decorate):
#      def wrapper(self, lie):
#          lie -= 3
#          return method_to_decorate(self, lie)
#      return wrapper

# class Lucy:
#      def __init__(self):
#          self.age = 32
#      @method_friendly_decorator
#      def sayYourAge(self, lie):
#          print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))

# l = Lucy()
# l.sayYourAge(-3)

# общий декратор

# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#     # Данная "обёртка" принимает любые аргументы
#     def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
#         print("Передали ли мне что-нибудь?:")
#         print(args)
#         print(kwargs)
#         function_to_decorate(*args, **kwargs)
#     return a_wrapper_accepting_arbitrary_arguments

# @a_decorator_passing_arbitrary_arguments
# def function_with_no_argument():
#     print("Python is cool, no argument here.")

# function_with_no_argument()

# @a_decorator_passing_arbitrary_arguments
# def function_with_arguments(a, b, c):
#     print(a, b, c)

# function_with_arguments(1, 2, 3)

# @a_decorator_passing_arbitrary_arguments
# def function_with_named_arguments(a, b, c, platypus="Почему нет?"):
#    print("Любят ли {}, {} и {} утконосов? {}".format(a, b, c, platypus))

# function_with_named_arguments("Билл", "Линус", "Стив", platypus="Определенно!")
# ('Билл', 'Линус', 'Стив')
# {'platypus': 'Определенно!'}



# class Mary(object):
#    def __init__(self):
#      self.age = 31
#    @a_decorator_passing_arbitrary_arguments
#    def sayYourAge(self, lie=-3): # Теперь мы можем указать значение по умолчанию
#       print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))

# m = Mary()
# m.sayYourAge()

# Примеры использования декораторов

def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock() - t)
        return res
    return wrapper

def logging(func):
    """
    Декоратор, логирующий работу кода.
    (хорошо, он просто выводит вызовы, но тут могло быть и логирование!)
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return res
    return wrapper

def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper

@benchmark
@logging
@counter
def reverse_string(string):
    return ''.join(reversed(string))

print(reverse_string("А роза упала на лапу Азора"))
print(reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura,"
"maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag,"
"a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash,"
"a jar, sore hats, a peon, a canal: Panama!"))