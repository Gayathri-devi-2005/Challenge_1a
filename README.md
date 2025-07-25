# Adobe Round 1A – PDF Outline Extractor

This project extracts hierarchical outlines (e.g., H1, H2, H3 level headings) from PDF documents using Python and PyMuPDF. It outputs a structured JSON showing the document title, outline, and corresponding page numbers.

---

## 📁 Folder Structure

```
adobe_round1a_starter/
├── main.py              # PDF outline extractor script
├── Dockerfile           # Docker setup file (as per Adobe format)
├── requirements.txt     # Required Python packages
├── README.md            # This file
├── input/               # Folder to place input PDF files
│   └── sample.pdf       # Sample input file for testing
├── output/              # JSON outputs will be saved here
│   └── sample.json      # Output generated from sample.pdf
```

---

## 🐳 Docker Instructions (As Per Adobe)

### 🛠 Build the Docker image

```bash
docker build --platform linux/amd64 -t pdf_outline_extractor .
```

### 🚀 Run the Docker container

```bash
docker run --rm \
  -v ${PWD}/input:/app/input \
  -v ${PWD}/output:/app/output \
  --network none pdf_outline_extractor
```

> 📌 Replace `${PWD}` with `%cd%` if you're using CMD on Windows, or use `${PWD}` in PowerShell or Linux.

---

## 📤 How It Works

1. The program scans every PDF in the `input/` folder.
2. For each PDF, it detects headings based on font size and style.
3. It outputs a JSON file in the `output/` folder with:
   - The title (from filename)
   - A list of heading sections and their page numbers

---

## ✅ Sample Output Format

```json
{
  "title": "sample",
  "outline": [
    {
      "level": "H1",
      "text": "1. Introduction to Machine Learning",
      "page": 0
    },
    {
      "level": "H2",
      "text": "1.1 Supervised Learning",
      "page": 1
    }
  ]
}
```

---

## 👩‍💻 Author

Gayathri Devi Yaragarla  
Adobe Connecting the Dots Hackathon – Round 1A  
July 2025
