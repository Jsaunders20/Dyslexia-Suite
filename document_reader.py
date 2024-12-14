"""
Simple Document Reader with Text-to-Speech
A basic application that reads PDFs and text documents aloud.
"""

import tkinter as tk
from tkinter import ttk, filedialog
import pyttsx3
import PyPDF2
import os
from threading import Thread
import queue
from docx import Document

class DocumentReader:
    def __init__(self, root):
        self.root = root
        self.root.title("Document Reader")
        
        # Initialize variables first
        self.rate = tk.IntVar(value=150)
        self.volume = tk.DoubleVar(value=1.0)
        self.is_reading = False
        self.text_queue = queue.Queue()
        
        # Configure main window
        self.root.geometry("800x600")
        
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', self.rate.get())
        self.engine.setProperty('volume', self.volume.get())
        
        # Set up the UI last
        self.setup_ui()
        
    def setup_ui(self):
        """Create and configure the user interface"""
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Create file selection button
        select_button = ttk.Button(
            main_frame,
            text="Select File (PDF, TXT, or DOCX)",
            command=self.select_file
        )
        select_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        
        # Create controls frame
        controls_frame = ttk.LabelFrame(main_frame, text="Controls", padding="10")
        controls_frame.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        
        # Speech rate control
        ttk.Label(controls_frame, text="Speed:").grid(row=0, column=0, padx=5)
        rate_scale = ttk.Scale(
            controls_frame,
            from_=50,
            to=300,
            variable=self.rate,
            orient="horizontal",
            command=self.update_rate
        )
        rate_scale.grid(row=0, column=1, padx=5, sticky="ew")
        
        # Volume control
        ttk.Label(controls_frame, text="Volume:").grid(row=0, column=2, padx=5)
        volume_scale = ttk.Scale(
            controls_frame,
            from_=0.0,
            to=1.0,
            variable=self.volume,
            orient="horizontal",
            command=self.update_volume
        )
        volume_scale.grid(row=0, column=3, padx=5, sticky="ew")
        
        # Control buttons
        self.play_button = ttk.Button(controls_frame, text="Play", command=self.toggle_reading)
        self.play_button.grid(row=0, column=4, padx=5)
        
        stop_button = ttk.Button(controls_frame, text="Stop", command=self.stop_reading)
        stop_button.grid(row=0, column=5, padx=5)
        
        # Text preview
        preview_frame = ttk.LabelFrame(main_frame, text="Text Preview", padding="10")
        preview_frame.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        
        self.text_preview = tk.Text(preview_frame, wrap=tk.WORD, height=10)
        self.text_preview.grid(row=0, column=0, sticky="nsew")
        
        # Add scrollbar to preview
        preview_scroll = ttk.Scrollbar(preview_frame, orient="vertical", command=self.text_preview.yview)
        preview_scroll.grid(row=0, column=1, sticky="ns")
        self.text_preview.configure(yscrollcommand=preview_scroll.set)
        
        # Configure grid weights
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        preview_frame.grid_columnconfigure(0, weight=1)
        preview_frame.grid_rowconfigure(0, weight=1)
        controls_frame.grid_columnconfigure(1, weight=1)
        controls_frame.grid_columnconfigure(3, weight=1)
        
    def select_file(self):
        """Open file dialog to select a file"""
        try:
            file_types = [
                ('PDF files', '*.pdf'),
                ('Text files', '*.txt'),
                ('Word Documents', '*.docx'),
                ('All files', '*.*')
            ]
            
            file_path = filedialog.askopenfilename(
                title='Choose a file',
                filetypes=file_types,
                initialdir=os.path.expanduser('~')  # Start in user's home directory
            )
            
            if file_path:
                self.process_file(file_path)
        except Exception as e:
            print(f"Error in file selection: {e}")
            self.text_preview.delete(1.0, tk.END)
            self.text_preview.insert(tk.END, f"Error selecting file: {str(e)}")
            
    def process_file(self, file_path):
        """Extract text from the file based on its type"""
        try:
            text = ""
            ext = os.path.splitext(file_path)[1].lower()
            
            if ext == '.pdf':
                with open(file_path, 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    for page in pdf_reader.pages:
                        text += page.extract_text() + "\n"
                        
            elif ext == '.txt':
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read()
                    
            elif ext == '.docx':
                doc = Document(file_path)
                text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
                
            # Update preview and queue text for reading
            self.text_preview.delete(1.0, tk.END)
            self.text_preview.insert(tk.END, text)
            self.text_queue.put(text)
            
        except Exception as e:
            self.text_preview.delete(1.0, tk.END)
            self.text_preview.insert(tk.END, f"Error processing file: {str(e)}")
            
    def update_rate(self, *args):
        """Update speech rate"""
        try:
            rate = int(self.rate.get())  # Convert to integer explicitly
            self.engine.stop()  # Stop any current speech
            self.engine = pyttsx3.init()  # Reinitialize the engine
            self.engine.setProperty('rate', rate)
            self.engine.setProperty('volume', self.volume.get())
        except Exception as e:
            print(f"Error updating rate: {e}")
        
    def update_volume(self, *args):
        """Update speech volume"""
        try:
            volume = float(self.volume.get())  # Convert to float explicitly
            self.engine.stop()  # Stop any current speech
            self.engine = pyttsx3.init()  # Reinitialize the engine
            self.engine.setProperty('volume', volume)
            self.engine.setProperty('rate', self.rate.get())
        except Exception as e:
            print(f"Error updating volume: {e}")
        
    def toggle_reading(self):
        """Start or pause reading"""
        if not self.is_reading:
            self.is_reading = True
            self.play_button.configure(text="Pause")
            Thread(target=self.read_text, daemon=True).start()
        else:
            self.is_reading = False
            self.play_button.configure(text="Play")
            
    def stop_reading(self):
        """Stop reading and reset"""
        self.is_reading = False
        self.play_button.configure(text="Play")
        try:
            self.engine.stop()
        except Exception as e:
            print(f"Error stopping engine: {e}")
        
    def read_text(self):
        """Read text from the queue"""
        try:
            text = self.text_queue.get_nowait()
        except queue.Empty:
            text = self.text_preview.get(1.0, tk.END)
            
        if text.strip():
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                print(f"Error reading text: {e}")
            finally:
                self.is_reading = False
                self.play_button.configure(text="Play")

def main():
    root = tk.Tk()
    app = DocumentReader(root)
    root.mainloop()

if __name__ == "__main__":
    main()