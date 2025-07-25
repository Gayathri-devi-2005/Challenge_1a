import fitz  # PyMuPDF
import os
import json

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    title = os.path.splitext(os.path.basename(pdf_path))[0]
    outline = []

    for page_num, page in enumerate(doc, start=1):
        actual_page_num = page_num - 1  # Shift to 0-based numbering
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    text = " ".join([span["text"] for span in line["spans"]])
                    font_size = line["spans"][0]["size"]

                    # Simple rule-based classifier
                    if font_size >= 16:
                        level = "H1"
                    elif font_size >= 13:
                        level = "H2"
                    elif font_size >= 11:
                        level = "H3"
                    else:
                        continue

                    outline.append({
                        "level": level,
                        "text": text.strip(),
                        "page": actual_page_num  # Use 0-based page number
                    })

    return {
        "title": title,
        "outline": outline
    }

# Main function to scan input folder
if __name__ == "__main__":
    input_dir = "./input"
    output_dir = "./output"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename.replace(".pdf", ".json"))

            result = extract_outline(pdf_path)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)
