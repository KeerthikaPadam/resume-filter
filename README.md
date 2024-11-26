
# Resume Filter

A simple web application for filtering uploaded PDF resumes based on specific keywords. Users can upload up to 5 resumes and input keywords to search for in the resumes. The app processes the PDF files, extracts text, and filters resumes that match the provided keywords.

## Features
- Upload up to 5 PDF resumes.
- Enter comma-separated keywords for filtering.
- Displays the list of resumes that contain all the entered keywords.
- The tool uses PDF.js to extract text from PDF files.

## Prerequisites

- A modern web browser (Google Chrome, Mozilla Firefox, etc.)
- Internet connection for loading PDF.js from CDN

## Files Included
- `index.html`: The main HTML file containing the structure and functionality.
- `styles.css`: Basic styling for the page layout.
- `script.js`: JavaScript file for handling PDF extraction, filtering, and displaying results.

## Usage

### 1. Upload PDF Resumes
- Click the **"Upload File 1"**, **"Upload File 2"**, ..., **"Upload File 5"** buttons to select PDF files from your local machine. A maximum of 5 PDF files can be uploaded.

### 2. Enter Keywords
- In the "Enter Keywords" field, type a comma-separated list of keywords to filter the resumes (e.g., `Python, Machine Learning`).

### 3. Filter Resumes
- Click the **"Filter Resumes"** button to filter the uploaded resumes based on the entered keywords.
- The app will display a list of resumes that contain all the entered keywords.

### 4. Results
- The matching resumes are displayed below the button, with the file names listed.

## How It Works

1. **PDF.js Integration**: The app uses the [PDF.js](https://mozilla.github.io/pdf.js/) library to extract text from the uploaded PDF files.
2. **Text Extraction**: The text from each PDF is extracted page by page.
3. **Keyword Matching**: Each extracted text is compared with the entered keywords, and resumes that match all keywords are displayed.
   
## Installation

1. **Clone the repository** or download the project files:
   ```bash
   git clone https://github.com/your-username/resume-filter.git
   ```

2. Open the `index.html` file in a browser to use the tool.

## Libraries Used

- [PDF.js](https://mozilla.github.io/pdf.js/) for extracting text from PDF files.
- Basic HTML5, CSS, and JavaScript.

## Troubleshooting

- **PDF.js library not loading**: Ensure you have an active internet connection as the library is loaded from a CDN.
- **No matching resumes**: Ensure the keywords are entered correctly and match the content within the resumes. The keywords are case-insensitive.
  
## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

## License

This project is open-source and available under the [MIT License](LICENSE).

