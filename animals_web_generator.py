import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():

    animals_data = load_data('animals_data.json')


    output = ''
    for animal in animals_data:

        output += '<li class="cards__item">\n'


        name = animal.get('name')
        characteristics = animal.get('characteristics', {})
        diet = characteristics.get('diet')
        locations = animal.get('locations')
        animal_type = characteristics.get('type')


        if name:
            output += f'  <div class="card__title">{name}</div>\n'


        output += '  <p class="card__text">\n'
        if diet:
            output += f'      <strong>Diet:</strong> {diet}<br/>\n'
        if locations:
            output += f'      <strong>Location:</strong> {locations[0]}<br/>\n'
        if animal_type:
            output += f'      <strong>Type:</strong> {animal_type}<br/>\n'
        output += '  </p>\n'


        output += '</li>\n'


    with open("animals_template.html", "r") as f:
        template_content = f.read()

    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)


    with open("animals.html", "w") as f:
        f.write(new_html_content)

    print("Step 4: Professional HTML generated successfully! 🎊")


if __name__ == "__main__":
    main()