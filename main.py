"""This module provides a FastAPI app with various endpoints to manipulate names."""

import math
import random
from typing import Optional

from fastapi import Body, FastAPI, HTTPException

app = FastAPI()

# List to store generated names
names = []


@app.get("/")
def index():
    """Welcome message for the API."""
    return {"message": "Welcome to FastAPI API"}


@app.get("/generate_name/{name}")
def generate_name(name: str):
    """Generate a name and add it to the list."""
    names.append(name)
    return {"message": "Name generated successfully", "name": name}


@app.get("/read_names")
def read_names():
    """Read the list of names."""
    return {"names": names}


@app.put("/update_name/{name_index}")
def update_name(name_index: int, new_name: str = Body(..., embed=True)):
    """Update a name in the list by index."""
    if 0 <= name_index < len(names):
        names[name_index] = new_name
        return {"message": "Name updated successfully"}
    raise HTTPException(status_code=404, detail="Invalid index")


@app.delete("/delete_name/{name_index}")
def delete_name(name_index: int):
    """Delete a name from the list by index."""
    if 0 <= name_index < len(names):
        del names[name_index]
        return {"message": "Name deleted successfully"}
    raise HTTPException(status_code=404, detail="Invalid index")


@app.get("/calculate_sin/{number}")
def calculate_sin(number: float):
    """Calculate the sine of a number."""
    return {"sin": math.sin(number)}


@app.get("/calculate_cos/{number}")
def calculate_cos(number: float):
    """Calculate the cosine of a number."""
    return {"cos": math.cos(number)}


@app.get("/generate_random_number")
def generate_random_number(start: Optional[int] = 1, end: Optional[int] = 10):
    """Generate a random number within a specified range."""
    random_number = random.randint(start, end)
    return {"random_number": random_number}
