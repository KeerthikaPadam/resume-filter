import os
import pandas as pd
from tkinter import Tk, Label, Button, Listbox, Scrollbar, END, filedialog, messagebox, Frame, StringVar, Entry, Canvas
import PyPDF2  # For extracting text from PDFs
from PIL import Image, ImageTk  # For adding icons/images
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to parse resumes and extract text
def parse_resume(file_path):
    try:
        # Extract text from the PDF using PyPDF2
        with open(file_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return {
            "name": os.path.basename(file_path).split(".")[0],  # Use file name as candidate name
            "text": text,                                       # Store the full extracted text
            "file_path": file_path                               # Store file path for reference
        }
    except Exception as e:
        messagebox.showerror("Error", f"Failed to parse {file_path}: {str(e)}")
        return None

# Function to filter resumes based on user-entered keywords
def filter_resumes(resumes, keywords):
    if not keywords:  # If no keywords are specified, return all resumes
        return resumes
    filtered = []
    for resume in resumes:
        if all(keyword.lower() in resume["text"].lower() for keyword in keywords):
            filtered.append(resume)
    return filtered

# Batch export filtered resumes to a CSV file
def export_to_csv(filtered_resumes):
    try:
        if not filtered_resumes:
            messagebox.showwarning("No Data", "No filtered resumes to export.")
            return

        # Create a DataFrame from the filtered resumes
        df = pd.DataFrame(filtered_resumes)

        # Open a file dialog to save the CSV file
        export_file = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")]
        )
        if not export_file:  # If the user cancels the dialog, do nothing
            return

        # Export the DataFrame to a CSV file
        df.to_csv(export_file, index=False)
        messagebox.showinfo("Success", f"Exported {len(filtered_resumes)} resumes to {export_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to export resumes: {str(e)}")

# GUI Application
class ResumeFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume Filtering Tool")
        self.root.geometry("1000x700")
        self.resumes = []  # List to store parsed resumes
        self.resume_frames = []  # List to track frames for uploaded resumes

        # Add a background color for the main window
        self.root.configure(bg="#f0f0f0")

        # Header Section
        header_frame = Frame(self.root, bg="#4CAF50", pady=20)
        header_frame.pack(fill="x")
        Label(header_frame, text="Resume Filtering Tool", font=("Arial", 20, "bold"), fg="white", bg="#4CAF50").pack()

        # Input for required keywords
        input_frame = Frame(self.root, bg="#f0f0f0", pady=10)
        input_frame.pack(fill="x", padx=20)
        Label(input_frame, text="Enter Keywords (comma-separated):", font=("Arial", 14), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.keyword_entry = Entry(input_frame, width=50, font=("Arial", 12))
        self.keyword_entry.grid(row=0, column=1, padx=10, pady=10)

        # Buttons for uploading single resume or folder
        button_frame = Frame(self.root, bg="#f0f0f0", pady=10)
        button_frame.pack(fill="x", padx=20)
        Button(button_frame, text="Upload Single Resume", command=self.upload_single_resume, bg="#008CBA", fg="white", font=("Arial", 12)).grid(
            row=0, column=0, padx=10, pady=10, sticky="ew"
        )
        Button(button_frame, text="Upload Folder of Resumes", command=self.upload_folder, bg="#008CBA", fg="white", font=("Arial", 12)).grid(
            row=0, column=1, padx=10, pady=10, sticky="ew"
        )

        # Frame to display uploaded resumes dynamically
        self.uploaded_frame = Frame(self.root, bg="#ffffff", pady=10)
        self.uploaded_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Button to filter resumes
        Button(self.root, text="Filter Resumes", command=self.filter_resumes_gui, bg="#f44336", fg="white", font=("Arial", 14)).pack(
            fill="x", padx=20, pady=10
        )

        # Listbox to display filtered resumes
        self.filtered_listbox = Listbox(self.root, width=80, height=10, font=("Arial", 12), bg="#ffffff")
        self.filtered_listbox.pack(fill="both", expand=True, padx=20, pady=10)
        scrollbar_filtered = Scrollbar(self.root, orient="vertical", command=self.filtered_listbox.yview)
        scrollbar_filtered.pack(side="right", fill="y", padx=10)
        self.filtered_listbox.config(yscrollcommand=scrollbar_filtered.set)

        # Diagram Section
        self.diagram_frame = Frame(self.root, bg="#f0f0f0", pady=20)
        self.diagram_frame.pack(fill="x", padx=20)

        # Button to export filtered resumes
        Button(self.root, text="Export Filtered Resumes", command=self.export_filtered, bg="#4CAF50", fg="white", font=("Arial", 14)).pack(
            fill="x", padx=20, pady=10
        )

    def upload_single_resume(self):
        # Use askopenfilename to allow single file selection
        file_path = filedialog.askopenfilename(
            title="Select Resume",
            filetypes=[("PDF Files", "*.pdf")]
        )
        if file_path:
            # Parse the resume and add it to the list
            resume_data = parse_resume(file_path)
            if resume_data:
                self.resumes.append(resume_data)
                # Create a frame for the uploaded resume
                self.add_resume_to_ui(resume_data)
            messagebox.showinfo("Success", f"Uploaded 1 resume.")

    def upload_folder(self):
        # Use askdirectory to allow folder selection
        folder_path = filedialog.askdirectory(title="Select Folder Containing Resumes")
        if folder_path:
            # Get all PDF files in the folder
            pdf_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".pdf")]
            if not pdf_files:
                messagebox.showwarning("No PDFs Found", "The selected folder does not contain any PDF files.")
                return
            # Parse each PDF file
            for file_path in pdf_files:
                resume_data = parse_resume(file_path)
                if resume_data:
                    self.resumes.append(resume_data)
                    # Create a frame for the uploaded resume
                    self.add_resume_to_ui(resume_data)
            messagebox.showinfo("Success", f"Uploaded {len(pdf_files)} resumes from the folder.")

    def add_resume_to_ui(self, resume_data):
        # Create a frame for the uploaded resume
        resume_frame = Frame(self.uploaded_frame, bg="#ffffff", pady=5, highlightbackground="#cccccc", highlightthickness=1)
        resume_frame.pack(fill="x", pady=5)
        # Display the resume name with an icon
        try:
            icon = Image.open("resume_icon.png")  # Replace with your own resume icon
            icon = icon.resize((20, 20))
            icon = ImageTk.PhotoImage(icon)
            icon_label = Label(resume_frame, image=icon, bg="#ffffff")
            icon_label.image = icon  # Keep a reference to avoid garbage collection
            icon_label.pack(side="left", padx=5)
        except FileNotFoundError:
            pass
        Label(resume_frame, text=os.path.basename(resume_data["file_path"]), font=("Arial", 12), bg="#ffffff").pack(side="left", padx=5)
        # Add an "X" button to delete the resume
        delete_button = Button(resume_frame, text="X", fg="red", bg="#ffffff", command=lambda rf=resume_frame, rd=resume_data: self.delete_resume(rf, rd))
        delete_button.pack(side="right", padx=5)
        # Track the frame for future reference
        self.resume_frames.append(resume_frame)

    def delete_resume(self, resume_frame, resume_data):
        # Remove the resume from the list
        self.resumes.remove(resume_data)
        # Destroy the frame displaying the resume
        resume_frame.destroy()
        # Remove the frame from the tracking list
        self.resume_frames.remove(resume_frame)
        messagebox.showinfo("Deleted", f"Resume deleted: {resume_data['name']}")

    def filter_resumes_gui(self):
        # Get the keywords entered by the user
        keywords_input = self.keyword_entry.get().strip()
        if not keywords_input:
            messagebox.showwarning("No Keywords", "Please enter at least one keyword.")
            return
        keywords = [keyword.strip() for keyword in keywords_input.split(",") if keyword.strip()]
        # Filter resumes based on the entered keywords
        filtered = filter_resumes(self.resumes, keywords)
        self.filtered_resumes = filtered
        # Display filtered resumes in the filtered listbox
        self.filtered_listbox.delete(0, END)
        for resume in filtered:
            self.filtered_listbox.insert(END, f"{resume['name']} - File: {resume['file_path']}")
        if not keywords:
            messagebox.showinfo("Filter Complete", f"No keywords specified. Displaying all {len(filtered)} resumes.")
        else:
            messagebox.showinfo("Filter Complete", f"Found {len(filtered)} matching resumes.")
        # Update the diagram
        self.update_diagram(len(self.resumes), len(filtered))

    def update_diagram(self, total_resumes, filtered_resumes):
        # Clear previous diagram
        for widget in self.diagram_frame.winfo_children():
            widget.destroy()
        # Create a simple bar chart
        fig, ax = plt.subplots(figsize=(5, 2))
        ax.bar(["Total Resumes", "Filtered Resumes"], [total_resumes, filtered_resumes], color=["#008CBA", "#f44336"])
        ax.set_title("Resume Statistics", fontsize=12)
        ax.set_ylabel("Count", fontsize=10)
        canvas = FigureCanvasTkAgg(fig, master=self.diagram_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def export_filtered(self):
        if hasattr(self, "filtered_resumes"):
            export_to_csv(self.filtered_resumes)
        else:
            messagebox.showwarning("No Data", "No filtered resumes to export.")

# Run the application
if __name__ == "__main__":
    root = Tk()
    app = ResumeFilterApp(root)
    root.mainloop()
