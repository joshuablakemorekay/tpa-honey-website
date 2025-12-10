"""
Extract images from TPA Farm PDF
"""
import fitz  # PyMuPDF
import os

def extract_images_from_pdf(pdf_path, output_dir):
    """Extract all images from PDF"""
    print(f"Extracting images from {pdf_path}...")
    
    # Open PDF
    pdf_document = fitz.open(pdf_path)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    image_count = 0
    
    # Iterate through pages
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        image_list = page.get_images()
        
        print(f"Page {page_num + 1}: Found {len(image_list)} images")
        
        # Extract each image
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            # Save image
            image_filename = f"product_{page_num + 1}_{img_index + 1}.{image_ext}"
            image_path = os.path.join(output_dir, image_filename)
            
            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)
            
            print(f"  Saved: {image_filename}")
            image_count += 1
    
    pdf_document.close()
    print(f"\nTotal images extracted: {image_count}")
    return image_count

if __name__ == "__main__":
    pdf_path = "/mnt/user-data/uploads/TPA_Farm.pdf"
    output_dir = "/home/claude/tpa_honey_website/static/images"
    
    extract_images_from_pdf(pdf_path, output_dir)
