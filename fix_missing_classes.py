import re

with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add class to Body Repairing Works
pattern_body = re.compile(r'(<div class="svc"[^>]*>)\s*(<div class="ic">.*?</div>)\s*<h3>Body Repairing Works</h3>', re.DOTALL)
html = pattern_body.sub(r'<div class="svc body-repair">\n          \2\n          <h3>Body Repairing Works</h3>', html)

# Add class to Painting
pattern_paint = re.compile(r'(<div class="svc"[^>]*>)\s*(<div class="ic">.*?</div>)\s*<h3>Painting</h3>', re.DOTALL)
html = pattern_paint.sub(r'<div class="svc painting">\n          \2\n          <h3>Painting</h3>', html)

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Restored body-repair and painting classes.")
