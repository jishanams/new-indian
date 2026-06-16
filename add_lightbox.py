import re

with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# CSS to add
css = """
    /* Lightbox Modal */
    .lightbox {
      display: none;
      position: fixed;
      z-index: 9999;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.9);
      justify-content: center;
      align-items: center;
      padding: 20px;
      opacity: 0;
      transition: opacity 0.3s ease;
    }
    .lightbox.active {
      display: flex;
      opacity: 1;
    }
    .lightbox img {
      max-width: 90%;
      max-height: 90vh;
      border-radius: 8px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
      object-fit: contain;
    }
    .lightbox-close {
      position: absolute;
      top: 20px;
      right: 30px;
      color: white;
      font-size: 40px;
      font-weight: bold;
      cursor: pointer;
      user-select: none;
    }
    .g-item { cursor: pointer; }
"""

# HTML/JS to add before </body>
js_html = """
  <!-- Lightbox Modal -->
  <div id="lightbox" class="lightbox" onclick="closeLightbox()">
    <span class="lightbox-close">&times;</span>
    <img id="lightbox-img" src="">
  </div>

  <script>
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    
    // Add click listeners to all gallery images
    document.querySelectorAll('.g-item img').forEach(img => {
      img.addEventListener('click', function(e) {
        e.stopPropagation(); // Prevent g-item click if needed
        lightboxImg.src = this.src;
        lightbox.classList.add('active');
      });
    });
    
    // Add click listeners to the wrappers too in case they click the label
    document.querySelectorAll('.g-item').forEach(item => {
      item.addEventListener('click', function() {
        const img = this.querySelector('img');
        if(img) {
          lightboxImg.src = img.src;
          lightbox.classList.add('active');
        }
      });
    });

    function closeLightbox() {
      lightbox.classList.remove('active');
    }
  </script>
</body>
"""

# Inject CSS
if '.lightbox {' not in html:
    html = html.replace('</style>', css + '</style>')

# Inject HTML/JS
if 'id="lightbox"' not in html:
    html = html.replace('</body>', js_html)

with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added lightbox code successfully.")
