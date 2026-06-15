import re
path = 'core/templates/core/index.html'
data = open(path, encoding='utf-8').read()
# Replace {% static \'filename\' %} with {% static 'filename' %}
fixed = re.sub(r"\{\%\s*static\s+\\\'([^']+)\\\'\s*\%\}", r"{% static '\1' %}", data)
open(path, 'w', encoding='utf-8').write(fixed)
print("Fixed slashes!")
