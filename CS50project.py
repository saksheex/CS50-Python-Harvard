
import os
import requests
from dotenv import load_dotenv
from PIL import Image
from google.genai import types
from google import genai
import io


def main():
    img_path = input("Enter img path:")
    ingredients = analyze_image(img_path)
    recipes = get_recipes(ingredients)
    filtered = filter_recipes(recipes)
    result = display_recipe(filtered[0])
    print (result)

def analyze_image(image_path):
    load_dotenv()
    key = os.getenv("GEMINI_KEY")

    if not os.path.exists(image_path):
       raise FileNotFoundError(f"Image not found: {image_path}")

    image = Image.open(image_path)
    buf = io.BytesIO()
    image.save(buf, format=image.format or "JPEG")
    mime = "image/" + (image.format or "JPEG").lower()

    client = genai.Client(api_key=key)
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=[
            types.Part.from_bytes(data=buf.getvalue(), mime_type=mime),
            types.Part.from_text(text="List all the food ingredients you can see in this image. Return only ingredient names separated by commas."),
        ],
        config=types.GenerateContentConfig(
            temperature=0,
            top_p=0.95,
            top_k=20,
        ),
    )

    ingredients_string = response.text

    ingredients = []
    for items in ingredients_string.split(","):
      ingredients.append(items.strip())
    return ingredients


def get_recipes(ingredients):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    ing = ",".join(ingredients)
    parameters = {
        "ingredients": ing,
        "number": 5,
        "apiKey": api_key,
    }
    response = requests.get("https://api.spoonacular.com/recipes/findByIngredients",params=parameters)
    recipes = response.json()

    return recipes
        
def filter_recipes(recipes, max_missing=None, min_used=None):
    result = []
    for recipe in recipes:
        if max_missing is not None:
            if recipe["missedIngredientCount"] > max_missing:
                continue
        if min_used is not None:
            if recipe["usedIngredientCount"] < min_used:
                continue
        result.append(recipe)
    return result
    
def display_recipe(recipe):
   
    result = ""

    result += "Recipe: " + recipe["title"]
    result += "\nIngredients you have: " + str(recipe["usedIngredientCount"])
    result += "\nIngredients you need: " + str(recipe["missedIngredientCount"])

    result += "\n\nIngredients you have:"
    for ingredient in recipe["usedIngredients"]:
        result += "\n  - " + ingredient["name"]

    result += "\n\nIngredients you need to buy:"
    for ingredient in recipe["missedIngredients"]:
        amount = ingredient["original"]
        result += "\n  - " + amount

    result += "\n\nRecipe image: " + recipe["image"]

    return result


if __name__ == "__main__":
    main()