import re

with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix any BOM
if html.startswith('\ufeff'):
    html = html[1:]

# Replace the slider CSS
old_css = """    .slide-1,
    .slide-2,
    .slide-3 {
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
    }

    .slide-1 {
      background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.4)),
      url("{% static 'banner1.png' %}");
    }

    .slide-2 {
      background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.4)),
      url("{% static 'banner2.png' %}");
    }

    .slide-3 {
      background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.4)),
      url("{% static 'banner3.png' %}");
    }"""

new_css = """    .slide-1,
    .slide-2,
    .slide-3 {
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
    }

    .slide-1 {
      background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.4)), url("{% static 'banner1.png' %}");
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
    }

    .slide-2 {
      background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.4)), url("{% static 'banner2.png' %}");
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
    }

    .slide-3 {
      background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.4)), url("{% static 'banner3.png' %}");
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
    }"""

html = html.replace(old_css, new_css)

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed banner CSS.")
