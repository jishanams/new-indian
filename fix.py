import os
import re

path = 'core/templates/core/index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add {% load static %}
if '{% load static %}' not in html:
    html = '{% load static %}\n' + html

# 2. Add Malayalam Font
if 'Noto+Sans+Malayalam' not in html:
    html = html.replace(
        'family=Saira+Extra+Condensed:wght@700&display=swap',
        'family=Saira+Extra+Condensed:wght@700&family=Noto+Sans+Malayalam:wght@600;700;800&display=swap'
    )

# 3. Update slide-1 background
html = re.sub(r'\.slide-1\s*\{\s*background:\s*linear-gradient[^\}]+?\}', 
              r'.slide-1 { background: linear-gradient(to right, rgba(13, 47, 107, 0.85), rgba(16, 19, 25, 0.6)), url("{% static \'banner1.jpeg\' %}") center/cover no-repeat; }', 
              html)

# 4. Add .malayalam-title class
if '.malayalam-title' not in html:
    css_to_add = '''
    .malayalam-title {
      font-family: 'Noto Sans Malayalam', sans-serif !important;
      font-size: clamp(34px, 5vw, 64px) !important;
      line-height: 1.4 !important;
      padding-bottom: 8px;
    }
'''
    html = html.replace('.slide h1 {', css_to_add + '\n    .slide h1 {')

# 5. Malayalam Texts
html = re.sub(r'<h1>All Maruti Services.<br>One <em>Roof</em>.</h1>', '<h1 class="malayalam-title">സർവീസ് ചെയ്യാൻ ഇനി ചുരമിറങ്ങേണ്ട</h1>', html)
html = re.sub(r'<h1>Cashless Claims.<br><em>Zero</em> Running Around.</h1>', '<h1 class="malayalam-title">ഒരൊറ്റ കോളിൽ<br>ഞങ്ങൾ <em>റോഡിലെത്തും.</em></h1>', html)
html = re.sub(r'<h1>Dents Out.<br>Shine <em>Back</em>.</h1>', '<h1 class="malayalam-title"><em>ഞായറും</em> ഞങ്ങൾ<br>പണി മുടക്കില്ല.</h1>', html)

# 6. Images
html = re.sub(r'<div class="n">Arena \+ Nexa</div>', '<img src="{% static \'arena.png\' %}" style="height: 42px; object-fit: contain;" alt="Arena Nexa Logo">', html)
html = re.sub(r'<img src="images/workshop-front.jpg"', '<img src="{% static \'kid3.jpg\' %}"', html)
html = re.sub(r'<img src="images/kid3.jpg"', '<img src="{% static \'kid3.jpg\' %}"', html)
html = re.sub(r'<img src="images/alignment.jpg"', '<img src="{% static \'service bays.png\' %}"', html)
html = re.sub(r'<img src="images/team.jpg"', '<img src="{% static \'trainned team.png\' %}"', html)
html = re.sub(r'<img src="images/customer-lounge.jpg"', '<img src="{% static \'waiting.png\' %}"', html)

# All other images to use static
html = re.sub(r'src="images/([^"]+)"', r'src="{% static \'\1\' %}"', html)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done fixing index.html")
