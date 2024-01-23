import tkinter as tk
from tkinter import filedialog
import os
import patoolib

class RarExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RAR File Extractor")

        # Create and set up the GUI elements
        self.label = tk.Label(root, text="Select a RAR file:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_rar_file)
        self.browse_button.pack(pady=10)

        self.extract_button = tk.Button(root, text="Extract", command=self.extract_rar_file)
        self.extract_button.pack(pady=10)

    def browse_rar_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("RAR files", "*.rar")])
        if file_path:
            self.rar_file_path = file_path
            self.label.config(text=f"Selected RAR file: {os.path.basename(file_path)}")

    def extract_rar_file(self):
        if hasattr(self, 'rar_file_path'):
            # Extract the RAR file to a folder with the same name as the RAR file
            output_folder = os.path.join(os.path.dirname(self.rar_file_path), os.path.splitext(os.path.basename(self.rar_file_path))[0])
            os.makedirs(output_folder, exist_ok=True)

            try:
                # Extract the RAR file to the folder
                patoolib.extract_archive(self.rar_file_path, outdir=output_folder)
                tk.messagebox.showinfo("Success", "Extraction complete!")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Extraction failed:\n{str(e)}")
        else:
            tk.messagebox.showwarning("Warning", "Please select a RAR file first.")

if __name__ == "__main__":
    root = tk.Tk()

    # Set the minimum size of the window
    root.minsize(400, 200)

    # Set the initial size of the window
    root.geometry("500x250")

    app = RarExtractorApp(root)
    root.mainloop()
