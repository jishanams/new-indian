import re

with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Use regex to fix the typos regardless of icon
nexa_pattern = re.compile(r'<div class="svc"[^>]*>\s*(<div class="ic">.*?</div>)\s*<h3>Nexa Service</h3>', re.DOTALL)
html = nexa_pattern.sub(r'<div class="svc nexa">\n          \1\n          <h3>Nexa Service</h3>', html)

arena_pattern = re.compile(r'<div class="svc"[^>]*>\s*(<div class="ic">.*?</div>)\s*<h3>Arena Service</h3>', re.DOTALL)
html = arena_pattern.sub(r'<div class="svc">\n          \1\n          <h3>Arena Service</h3>', html)


css_to_add = """
    .svc.nexa {
      background: linear-gradient(rgba(16, 19, 25, 0.7), rgba(16, 19, 25, 0.7)),
      url("{% static 'nexa.png' %}");
      background-size: cover;
      background-position: center;
      color: #fff;
      border-color: var(--nexa-black)
    }
    .svc.nexa p { color: white }
    .svc.nexa .ic { background: rgba(255, 255, 255, .1); color: #fff; }
"""

if '.svc.nexa {' not in html:
    html = html.replace('    /* why */', css_to_add + '\n    /* why */')

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed Nexa card background and corrected typos.")
