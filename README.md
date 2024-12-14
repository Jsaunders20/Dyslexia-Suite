# Dyslexia-Friendly Text Editor

A customizable text editor designed to make reading and writing more accessible for individuals with dyslexia. This application provides real-time text formatting with features specifically chosen to enhance readability for dyslexic users.

## Features

- **Adjustable Font Size:** Scale text from 8pt to 24pt for optimal readability
- **Customizable Line Spacing:** Adjust the space between lines to reduce text crowding
- **Variable Word Spacing:** Control the spacing between words to prevent text from running together
- **Vowel Highlighting:** Optional blue highlighting of vowels to make word recognition easier
- **Real-time Preview:** See all formatting changes instantly in a preview pane
- **OpenDyslexic Font Support:** Automatically uses OpenDyslexic font if installed

## Installation

### Prerequisites
- Python 3.x
- tkinter (usually comes with Python)
- Optional: OpenDyslexic font for optimal readability

### Running from Source
1. Clone this repository:
```bash
git clone https://github.com/[YourUsername]/dyslexia-editor.git
cd dyslexia-editor
```

2. Run the application:
```bash
python dyslexia_editor.py
```

### Creating a Standalone Application

#### For macOS:
```bash
# Install PyInstaller
pip install pyinstaller

# Create the application
pyinstaller --windowed --name DyslexiaEditor --noconfirm dyslexia_editor.py
```
The application will be available in the `dist` folder.

#### For Windows:
```bash
# Install PyInstaller
pip install pyinstaller

# Create the executable
pyinstaller --onefile --windowed --name DyslexiaEditor --noconfirm dyslexia_editor.py
```
The executable will be available in the `dist` folder.

## Usage

1. Launch the application
2. Type or paste text into the upper text area
3. Use the sliders to adjust:
   - Font size
   - Line spacing
   - Word spacing
4. Toggle vowel highlighting with the checkbox
5. View the formatted text in the preview pane below

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License 

## Acknowledgments

- OpenDyslexic font project for providing an accessible typeface
- Research on dyslexia-friendly text formatting that informed this project's features

## Contact

Jackson Saunders - Jsaunders20@fordham.edu

Project Link: https://github.com/Jsaunders20/dyslexia-editor

## Future Improvements

- [ ] Add support for additional dyslexia-friendly fonts
- [ ] Implement text-to-speech functionality
- [ ] Add color theme options for different visual preferences
- [ ] Create options to save and load custom presets
- [ ] Add export options for formatted text

## Citation

If you use this software in your research, please cite:

```
Saunders, J. (2024). Dyslexia-Friendly Text Editor [Computer software]. 
https://github.com/[YourUsername]/dyslexia-editor
```
