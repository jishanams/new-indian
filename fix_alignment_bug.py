import re

with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to find the mangled block and replace it with the correct classes.
# The mangled block looks like:
#        <div class="svc alignment">
#          <div class="ic">...</div>
#          <h3>Painting</h3>
#          <p>...</p>
#        </div>
#        <div class="svc">
#          <div class="ic">...</div>
#          <h3>Wheel Alignment</h3>
#          <p>...</p>
#        </div>

# Let's just do a direct string replace for the `<div class="svc alignment">` that precedes `<h3>Painting</h3>`.
# But there might be whitespace variations.
# A safe regex:

pattern = re.compile(
    r'<div class="svc alignment">\s*(<div class="ic">.*?</div>)\s*<h3>Painting</h3>(.*?)<div class="svc">\s*(<div class="ic">.*?</div>)\s*<h3>Wheel Alignment</h3>',
    re.DOTALL
)

replacement = r'''<div class="svc painting">
          \1
          <h3>Painting</h3>\2<div class="svc alignment">
          \3
          <h3>Wheel Alignment</h3>'''

html = pattern.sub(replacement, html)

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed the painting and alignment classes.")
