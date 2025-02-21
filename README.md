# Resume Filtering Tool

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green) ![PyPDF2](https://img.shields.io/badge/PyPDF2-PDF%20Parsing-orange)

The **Resume Filtering Tool** is a Python-based desktop application that helps recruiters and hiring managers filter resumes based on user-defined keywords. It supports uploading individual resumes or entire folders of resumes, extracting text from PDFs, filtering based on keywords, and exporting filtered results as a CSV file.

---

## Features

- **Upload Resumes**: Upload single PDF files or entire folders containing resumes.
- **Keyword-Based Filtering**: Filter resumes based on user-entered keywords (e.g., "Python", "SQL", "Machine Learning").
- **Export Results**: Export filtered resumes as a CSV file for further analysis.
- **Visual Dashboard**: Includes a bar chart showing the total number of resumes vs. filtered resumes.
- **User-Friendly Interface**: Built with `tkinter` for an intuitive graphical user interface (GUI).

---

## Installation

### Prerequisites

1. **Python 3.x**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **Required Libraries**: Install the required libraries using `pip`.

```bash
pip install PyPDF2 pandas matplotlib pillow
```

### Clone the Repository

To clone this repository, run the following command:

```bash
git clone https://github.com/your-username/resume-filtering-tool.git
cd resume-filtering-tool
```

---

## Usage

1. **Run the Application**:
   - Navigate to the project directory and execute the script:

     ```bash
     python resume_filter_tool.py
     ```

2. **Upload Resumes**:
   - Use the "Upload Single Resume" button to upload individual PDF files.
   - Use the "Upload Folder of Resumes" button to upload an entire folder of PDF files.

3. **Enter Keywords**:
   - In the input box, type the keywords you want to filter by (e.g., `Python, SQL, Machine Learning`).

4. **Filter Resumes**:
   - Click the "Filter Resumes" button to filter resumes based on the entered keywords.

5. **Export Filtered Resumes**:
   - Click the "Export Filtered Resumes" button to save the filtered results as a CSV file.

---

## Project Structure

```
resume-filtering-tool/
├── resume_filter_tool.py       # Main application script
├── resume_icon.png             # Icon for uploaded resumes (optional)
├── README.md                   # Documentation file
└── requirements.txt            # List of required Python libraries
```

---

## Screenshots

### Main Interface
![Main Interface](screenshots/main_interface.png)

### Filtered Resumes
![Filtered Resumes](screenshots/filtered_resumes.png)

*(Replace the above image links with actual screenshots of your application.)*

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **PyPDF2**: For extracting text from PDF files.
- **Tkinter**: For building the GUI.
- **Matplotlib**: For creating visualizations.
- **Pillow**: For handling images/icons in the GUI.

---

## Contact

If you have any questions or suggestions, feel free to reach out:

- Email: kusumakeerthi.padam@gmail.com
- GitHub: [Your GitHub Profile](https://github.com/KeerthikaPadam)

