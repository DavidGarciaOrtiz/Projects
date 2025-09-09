import numpy as np

def greater_than_10(arr):
    """Return a boolean array indicating which elements are greater than 10."""
    return arr > 10

# Example test    
print(greater_than_10(11)) # True
print(greater_than_10(9))  # False