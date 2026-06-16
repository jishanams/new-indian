import re

with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update the HTML class for Water Service
pattern_water = re.compile(r'<div class="svc"[^>]*>\s*(<div class="ic">.*?</div>)\s*<h3>Water Service</h3>', re.DOTALL)
html = pattern_water.sub(r'<div class="svc water">\n          \1\n          <h3>Water Service</h3>', html)

# Define the CSS
css_to_add = """
    .svc.water {
      background: linear-gradient(rgba(16, 19, 25, 0.7), rgba(16, 19, 25, 0.7)),
      url("{% static 'waterservice.png' %}");
      background-size: cover;
      background-position: center;
      color: #fff;
      border-color: var(--nexa-black)
    }

    .svc.water p {
      color: white
    }

    .svc.water .ic {
      background: rgba(255, 255, 255, .1);
      color: #fff;
    }
"""

# Inject CSS if it doesn't exist
if '.svc.water {' not in html:
    html = html.replace('    /* why */', css_to_add + '\n    /* why */')

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added background to Water Service card.")
