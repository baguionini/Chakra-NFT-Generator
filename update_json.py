import json

uri = ""

def update_url(file_name):
    file = open(f"json/{file_name}.json", "r")
    json_object = json.load(file)

    file.close()

    json_object["image"] = f"ipfs://{uri}/{file_name}.png"

    file = open(f"json/{file_name}.json", "w")

    json.dump(json_object, file, indent=4)
    file.close()

for i in range(32):
    update_url(i+1)