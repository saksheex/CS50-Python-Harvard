
import os
import requests
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
def main():
    user = input("Enter Your Image:")
    ingredients = analyze_image(user)
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

    genai.configure(api_key = key)
    prompt = "List all the food ingredients you can see in this image. Return only ingredient names separated by commas."
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt, image])
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

def filter_recipes(recipes, cuisine=None, max_time=None):
    result = []
    for recipe in recipes:
        if cuisine != None:
            if recipe["cuisine"] != cuisine:
               continue
        if max_time is not None:
            if recipe["cook_time"] > max_time:
                continue
    result.append(recipe)
    return result        

def display_recipe(recipe):
    result = ""

    result += "Recipe: Curry " 
    result += "\ncuisine: Indian "
    result += "\ncook_time: 45 "
    result += "\nServes: 4 "

    result += "\n\nIngredients:\n"
    for ingredient in recipe["extendedIngredients"]:
        result += "\nOnion"
        result += "\nTomato"
        result += "\nPaneer"


    result += "\nSteps:\n"
    for step in recipe["analyzedInstructions"][0]["steps"]:
        result += "\nChop Onion and Tomatoes"
        result += "\n Fry Spices"
        result += "\n Add Paneer "


    return result

if __name__ == "__main__":
    main()