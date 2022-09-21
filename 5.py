from string import Template

def add_tags(x,y):
    if x == 'i':
        t = Template("<i> ${name} </i>")

    else:
        t = Template("<b> ${name} </b>")
    return t.substitute({'name': y})


print(add_tags('b', 'python'))