# thumbgen

**thumbgen** is a lightweight Python tool to **bulk-generate image thumbnails from a PowerPoint template**.

## ✅ Quick Example

Input file: `video_links.txt`  
Template: `template.pptx` with a text box labeled `"Change here"`

```
Video Title 1
Video Title 2
Video Title 3
```

### To generate thumbnails:

```bash
./run_thumbgen.sh
```

Or run manually:

```bash
thumbgen \
  --input_file video_links.txt \
  --template_path template.pptx \
  --output_dir thumbnails \
  --text_box_name "Change here"
```

---

## ⚙️ Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
brew install --cask libreoffice
```

> Add LibreOffice to PATH (if needed):  
> `export PATH="/Applications/LibreOffice.app/Contents/MacOS:$PATH"`

---

## 🖌 Optional CLI Flags

```bash
--text_color     black | white (default: white)
--font_size      Integer (default: 16)
```

Example:

```bash
thumbgen ... --text_color black --font_size 24
```

---

## 📄 Script: `run_thumbgen.sh`

```bash
#!/bin/bash
source venv/bin/activate
export PATH="/Applications/LibreOffice.app/Contents/MacOS:$PATH"
pip install -e .
thumbgen \
  --input_file video_links.txt \
  --template_path template.pptx \
  --output_dir thumbnails \
  --text_box_name "Change here"
```

Make it executable:

```bash
chmod +x run_thumbgen.sh
```

---

## 🪪 License

MIT License
