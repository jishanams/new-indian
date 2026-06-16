import re

with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

video_html = """
      <div style="margin-bottom: 30px; border-radius: var(--radius); overflow: hidden; box-shadow: 0 10px 30px rgba(13, 47, 107, .1);">
        <video autoplay loop muted playsinline style="width: 100%; display: block; max-height: 500px; object-fit: cover;">
          <source src="{% static 'New Indian video.MOV' %}" type="video/mp4">
          Your browser does not support the video tag.
        </video>
      </div>
      <div class="gallery-grid">"""

html = html.replace('<div class="gallery-grid">', video_html, 1)

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added video above gallery grid.")
