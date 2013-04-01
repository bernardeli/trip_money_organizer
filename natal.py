from models import *

ricardo = Person("Ricardo")
bruno = Person("Bruno")
renato = Person("Renato")
diego = Person("Diego")

contas = Trip([ricardo, bruno, renato, diego])

ricardo.pay(60+40)
bruno.pay(55 + 40)
renato.pay(68+30+117)
diego.pay(82+35)

contas.calculate()
