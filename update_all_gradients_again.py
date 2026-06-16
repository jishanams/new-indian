with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the gradient across all service cards
old_color = "rgb(53 105 209 / 70%)"
new_color = "rgb(102 128 182 / 70%)"

html = html.replace(old_color, new_color)

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated all gradients to the new color.")
