import fitz  # PyMuPDF
import os
from datetime import datetime, timedelta
from glob import glob


def extract_all_images(pdf_path, out_dir="../extracted_pictograms"):
    """
    Extracts all images from the first page of a PDF and saves them
    to a structured directory.
    """

    print(f"Processing: {pdf_path}")
    os.makedirs(out_dir, exist_ok=True)

    # Open PDF
    doc = fitz.open(pdf_path)
    page = doc[0]  # first page
    image_list = page.get_images(full=True)

    print(f"  Found {len(image_list)} images on page 1")

    # Prepare output folder
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    pdf_folder = os.path.join(out_dir, base_name)

    os.makedirs(pdf_folder, exist_ok=True)

    if not image_list:
        print("  No images found.")
        return

    # Extract all images
    for idx, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        ext = base_image["ext"]

        # Output name
        img_filename = os.path.join(pdf_folder, f"image_{idx+1}.{ext}")

        # Save image
        with open(img_filename, "wb") as f:
            f.write(image_bytes)

        print(f"  Saved: {img_filename}")

    print("Done.\n")

# Example usage
def extract_data():
    extract_all_images("./2019/01/2019_01_01.pdf")

# Example usage
if __name__ == "__main__":
    extract_data()