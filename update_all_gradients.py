with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the gradient across all service cards
old_gradient = "linear-gradient(rgba(16, 19, 25, 0.7), rgba(16, 19, 25, 0.7))"
new_gradient = "linear-gradient(rgb(53 105 209 / 70%), rgba(16, 19, 25, 0.7))"

html = html.replace(old_gradient, new_gradient)

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated all gradients.")
