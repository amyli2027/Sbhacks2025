import json

# Open and read the JSON file
with open('menu_data.json', 'r') as file:
    data = json.load(file)

#exact search
def search_food(name):
    results = []  # To store search results
    for dining_hall in data:
        hall_name = dining_hall.get('dining_hall', 'Unknown')
        meals = dining_hall.get('meals', [])
        date = dining_hall.get('date', 'Unknown')
        
        for meal in meals:
            meal_type = meal.get('meal_type', 'Unknown')
            food_items = meal.get('food_items', [])
            
            for category in food_items:
                category_name = category.get('category', 'Unknown')
                items = category.get('items', [])
                
                # Check if the searched food is in the items list
                if name in items:
                    results.append({
                        'dining_hall': hall_name,
                        'meal_type': meal_type,
                        'category': category_name,
                        'food_item': name, 
                        'date': date
                    })
    
    return results

#partial search
def search_food2(partial_name):
    results = []  # To store search results
    partial_name_lower = partial_name.lower()  # Convert to lowercase 
    
    for entry in data:
        date = entry.get('date', 'Unknown')
        dining_hall = entry.get('dining_hall', 'Unknown')
        meals = entry.get('meals', [])
        
        for meal in meals:
            meal_type = meal.get('meal_type', 'Unknown')
            food_items = meal.get('food_items', [])
            
            for category in food_items:
                category_name = category.get('category', 'Unknown')
                items = category.get('items', [])
                
                # Check if the partial term is in any food item's name
                matching_items = [item for item in items if partial_name_lower in item.lower()]
                
                for match in matching_items:
                    results.append({
                        'date': date,
                        'dining_hall': dining_hall,
                        'meal_type': meal_type,
                        'category': category_name,
                        'food_item': match
                    })
    
    return results

# Search for a specific food item
search_results = search_food('Baked Potato(vgn)')
search_results2 = search_food2('bac')

# Display the results
if search_results: #exact search
    print("Food found in the following locations:")
    for result in search_results:
        print(f"- {result['food_item']} is available at {result['dining_hall']} during {result['meal_type']} in the {result['category']} section at {result['date']}.")
else:
    print("Food not found.")

print("NEW SEARCH") #partial search
if search_results2:
    print("Food found in the following locations:")
    for result in search_results2:
        print(f"- {result['food_item']} is available at {result['dining_hall']} during {result['meal_type']} in the {result['category']} section at {result['date']}.")
else:
    print("Food not found.")
