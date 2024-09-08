
# Summarizer Web Application

This project is a web-based Text Summarization tool built using Flask and Spacy NLP library. Users can input text, select a word reduction ratio, and get a summarized version of their text. The web interface is styled with Bootstrap and custom CSS for a visually appealing user experience.

## Features 🌟
- Input Text: Enter your text in a large input box that supports scrolling for long content. 📝
- Summary Generation: Get the summarized version of your input text with selectable word reduction ratios (1/2, 1/3, 1/5, or 1/10). 🧾
- Word Count Display: The word count of both the original and summarized texts is shown for easy comparison. 🔢
- Clean Design: Styled with Bootstrap and custom CSS for a clean and intuitive user experience. 🎨

## Technologies Used 🛠️
- Backend: Python, Flask
- Text Summarization: Spacy NLP library
- Frontend: HTML, CSS (Bootstrap, Custom Styles)

## Setup
1. Clone the repository:

```
git clone https://github.com/rjasra/TextSummarizer/tree/main
cd text-summarizer
```
2. Install the required dependencies:

```
pip install -r requirements.txt
```
3. Download the Spacy model used for text processing:
```
python -m spacy download en_core_web_sm
```
4. Run the Flask application:
```
python app.py
```
5. Open your browser and go to http://127.0.0.1:5000/. 🌐

## Project Structure 🗂️
```
├── app.py                # Flask application
├── text_summary.py        # Summarizer logic with Spacy
├── templates
│   ├── index.html        # Home page
│   ├── summary.html      # Summary result page
├── static
│   ├── style.css         # Custom styles
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
```
## Screenshots 📸
### Home Page

The Home page allows users to input text and select a word reduction ratio. (Lets say we want to reduce word length by 1/2 here)

![image](https://github.com/user-attachments/assets/b40da029-2ed5-442d-9b06-a02ffdb6713a)

### Summary Page

After submission, the summarized text will be displayed alongside the original text.

![image](https://github.com/user-attachments/assets/18322c62-b84a-4b60-a3f4-314e9fa55ff6)

