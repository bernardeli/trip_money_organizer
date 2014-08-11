#!/usr/bin/python

from __future__ import division

# verifies if python version is < 2.3.*
import sys
if sys.version_info[1] < 3:
    from helpers_22 import *

class Trip(object):
    def __init__(self, people=[]):
        self.people = people

    def add_person(self, person):
        self.people.append(person)

    def calculate(self):
        people_ordered = self.order_by_payment()
        for person in people_ordered:
            person.other_pay(people_ordered)
        self.show_results()

    def show_results(self):
        for person in self.people:
            if len(person.should_pay.keys()) == 0:
                print "%s does not pay anything" % (person.name)
                continue
            print "%s must pay:" % (person.name)
            for other in person.should_pay.iterkeys():
                if person.should_pay[other] > 0:
                    print "\t%2.2f to %s" % (person.should_pay[other], other.name)

    def order_by_payment(self):
        return sorted(self.people)

class Person(object):
    def __init__(self, name):
        self.name = name
        self.payments = [Payment(0)]
        self.should_pay = dict()
        self.should_receive = 0

    def __repr__(self):
        return self.name

    def __cmp__(self, other):
        if self.max_payment() < other.max_payment():
            return 1
        elif self.max_payment() > other.max_payment():
            return -1
        else:
            return 0

    def other_pay(self, people):
        total = sum(map(lambda x: x.value, self.payments))
        div = total/len(people)
        for person in people:
            pay = person.should_pay.get(self, 0) + div
            if self.should_pay.get(person, 0) > pay:
                self.should_pay[person] -= pay
                if person.should_pay.get(self, False) is not False:
                    del person.should_pay[self]
            else:
                person.should_pay[self] = pay - self.should_pay.get(person, 0)
                if self.should_pay.get(person, False) is not False:
                    del self.should_pay[person]

    def max_payment(self):
        return max(map(lambda x: x.value, self.payments))

    def pay(self, value):
        self.payments.append(Payment(value))

class Payment(object):
    def __init__(self, value=0, name=None):
        self.value = value
        self.name = name # unused
