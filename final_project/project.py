
import os
import requests
from dotenv import load_dotenv
from PIL import Image
from google.genai import types
from google import genai
import io

def main():

    img_path = input("Enter image path: ")
    ingredients = analyze_image(img_path)
    print("Detected ingredients:", ingredients, "\n")
    recipes = get_recipes(ingredients)
    filtered = filter_recipes(recipes)
    if not filtered:
        print("No recipes found.")
    else:
        result = display_recipe(filtered[0])
        print(result)

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
        model="gemini-flash-lite-latest",
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
    api_key = os.getenv("SPOONACULAR_KEY")
    ing = ",".join(ingredients)

    # Step 1: find matching recipes by ingredients
    search_response = requests.get(
        "https://api.spoonacular.com/recipes/findByIngredients",
        params={
            "ingredients": ing,
            "number": 3,
            "ranking": 2,
            "ignorePantry": True,
            "apiKey": api_key,
        }
    )
    recipes = search_response.json()

    # If no response or error, return empty list
    if isinstance(recipes, dict) and "status" in recipes:
        print(f"API Error: {recipes.get('message')}")
        return []
    
    print("Matched recipes:", [r["title"] for r in recipes], "\n")

    if not recipes:
        return []

    # Step 2: fetch full details for each recipe (steps, time, servings)
    ids = ",".join(str(r["id"]) for r in recipes)
    detail_response = requests.get(
        f"https://api.spoonacular.com/recipes/informationBulk",
        params={
            "ids": ids,
            "includeNutrition": False,
            "apiKey": api_key,
        }
    )
    details = {int(d["id"]): d for d in detail_response.json()}

    # Step 3: merge ingredient match info with full details
    for recipe in recipes:
        recipe.update(details.get(recipe["id"], {}))

    return recipes

def filter_recipes(recipes, max_missing=1, min_used=2):
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

    result += "Recipe: " + recipe["title"] + "\n\n"

    result += "\n\nIngredients you have:"
    for ingredient in recipe["usedIngredients"]:
        result += "\n  - " + ingredient["name"]

    result += "\n\nIngredients you need to buy:"
    for ingredient in recipe["missedIngredients"]:
        amount = ingredient["original"]
        result += "\n  - " + amount

    result += "\n\n Cooking Instructions:"
    if recipe.get("analyzedInstructions"):  
        steps = recipe["analyzedInstructions"][0]["steps"]  
        
        for step in steps:
            step_num = step["number"]
            step_text = step["step"]
            result += f"{step_num}. {step_text}\n"
    

    result += "\n\nRecipe image: " + recipe["image"]

    return result

if __name__ == "__main__":
    main()