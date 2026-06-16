import re

with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix multi-line background declarations in .svc classes
pattern = re.compile(r'background:\s*linear-gradient\([^)]+\),\s*\n\s*url\([^)]+\);', re.MULTILINE)

def single_line_repl(match):
    # Just remove the newline and extra spaces
    s = match.group(0)
    return re.sub(r',\s*\n\s*url', ', url', s)

html = pattern.sub(single_line_repl, html)

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed multiline CSS backgrounds.")
