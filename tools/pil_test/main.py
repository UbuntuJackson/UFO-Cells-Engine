from PIL import Image
from itertools import product
import json
import os

def split_image(path, w, h):

    for i in os.listdir("res/picture_data"):
        print(i)
        os.remove("res/picture_data/"+ i)

    for i in os.listdir("res/splitted_images"):
        print(i)
        os.remove("res/splitted_images/" + i)

    picture_data = {
        "chunks" : []
    }

    
    chunk_size = w, h

    image = Image.open("res/images/" + path + ".png")
    w, h = image.size

    grid = product(range(0, w, chunk_size[0]), range(0, h, chunk_size[1]))

    for x, y in grid:
        chunk = (x, y, x+chunk_size[0], y+chunk_size[1])
        out = "res/splitted_images/" + path + "_" + str(x) + "_" + str(y) + ".png"

        picture_data["chunks"].append({"path" : out, "x" : int(x/chunk_size[0]), "y" : int(y/chunk_size[1])})
        image.crop(chunk).save(out)

    j_picture_data = json.dumps(picture_data, indent = 4)

    with open("res/picture_data/" + path + ".json", "w") as outfile:
        outfile.write(j_picture_data)

    del image

split_image("image_to_split") #python program needs to take arguments
