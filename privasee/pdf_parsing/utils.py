import fitz
import os

def extract_text_info_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text_info = []
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if block["type"] == 0:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text_info.append({
                            "page_num": page_num,
                            "size": span["size"],
                            "text": span["text"]
                        })
    return text_info

def split_pdf_by_title(pdf_path, output_dir, min_font_size=20):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    text_info = extract_text_info_from_pdf(pdf_path)
    document = fitz.open(pdf_path)
    split_indices = [0]

    for info in text_info:
        if info["size"] >= min_font_size and info["text"].strip().startswith("Article "):
            print(f"Large text detected on page {info['page_num'] + 1}: '{info['text'].strip()}' with size {info['size']}")
            if info["page_num"] not in split_indices:
                split_indices.append(info["page_num"])
    
    split_indices.append(len(document))

    print(f"Split indices: {split_indices}")

    for i in range(len(split_indices) - 1):
        start = split_indices[i]
        end = split_indices[i + 1]
        if start < end:
            split_doc = fitz.open()
            split_doc.insert_pdf(document, from_page=start, to_page=end - 1)
            output_file = os.path.join(output_dir, f"article_{i+1}.pdf")
            split_doc.save(output_file)
            print(f"Saved split document: {output_file}")
    
    print(f"PDF split into {len(split_indices) - 1}")

def convert_pdf_to_txt(pdf_path, txt_path):
    document = fitz.open(pdf_path)
    
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text = page.get_text("text")
            txt_file.write(text)
            txt_file.write("\n\n")

def convert_all_pdfs_in_directory(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        
    for filename in os.listdir(input_directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_directory, filename)
            txt_path = os.path.join(output_directory, filename.replace(".pdf", ".txt"))
            convert_pdf_to_txt(pdf_path, txt_path)
            print(f"Converted {filename} to {filename.replace('.pdf', '.txt')}")
