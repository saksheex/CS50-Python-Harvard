
from CS50project import filter_recipes
def test_filter_recipes():
    recipes = [
        {"name": "Pasta", "cuisine": "Italian", "cook_time": 20},
        {"name": "Curry", "cuisine": "Indian", "cook_time": 45}

    ]
    result = filter_recipes(recipes,cuisine = "Indian")
    assert len(result) == 1
    assert result[0]["name"] == "Curry"

    