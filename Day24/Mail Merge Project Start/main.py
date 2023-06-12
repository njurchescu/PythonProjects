
PLACEHOLDER = "[name]"

with open("input/Names/invited_names.txt") as file_name:
    # names = file_name.read()
    names = file_name.readlines()
    with open("input/Letters/starting_letter.txt") as file_letter:
        letter = file_letter.read()
        for name in names:
            stripped_name = name.strip()
            new_letter = letter.replace(PLACEHOLDER, stripped_name)
            with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_file:
                completed_file.write(new_letter)

