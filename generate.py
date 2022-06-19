import random
import math
import json
import os
from samila import GenerativeImage, Projection

base_uri = "replace"
collection_name = "Chakra"
description = "Chakra is a generative piece of art created using Samila."

def create_attributes(spiral_color, bg_color):
    return [
        {
            "trait_type": "Spiral Color",
            "value": spiral_color
        },
        {
            "trait_type": "Background Color",
            "value": bg_color
        },
    ]

def create_folder(directory_name):
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, rf'{directory_name}')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

def create_json_file(file_name, props):
    # Serializing json 
    json_object = json.dumps(props, indent = 4)
    
    # Writing to sample.json
    with open(f"json/{file_name}.json", "w") as outfile:
        outfile.write(json_object)

def generate_random_color():
    r = lambda: random.randint(0,255)
    return "#%02X%02X%02X" % (r(),r(),r())

def f1(x,y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result

def f2(x,y):
    result = random.uniform(-1,1) * x**3  - math.cos(y**2) + abs(y-x)
    return result

def f3(x,y):
    result = random.uniform(-1,1) * x**2  - math.cos(y**2) + abs(y-x)
    return result

def f4(x,y):
    result = random.uniform(-1,1) * x**3  - math.sin(y**2) + abs(y-x)
    return result

def generate_image(function1, function2, background_color, number):

    image = GenerativeImage(function1, function2)

    spiral_color = generate_random_color()
    image.generate()
    image.plot(
        projection=Projection.POLAR, 
        color=spiral_color, 
        bgcolor=background_color
    )

    props = {
        "name": f"{collection_name} #{number}",
        "description": description,
        "image": f"ipfs://{base_uri}/{number}.png",
        "attributes": create_attributes(spiral_color, background_color)
    }

    print(f"Saving image {number}")
    image.save_image(file_adr=f"img/{number}.png", depth=2)
    create_json_file(number, props)

if __name__ == "__main__":

    functions = [f1, f2, f3, f4]
    background_colors = ["black", "white"]
    current_img = 1

    create_folder('img')
    create_folder('json')
    for color in background_colors:
        for function_1 in functions:
            for function_2 in functions:
                generate_image(function_1, function_2, color, current_img)
                current_img += 1