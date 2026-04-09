def main():
    pass

def analyze_image(image_path):
    pass

def get_recipes(ingredients):
    pass

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
    pass

if __name__ == "__main__":
    main()