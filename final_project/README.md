# Cook GPT

#### Video Demo: <URL HERE>

#### Description:

Cook GPT is a Python program that takes a photo of your ingredients, figures out what's in it, and suggests a recipe you can actually make with what you have. It uses Google Gemini to read the image and Spoonacular to find matching recipes.

You give it an image path. It tells you what to cook.

## Files

### `project.py`

Contains `main` and four other functions:

**`analyze_image(image_path)`**
Opens the image with Pillow, sends it to Gemini's vision model, and asks it to list the ingredients it sees. Returns a Python list of ingredient strings. Raises `FileNotFoundError` if the path is wrong. `temperature=0` is set so the output stays consistent across runs.

**`get_recipes(ingredients)`**
Takes the ingredient list and calls Spoonacular's `/findByIngredients` endpoint to get up to three recipe matches. Then makes a second call to `/informationBulk` to get full cooking instructions for each. Both calls are merged into one return value so the rest of the program only has to deal with a single list.

**`filter_recipes(recipes, max_missing=1, min_used=2)`**
Filters out recipes where you're missing too many ingredients or barely using any of what you have. Defaults are `max_missing=1` and `min_used=2`. These can be changed by the caller if needed.

**`display_recipe(recipe)`**
Formats one recipe into a readable string: title, ingredients you have, ingredients to buy (with amounts), cooking steps, and an image URL.

### `test_project.py`

**`test_analyze_image()`**
Runs `analyze_image` on a real image and checks that it returns a non-empty list. Needs a valid Gemini key in `.env`.

**`test_get_recipes()`**
Mocks `requests.get` using `unittest.mock.patch` so no real API call is made. Checks that the function returns a list of the expected length.

**`test_filter_recipes()`**
Passes three recipes with different ingredient counts and checks that only the one meeting both thresholds comes through.

**`test_display_recipe()`**
Builds a fake recipe dict and checks that the output contains the title, ingredient names, and quantity strings.

### `requirements.txt`

```
requests
python-dotenv
Pillow
google-genai
```

## Design Notes

Gemini was used for image recognition because it handles everyday food items well and returns plain text that's easy to parse. Setting `temperature=0` keeps the ingredient list predictable.

The recipe lookup is split into two API calls because Spoonacular's ingredient-matching endpoint doesn't include cooking steps. A bulk details call was added to get them. Both are wrapped in `get_recipes` so callers don't have to manage two steps.

`filter_recipes` is its own function so it can be tested without touching any API logic and so the thresholds can be tuned without changing how recipes are fetched.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Create a `.env` file with your keys:
   ```
   GEMINI_KEY=your_key
   SPOONACULAR_KEY=your_key
   ```

3. Run:
   ```
   python project.py
   ```

4. Enter an image path when prompted (e.g. `vegetables.png`).

5. Run tests:
   ```
   pytest test_project.py
   ```