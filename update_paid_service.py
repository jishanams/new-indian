import re

with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add a CSS class block for .svc.paid
css_to_add = """
    .svc.paid {
      background: linear-gradient(rgba(16, 19, 25, 0.7), rgba(16, 19, 25, 0.7)),
      url("{% static 'paidservice.png' %}");
      background-size: cover;
      background-position: center;
      color: #fff;
      border-color: var(--nexa-black)
    }

    .svc.paid p {
      color: white
    }

    .svc.paid .ic {
      background: rgba(255, 255, 255, .1);
      color: #fff;
    }
"""

if '.svc.paid {' not in html:
    html = html.replace('    /* why */', css_to_add + '\n    /* why */')

# Find the Paid Service HTML block
# It looks like:
#         <div class="svc">
#           <div class="ic"><svg ...>...</svg></div>
#           <h3>Paid Service</h3>

old_html = '<h3>Paid Service</h3>'

# We just want to replace the `<div class="svc">` right before `Paid Service` with `<div class="svc paid">`
# Let's do a regex to find the div class="svc" that contains Paid Service
# Or we can just use re.sub
pattern = re.compile(r'(<div class="svc")>\s*(<div class="ic">.*?</div>\s*<h3>Paid Service</h3>)', re.DOTALL)
html = pattern.sub(r'\1 paid">\n          \2', html)

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated Paid Service successfully.")
