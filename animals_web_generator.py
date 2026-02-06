import json


def load_data(file_path):

    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):

    output = '<li class="cards__item">\n'


    name = animal_obj.get('name')
    characteristics = animal_obj.get('characteristics', {})
    diet = characteristics.get('diet')
    locations = animal_obj.get('locations')
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
    return output


def main():

    animals_data = load_data('animals_data.json')


    animals_html_string = ''
    for animal in animals_data:
        animals_html_string += serialize_animal(animal)


    with open("animals_template.html", "r") as f:
        template_content = f.read()

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html_string)


    with open("animals.html", "w") as f:
        f.write(final_html)

    print("Project completed successfully with clean code structure! 🚀")


if __name__ == "__main__":
    main()