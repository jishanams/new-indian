from PIL import Image, ImageChops

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return im

try:
    img = Image.open('static/title.png')
    
    # Try converting to RGBA if not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
        
    # Get the bounding box of non-transparent/non-white pixels
    # Since it might have a white background, we need to handle that.
    # To reliably crop white space:
    bg = Image.new('RGBA', img.size, (255,255,255,255))
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    
    if bbox:
        cropped_img = img.crop(bbox)
        # Add a tiny 2% padding so it's not totally flush against the edge
        padding = int(max(cropped_img.size) * 0.05)
        new_size = (cropped_img.width + 2*padding, cropped_img.height + 2*padding)
        padded_img = Image.new('RGBA', new_size, (255,255,255,0))
        padded_img.paste(cropped_img, (padding, padding))
        padded_img.save('static/title.png')
        print("Successfully cropped image.")
    else:
        print("Could not find bounding box.")
except Exception as e:
    print(f"Error: {e}")
