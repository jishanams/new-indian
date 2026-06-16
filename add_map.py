import re

with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

map_html = """
  <!-- Google Map Embed -->
  <section id="map" style="width: 100%; line-height: 0;">
    <iframe 
      src="https://www.google.com/maps?q=Mysore+Road,+Sultan+Bathery,+Kerala+673592&output=embed" 
      width="100%" 
      height="450" 
      style="border:0;" 
      allowfullscreen="" 
      loading="lazy" 
      referrerpolicy="no-referrer-when-downgrade">
    </iframe>
  </section>
"""

# Only add if not already there
if 'id="map"' not in html:
    # Replace the first occurrence of <footer> with the map + <footer>
    html = html.replace('<footer>', map_html + '\n  <footer>')
    
    with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Added map successfully.")
else:
    print("Map already exists.")
