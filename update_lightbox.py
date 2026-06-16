import re

with open('core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the old lightbox HTML and JS
old_lightbox_block = re.search(r'<!-- Lightbox Modal -->.*?</script>', html, re.DOTALL)
if old_lightbox_block:
    old_code = old_lightbox_block.group(0)
    
    new_css = """
    .lightbox-arrow {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      color: white;
      font-size: 50px;
      font-weight: bold;
      cursor: pointer;
      user-select: none;
      padding: 16px;
      transition: 0.3s;
      background: rgba(0,0,0,0.3);
      border-radius: 5px;
    }
    .lightbox-arrow:hover { background: rgba(0,0,0,0.8); }
    .lightbox-arrow.left { left: 20px; }
    .lightbox-arrow.right { right: 20px; }
    """
    
    # Inject CSS
    html = html.replace('</style>', new_css + '</style>')
    
    new_html_js = """<!-- Lightbox Modal -->
  <div id="lightbox" class="lightbox" onclick="closeLightbox(event)">
    <span class="lightbox-close" onclick="closeLightbox(event)">&times;</span>
    <div class="lightbox-arrow left" onclick="changeImage(-1, event)">&#10094;</div>
    <img id="lightbox-img" src="" onclick="event.stopPropagation()">
    <div class="lightbox-arrow right" onclick="changeImage(1, event)">&#10095;</div>
  </div>

  <script>
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    let currentImageIndex = 0;
    let galleryImages = [];
    
    // Collect all gallery image sources
    document.querySelectorAll('.g-item img').forEach((img, index) => {
      galleryImages.push(img.src);
    });
    
    // Setup click listeners for gallery
    document.querySelectorAll('.g-item').forEach((item, index) => {
      item.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        currentImageIndex = index;
        updateLightboxImage();
        lightbox.classList.add('active');
      });
    });

    function updateLightboxImage() {
      lightboxImg.src = galleryImages[currentImageIndex];
    }

    function changeImage(direction, event) {
      if(event) event.stopPropagation();
      currentImageIndex += direction;
      // Loop around
      if(currentImageIndex >= galleryImages.length) currentImageIndex = 0;
      if(currentImageIndex < 0) currentImageIndex = galleryImages.length - 1;
      updateLightboxImage();
    }

    function closeLightbox(event) {
      // Only close if clicking the background or the close button
      if(event.target === lightbox || event.target.className === 'lightbox-close') {
        lightbox.classList.remove('active');
      }
    }
  </script>"""
    
    html = html.replace(old_code, new_html_js)

    with open('core/templates/core/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated lightbox successfully!")
else:
    print("Could not find old lightbox code.")
