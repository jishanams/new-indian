import re

with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add a CSS class blocks
css_to_add = """
    .svc.warranty {
      background: linear-gradient(rgba(16, 19, 25, 0.7), rgba(16, 19, 25, 0.7)),
      url("{% static 'warranty.png' %}");
      background-size: cover;
      background-position: center;
      color: #fff;
      border-color: var(--nexa-black)
    }
    .svc.warranty p { color: white }
    .svc.warranty .ic { background: rgba(255, 255, 255, .1); color: #fff; }

    .svc.body-repair {
      background: linear-gradient(rgba(16, 19, 25, 0.7), rgba(16, 19, 25, 0.7)),
      url("{% static 'body-repair.png' %}");
      background-size: cover;
      background-position: center;
      color: #fff;
      border-color: var(--nexa-black)
    }
    .svc.body-repair p { color: white }
    .svc.body-repair .ic { background: rgba(255, 255, 255, .1); color: #fff; }

    .svc.painting {
      background: linear-gradient(rgba(16, 19, 25, 0.7), rgba(16, 19, 25, 0.7)),
      url("{% static 'paint-card.png' %}");
      background-size: cover;
      background-position: center;
      color: #fff;
      border-color: var(--nexa-black)
    }
    .svc.painting p { color: white }
    .svc.painting .ic { background: rgba(255, 255, 255, .1); color: #fff; }
"""

if '.svc.warranty {' not in html:
    html = html.replace('    /* why */', css_to_add + '\n    /* why */')

# Warranty
pattern_warranty = re.compile(r'(<div class="svc")>\s*(<div class="ic">.*?</div>\s*<h3>Warranty Service</h3>)', re.DOTALL)
html = pattern_warranty.sub(r'\1 warranty">\n          \2', html)

# Body Repair
pattern_body = re.compile(r'(<div class="svc")>\s*(<div class="ic">.*?</div>\s*<h3>Body Repairing Works</h3>)', re.DOTALL)
html = pattern_body.sub(r'\1 body-repair">\n          \2', html)

# Painting
pattern_paint = re.compile(r'(<div class="svc")>\s*(<div class="ic">.*?</div>\s*<h3>Painting</h3>)', re.DOTALL)
html = pattern_paint.sub(r'\1 painting">\n          \2', html)

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated more service cards successfully.")
