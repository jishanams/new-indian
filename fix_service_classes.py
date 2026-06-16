import re

with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the user's manual typos
html = html.replace('<div class="svc" warranty">', '<div class="svc warranty">')
html = html.replace('<div class="svc" body-repair">', '<div class="svc">')
html = html.replace('<div class="svc" painting">', '<div class="svc">')

# Now let's make sure Body Repair and Painting have their correct classes.
# We want <div class="svc body-repair"> for Body Repairing Works
pattern_body = re.compile(r'(<div class="svc")>\s*(<div class="ic">.*?</div>\s*<h3>Body Repairing Works</h3>)', re.DOTALL)
html = pattern_body.sub(r'\1 body-repair">\n          \2', html)

# We want <div class="svc painting"> for Painting
pattern_paint = re.compile(r'(<div class="svc")>\s*(<div class="ic">.*?</div>\s*<h3>Painting</h3>)', re.DOTALL)
html = pattern_paint.sub(r'\1 painting">\n          \2', html)

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed service card classes.")
