import re

with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update the HTML class for Scanning Works
pattern_scan = re.compile(r'<div class="svc"[^>]*>\s*(<div class="ic">.*?</div>)\s*<h3>Scanning Works</h3>', re.DOTALL)
html = pattern_scan.sub(r'<div class="svc scanning">\n          \1\n          <h3>Scanning Works</h3>', html)

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed the HTML class for the Scanning Works card.")
