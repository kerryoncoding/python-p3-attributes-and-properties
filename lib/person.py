#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self):
        if (name(type) == str) and (1 < len(name) < 25):
            self._name = name.title()
        else: 
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)