from PIL import Image

# File paths
input_file = r"C:\Users\Rahul Kumar\Desktop\apple.webp"  # Input WEBP file
output_jpg = r"C:\Users\Rahul Kumar\Desktop\apple.jpg"  # Output JPG file
output_png = r"C:\Users\Rahul Kumar\Desktop\apple.png"  # Output PNG file

try:
    # Open the WEBP image
    img = Image.open(input_file).convert("RGB")  # Convert to RGB for JPG/PNG

    # Save as JPG
    img.save(output_jpg, "JPEG", quality=95)
    print(f"✅ Converted WEBP to JPG: {output_jpg}")

    # Save as PNG
    img.save(output_png, "PNG")
    print(f"✅ Converted WEBP to PNG: {output_png}")

except FileNotFoundError:
    print(f"❌ Error: File not found at {input_file}")
except Exception as e:
    print(f"❌ An error occurred: {e}")
