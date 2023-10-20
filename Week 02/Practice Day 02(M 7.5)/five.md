## Explain the difference between inheritance and composition with proper examples.

Difference between inheritance and composition:

| Inheritance | Composition |
| --- | --- |
| Inheritance represents  the is-a relationship | Composition is a has-a relationship |
| A child class can access all public and protected members of the parent class | Composition does not allow direct access to the members of the composed objects |
| Changes to the parent class can affect all child classes | Changes to the composed objects do not affect other composed objects |
| Inheritance cannot extend the final class | Composition allows code reuse even from final classes. |

Inheritance:
```
# Inheritance provides "is a" realtion

class Animal:
    pass

# Dog is an animal
class Dog:
    pass

# Cow is an animal
class Cow:
    pass
```

Composition:
```
# Composition provides "has a" relation

class Engine:
    pass

# Car has a Engine
class Car:
    def __init__(self):
        self.engine = Engine()



class CPU:
    pass
# Computer has cpu
class Computer:
    def __init__(self):
        self.cpu = CPU()
```