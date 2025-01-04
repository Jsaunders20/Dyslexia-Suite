"""
Dyslexia-Friendly Text Editor
============================

A customizable text editor designed to assist dyslexic readers with features including:
- Adjustable font size
- Customizable line spacing
- Variable word spacing
- Vowel highlighting for easier word recognition
- Real-time preview with applied settings

Created by Jackson Saunders
GitHub: Jsaunders20

This editor uses Tkinter for the GUI and can be compiled into a standalone application 
for both Windows and macOS using PyInstaller.

Requirements:
- Python 3.x
- tkinter (usually comes with Python)
- Optional: OpenDyslexic font for optimal readability
"""

import tkinter as tk
from tkinter import ttk, font
import re

class DyslexiaEditor:
    def __init__(self, root):
        """
        Initialize the text editor with a main window and default settings.
        
        Args:
            root: The main Tkinter window
        """
        self.root = root
        self.root.title("Dyslexia-Friendly Text Editor")
        
        # Try to use OpenDyslexic font if available, otherwise fall back to Arial
        available_fonts = font.families()
        self.text_font = "Arial"  # Default fallback
        dyslexic_fonts = ["OpenDyslexic", "OpenDyslexic3"]
        for f in dyslexic_fonts:
            if f in available_fonts:
                self.text_font = f
                break
        
        # Initialize control variables
        self.font_size = tk.IntVar(value=12)
        self.line_spacing = tk.DoubleVar(value=1.5)
        self.word_spacing = tk.IntVar(value=1)
        self.highlight_vowels = tk.BooleanVar(value=False)
        
        # Set minimum window size for usability
        self.root.minsize(800, 600)
        
        self.create_widgets()
        
    def create_widgets(self):
        """Create and configure all GUI elements"""
        # Main container with padding
        main_container = ttk.Frame(self.root, padding="10")
        main_container.grid(row=0, column=0, sticky="nsew")
        
        # Controls section
        controls_frame = ttk.LabelFrame(main_container, text="Text Controls", padding="10")
        controls_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        
        # Font size slider
        ttk.Label(controls_frame, text="Font Size:").grid(row=0, column=0, padx=5)
        font_scale = ttk.Scale(
            controls_frame,
            from_=8,
            to=24,
            variable=self.font_size,
            orient="horizontal",
            command=lambda _: self.schedule_update()
        )
        font_scale.grid(row=0, column=1, padx=5)
        
        # Line spacing slider
        ttk.Label(controls_frame, text="Line Spacing:").grid(row=0, column=2, padx=5)
        line_scale = ttk.Scale(
            controls_frame,
            from_=1.0,
            to=3.0,
            variable=self.line_spacing,
            orient="horizontal",
            command=lambda _: self.schedule_update()
        )
        line_scale.grid(row=0, column=3, padx=5)
        
        # Word spacing slider
        ttk.Label(controls_frame, text="Word Spacing:").grid(row=0, column=4, padx=5)
        word_scale = ttk.Scale(
            controls_frame,
            from_=1,
            to=5,
            variable=self.word_spacing,
            orient="horizontal",
            command=lambda _: self.schedule_update()
        )
        word_scale.grid(row=0, column=5, padx=5)
        
        # Vowel highlighting toggle
        highlight_check = ttk.Checkbutton(
            controls_frame,
            text="Highlight Vowels",
            variable=self.highlight_vowels,
            command=self.schedule_update
        )
        highlight_check.grid(row=0, column=6, padx=5)
        
        # Text input area
        input_frame = ttk.LabelFrame(main_container, text="Input Text", padding="10")
        input_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        
        self.text_input = tk.Text(
            input_frame,
            wrap=tk.WORD,
            width=60,
            height=20,
            font=(self.text_font, 12)
        )
        self.text_input.grid(row=0, column=0, sticky="nsew")
        
        # Add scrollbar to input area
        input_scroll = ttk.Scrollbar(input_frame, orient="vertical", command=self.text_input.yview)
        input_scroll.grid(row=0, column=1, sticky="ns")
        self.text_input.configure(yscrollcommand=input_scroll.set)
        
        # Preview area
        preview_frame = ttk.LabelFrame(main_container, text="Preview", padding="10")
        preview_frame.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        
        self.preview = tk.Text(
            preview_frame,
            wrap=tk.WORD,
            width=60,
            height=10,
            font=(self.text_font, 12)
        )
        self.preview.grid(row=0, column=0, sticky="nsew")
        
        # Configure highlight style for vowels
        self.preview.tag_configure("vowel", foreground="blue")
        
        # Add scrollbar to preview area
        preview_scroll = ttk.Scrollbar(preview_frame, orient="vertical", command=self.preview.yview)
        preview_scroll.grid(row=0, column=1, sticky="ns")
        self.preview.configure(yscrollcommand=preview_scroll.set)
        
        # Configure grid weights for proper resizing
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        main_container.grid_columnconfigure(0, weight=1)
        main_container.grid_rowconfigure(1, weight=2)
        main_container.grid_rowconfigure(2, weight=1)
        input_frame.grid_columnconfigure(0, weight=1)
        preview_frame.grid_columnconfigure(0, weight=1)
        
        # Bind text changes to update preview
        self.text_input.bind('<KeyRelease>', self.schedule_update)
        
        # Initialize update scheduling
        self._update_pending = None
        
    def schedule_update(self, *args):
        """
        Schedule a preview update with a small delay to prevent overwhelming the system.
        This debouncing technique improves performance during rapid text entry.
        """
        if self._update_pending is not None:
            self.root.after_cancel(self._update_pending)
        self._update_pending = self.root.after(100, self.update_text_display)

    def highlight_text_vowels(self, text):
        """
        Process text to identify and mark vowels for highlighting.
        
        Args:
            text (str): The input text to process
            
        Returns:
            list: Pairs of (text_segment, is_vowel) indicating which segments to highlight
        """
        segments = []
        current = ""
        
        for char in text:
            if char.lower() in 'aeiou':
                if current:
                    segments.append((current, False))
                    current = ""
                segments.append((char, True))
            else:
                current += char
                
        if current:
            segments.append((current, False))
            
        return segments

    def update_text_display(self):
        """Update the preview text with current formatting and highlighting settings"""
        try:
            # Reset the update pending flag
            self._update_pending = None
            
            # Get current text
            text = self.text_input.get("1.0", "end-1c")
            
            # Enable preview for editing
            self.preview.configure(state='normal')
            
            # Clear preview
            self.preview.delete("1.0", tk.END)
            
            # Update font and spacing settings
            current_font_size = self.font_size.get()
            self.preview.configure(
                font=(self.text_font, current_font_size),
                spacing3=int(self.line_spacing.get() * 10),
                spacing1=int(self.line_spacing.get() * 10)
            )
            
            if text.strip():  # Only process if there's text
                words = text.split()
                for i, word in enumerate(words):
                    # Add word spacing
                    if i > 0:
                        self.preview.insert(tk.END, " " * self.word_spacing.get())
                    
                    if self.highlight_vowels.get():
                        # Process word for vowel highlighting
                        segments = self.highlight_text_vowels(word)
                        for text_segment, is_vowel in segments:
                            self.preview.insert(tk.END, text_segment, 
                                             "vowel" if is_vowel else "")
                    else:
                        # Insert word without highlighting
                        self.preview.insert(tk.END, word)
            
            # Make preview read-only
            self.preview.configure(state='disabled')
            
        except Exception as e:
            print(f"Error updating preview: {e}")

def main():
    """Initialize and run the application"""
    root = tk.Tk()
    app = DyslexiaEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
