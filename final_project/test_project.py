
from CS50project import analyze_image
def test_analyze_image():

    result = analyze_image("/Users/sakshee/Desktop/github/datascience-notebook/vegetables.png")
    assert type(result) == list
    assert len(result) > 0


from CS50project import get_recipes
from unittest.mock import patch, MagicMock
def test_get_recipes():
    fake_response = [
    {"id": 1, "title": "Paneer Curry"}
    ]
    mock_get = MagicMock()
    mock_get.json.return_value = fake_response

    with patch("requests.get", return_value=mock_get):
     result = get_recipes(["Onion", "Tomato", "Paneer"])
     assert type(result) == list
     assert len(result) == 1   



from CS50project import filter_recipes
def test_filter_recipes():
    recipes = [
        {"title": "Pizza", "missedIngredientCount": 5, "usedIngredientCount": 2},
        {"title": "Curry", "missedIngredientCount": 1, "usedIngredientCount": 2},
        {"title": "Pasta", "missedIngredientCount": 4, "usedIngredientCount": 1},
    ]
    result = filter_recipes(recipes, max_missing=1, min_used=2)
    assert len(result) == 1
    assert result[0]["title"] == "Curry"
    


from CS50project import display_recipe
def test_display_recipe():
    recipe = {
          "title": "pasta",
          "usedIngredients": [
            {"name": "rice"},         
            {"name": "eggs"},          
        ],
        "missedIngredients": [
            {"name": "ginger", "original": "1 piece ginger"},
            {"name": "soy sauce", "original": "4 tablespoons soy sauce"},
        ],
        "image": "https://img.spoonacular.com/test.jpg"
    }

    result = display_recipe(recipe)
    assert "pasta" in result
    assert "rice" in result
    assert "1 piece ginger" in result
    


