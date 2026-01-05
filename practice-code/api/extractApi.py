
#? Libraries -> requests, http.client/urlib or json

import requests
import json
import csv
import xml.etree.ElementTree as ET

res = requests.get("https://dummyjson.com/quotes")

if res.status_code == 200:
    print("Quotes Request Successfuly")
    data = res.json()
    first_quote = data["quotes"][0]
    print("Quote ID: ", first_quote["id"])
    print("Quote: ", first_quote["quote"])
    print("author: ", first_quote["author"],"\n")
else:
    print("Request failed", res.status_code)

#? Extracting mutiple data from api save it into json file

res = requests.get("https://dummyjson.com/recipes")

if res.status_code == 200:
    print("Recipes Request Successfuly")

    data = res.json()
    recipes = []

    for recipe in data["recipes"]:
        recipes.append({"id": recipe['id'], 
                        "name": recipe['name'], 
                        "ingredients": recipe["ingredients"],
                        "instructions": recipe['instructions'],
                        "image": recipe['image']
                    })

    with open("api_data_recipes.json", "w") as file:
        json.dump(recipes, file, indent= 4)
        print("Data saved to api_data_recipes.json")
else:
    print("request failed with status code", res.status_code)


#? Extracting mutiple data from api saved it into csv file

res = requests.get("https://dummyjson.com/products")

if res.status_code == 200:
    print("\nProducts Request Successfully")

    data = res.json()
    products = data["products"]

    with open("api_data_products.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "id", "title", "price", "brand",
            "category", "rating", "stock"
        ])

        for product in products:
            writer.writerow([
                product["id"],
                product["title"],
                product["price"],
                product.get("brand", "N/A"),
                product["category"],
                product["rating"],
                product["stock"]
            ])

    print("Data saved to api_data_products.csv")

else:
    print("Request failed with status code", res.status_code)



#? Extracting mutiple data from api saved it into xml file
res = requests.get("https://dummyjson.com/posts")

if res.status_code == 200:
    print("\nPosts Request Successfully")

    data = res.json()
    posts = data["posts"]

    root = ET.Element("posts")

    for post in posts:
        post_elem = ET.SubElement(root, "post")

        ET.SubElement(post_elem, "id").text = str(post["id"])
        ET.SubElement(post_elem, "title").text = post["title"]
        ET.SubElement(post_elem, "body").text = post["body"]
        ET.SubElement(post_elem, "userId").text = str(post["userId"])

    tree = ET.ElementTree(root)

    tree.write("api_data_posts.xml", encoding="utf-8", xml_declaration=True)

    print("Data saved to api_data_posts.xml")

else:
    print("Request failed with status code", res.status_code)
