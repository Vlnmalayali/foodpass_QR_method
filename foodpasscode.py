import os
from PIL import Image

# Settings — adjust if your filenames or paths change
background_image_path = "pass.jpg"
qr_images_dir = "Qr_Images"  # Directory with all QR images (place your QR files here)
output_dir = "Output"
os.makedirs(output_dir, exist_ok=True)

# Load the template background
background = Image.open(background_image_path).convert("RGBA")

# White box position and size (tuned for your template, adjust if needed)
box_x, box_y = 300, 560
box_w, box_h = 510, 510

# Process each QR image in your QR folder
for qr_filename in os.listdir(qr_images_dir):
    if qr_filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        qr_path = os.path.join(qr_images_dir, qr_filename)
        qr_img = Image.open(qr_path).convert("RGBA")
        
        # Resize the QR to fit the white box exactly
        qr_img = qr_img.resize((box_w, box_h))
        
        # Prepare composite by copying the background
        composed = background.copy()
        composed.paste(qr_img, (box_x, box_y), qr_img)
        
        # Output filename will match the QR image name
        out_path = os.path.join(output_dir, os.path.splitext(qr_filename)[0] + ".png")
        composed.save(out_path)

print("Food passes have been generated with QR codes correctly placed!")
