import re

with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update .slide .container
# Current:
#     .slide .container {
#       padding: 84px 20px 70px;
#       position: relative;
#       z-index: 1
#     }
new_slide_container_css = """    .slide .container {
      padding: 84px 20px 140px;
      position: relative;
      z-index: 1;
      min-height: 80vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }"""
html = re.sub(r'    \.slide \.container \{[^\}]+\}', new_slide_container_css, html)

# Update .hero-ctas
# Current:
#     .hero-ctas {
#       display: flex;
#       gap: 14px;
#       margin-top: 34px;
#       flex-wrap: wrap
#     }
new_hero_ctas_css = """    .hero-ctas {
      display: flex;
      gap: 14px;
      flex-wrap: wrap;
      position: absolute;
      bottom: 40px;
      left: 20px;
      right: 20px;
    }"""
html = re.sub(r'    \.hero-ctas \{[^\}]+\}', new_hero_ctas_css, html)

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated hero-ctas to be at the bottom of the container.")
