import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():

    animals_data = load_data('animals_data.json')

    output = ''
    for animal in animals_data:
        name = animal.get('name')
        characteristics = animal.get('characteristics', {})
        diet = characteristics.get('diet')
        locations = animal.get('locations')
        animal_type = characteristics.get('type')

        if name:
            output += f"Name: {name}<br/>\n"
        if diet:
            output += f"Diet: {diet}<br/>\n"
        if locations:
            output += f"Location: {locations[0]}<br/>\n"
        if animal_type:
            output += f"Type: {animal_type}<br/>\n"

        output += "<br/>\n"

    with open("animals_template.html", "r") as f:
        template_content = f.read()

    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as f:
        f.write(new_html_content)

    print("Successfully generated animals.html!")


if __name__ == "__main__":
    main()