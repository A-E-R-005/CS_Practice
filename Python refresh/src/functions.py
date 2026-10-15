def add(a: float, b:float) -> float:
    print(f"Adding {a} + {b}")
    return a+b


print(add(4,5))


def greet(name: str, greeting: str = "Hi") -> None:
    print(f"{greeting}, {name}")


greet("Adam", "Ciao")
greet("Bob")

def func():
    print('Hello')

func()
func()
func()