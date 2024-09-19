with open("./Input/Letters/starting_letter.txt") as letter:
    template = letter.read()

#for each name in invited_names.txt

name_list = []

with open("./Input/Names/invited_names.txt") as names:
    for line in names:
        name = line.strip()
        name_list.append(name)

#Replace the [name] placeholder with the actual name.

for name in name_list:
    name_letter = template.replace("[name]", name)
    file_name = name + ".docx"

#Save the letters in the folder "ReadyToSend".

    file_path = "./Output/ReadyToSend/" + file_name

    with open(file_path, "w") as file:
        file.write(name_letter)