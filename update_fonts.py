import re
with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Google Fonts link
html = re.sub(
    r'family=Saira\+Condensed:wght@600;700;800&family=Saira:wght@400;500;600&family=Saira\+Extra\+Condensed:wght@700&family=Noto\+Sans\+Malayalam:wght@600;700;800&display=swap',
    r'family=Roboto:wght@400;500;700;900&family=Noto+Sans+Malayalam:wght@600;700;800&display=swap',
    html
)

# Replace all Saira font families
html = html.replace("'Saira Condensed'", "'Roboto'")
html = html.replace("'Saira Extra Condensed'", "'Roboto'")
html = html.replace("'Saira'", "'Roboto'")

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fonts updated to Roboto!')
