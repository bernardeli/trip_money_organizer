from models import *

b = Person("Bruno")
r = Person("Chapeleira")
p = Person("Pessoal")
a = Person("Raissa")
c = Person("Carol")

ubatuba = Trip([b,r,p,a,c])
b.pay(107)
p.pay(63)
a.pay(20)
c.pay(25)
ubatuba.calculate()

