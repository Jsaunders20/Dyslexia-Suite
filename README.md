# Dyslexia Accessibility Tools

A suite of applications designed to make reading and writing more accessible for individuals with dyslexia. This repository contains two main applications:

## 1. Dyslexia-Friendly Text Editor

A customizable text editor that provides real-time text formatting with features specifically chosen to enhance readability for dyslexic users.

### Features

- **Adjustable Font Size:** Scale text from 8pt to 24pt for optimal readability
- **Customizable Line Spacing:** Adjust the space between lines to reduce text crowding
- **Variable Word Spacing:** Control the spacing between words to prevent text from running together
- **Vowel Highlighting:** Optional blue highlighting of vowels to make word recognition easier
- **Real-time Preview:** See all formatting changes instantly in a preview pane
- **OpenDyslexic Font Support:** Automatically uses OpenDyslexic font if installed

## 2. Document Reader with Text-to-Speech

A complementary application that reads documents aloud, supporting various file formats and offering customizable reading settings.

### Features

- **Multiple File Format Support:** 
  - PDF files (.pdf)
  - Text files (.txt)
  - Word Documents (.docx)
- **Adjustable Reading Speed:** Control the pace of text-to-speech
- **Volume Control:** Easily adjust the reading volume
- **Text Preview:** View document contents before and during reading
- **Simple Controls:** Play, pause, and stop functionality
- **File Selection:** Easy-to-use file picker for selecting documents

## Installation

### Prerequisites
- Python 3.x
- tkinter (usually comes with Python)
- Optional: OpenDyslexic font for optimal readability

### Installing Dependencies
```bash
pip install pyttsx3 PyPDF2 python-docx
```

### Running from Source
1. Clone this repository:
```bash
git clone https://github.com/Jsaunders20/dyslexia-tools.git
cd dyslexia-tools
```

2. Run either application:
```bash
# For the text editor
python dyslexia_editor.py

# For the document reader
python document_reader.py
```

### Creating Standalone Applications

#### For macOS:
```bash
# Install PyInstaller
pip install pyinstaller

# Create the text editor application
pyinstaller --windowed --name DyslexiaEditor --noconfirm dyslexia_editor.py

# Create the document reader application
pyinstaller --windowed --name DocumentReader --noconfirm document_reader.py
```

#### For Windows:
```bash
# Install PyInstaller
pip install pyinstaller

# Create the applications
pyinstaller --onefile --windowed --name DyslexiaEditor dyslexia_editor.py
pyinstaller --onefile --windowed --name DocumentReader document_reader.py
```

The applications will be available in the `dist` folder.

## Usage

### Text Editor
1. Launch DyslexiaEditor
2. Type or paste text into the upper text area
3. Use the sliders to adjust:
   - Font size
   - Line spacing
   - Word spacing
4. Toggle vowel highlighting with the checkbox
5. View the formatted text in the preview pane

### Document Reader
1. Launch DocumentReader
2. Click "Select File" and choose a document
3. Adjust reading speed and volume using the sliders
4. Use Play/Pause and Stop buttons to control reading
5. View document text in the preview pane

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License

## Acknowledgments

- OpenDyslexic font project for providing an accessible typeface
- Research on dyslexia-friendly text formatting that informed this project's features
- Text-to-speech technology that makes document reading more accessible

## Contact

Jackson Saunders - Jsaunders20@fordham.edu

Project Link: https://github.com/Jsaunders20/dyslexia-tools

## Future Improvements

- [ ] Add support for additional dyslexic-friendly fonts
- [ ] Implement more text formatting options
- [ ] Add support for more document formats
- [ ] Create options to save and load custom presets
- [ ] Add export options for formatted text
- [ ] Implement batch processing for multiple documents
- [ ] Add support for different languages and accents
- [ ] Create a unified interface for both tools

## Citation

If you use this software in your research, please cite:

```
Saunders, J. (2024). Dyslexia Accessibility Tools [Computer software]. 
https://github.com/Jsaunders20/dyslexia-tools
```
