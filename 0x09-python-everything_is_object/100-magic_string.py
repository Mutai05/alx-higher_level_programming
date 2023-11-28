#!/usr/bin/python3

def magic_string():
    """Generates a string 'BestSchool' repeated a certain number of times based on the iteration count."""
    return ", ".join(["BestSchool"] * magic_string.iteration_count())

magic_string.iteration_count = lambda: magic_string.iteration_count.__dict__.setdefault("count", 0) + 1

