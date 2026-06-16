import re

with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update the HTML class
arena_pattern = re.compile(r'<div class="svc"[^>]*>\s*(<div class="ic">.*?</div>)\s*<h3>Arena Service</h3>', re.DOTALL)
html = arena_pattern.sub(r'<div class="svc arena">\n          \1\n          <h3>Arena Service</h3>', html)

# Define the CSS
css_to_add = """
    .svc.arena {
      background: linear-gradient(rgba(16, 19, 25, 0.7), rgba(16, 19, 25, 0.7)),
      url("{% static 'arenaservice.png' %}");
      background-size: cover;
      background-position: center;
      color: #fff;
      border-color: var(--nexa-black)
    }
    .svc.arena p { color: white }
    .svc.arena .ic { background: rgba(255, 255, 255, .1); color: #fff; }
"""

# Inject CSS if it doesn't exist
if '.svc.arena {' not in html:
    html = html.replace('    /* why */', css_to_add + '\n    /* why */')

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added background to Arena card.")
