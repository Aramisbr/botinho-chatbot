# Botinho: Your Intelligent Document Assistant 🤖

Botinho is a versatile chatbot built with Python, Flask, and LangChain, designed to help you extract information and chat with various document sources like YouTube videos, PDF files, and websites through an intuitive web interface.

## ✨ Features

* **Interactive Chat Interface:** User-friendly web UI built with Flask.
* **YouTube Video Processing:** Provide a YouTube URL, and Botinho will transcribe the video (using Faster Whisper) and answer based on content.
* **PDF Document Querying:** Upload your PDF files and ask Botinho questions based on their text.
* **Website Content Extraction:** Give Botinho a website URL, and it will fetch the content and discuss it with you.
* **Conversation History:** Keeps track of your ongoing conversation with Botinho.
* **Dynamic Document Loading:** Easily switch context by loading new documents via the UI.
* **Modular Loaders:** Cleanly separated Python modules for handling different document sources.

## 🛠️ Technologies & Libraries Used

* **Backend:** Python, Flask
* **Core AI & LLM Orchestration:** LangChain
* **Language Model Interaction:** OpenAI (from LangChain)
* **Speech-to-Text (YouTube):** Faster Whisper
* **YouTube Downloader:** `yt-dlp`
* **PDF Processing:** `PyPDFLoader` (from LangChain)
* **Web Content Fetching:** `WebBaseLoader`(from LangChain)
* **Frontend:** HTML, CSS (for UI interactions like toggling panels)
* **Version Control:** Git, GitHub

## 📂 Project Structure (Simplified)

botinho-chatbot/
├── app.py                  # Main Flask application
├── chatbot/
│   └── botinho.py          # Core LangChain chat logic
├── loaders/
│   ├── youtube_loader.py   # YouTube content extraction
│   ├── pdf_loader.py       # PDF content extraction
│   └── site_loader.py      # Website content extraction
├── static/
│   └── style.css           # CSS for styling
├── templates/
│   └── index.html          # Main HTML page for the chat interface
├── temp_pdf_uploads/       # Temporary storage for uploaded PDFs
├── audios/                 # Temporary storage for downloaded audio
├── .env                    # For API keys
├── .env.example            # Example for environment variables
├── requirements.txt        # Python dependencies
├── .gitignore              # Untracked files
├── LICENSE                 # MIT License
└── README.md               # This file


## 🚀 Getting Started

Follow these instructions to set up and run Botinho on your local machine.

### Prerequisites

* Python 3.8+ installed.
* `pip` (Python package installer) installed.
* Git installed.
* FFmpeg: Essential for processing audio from YouTube videos.
    * **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html) (e.g., gyan.dev builds), extract, and ensure the `bin` folder is added to your system's PATH.
    * **macOS:** `brew install ffmpeg`
    * **Linux (Debian/Ubuntu):** `sudo apt update && sudo apt install ffmpeg`

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Aramisbr/botinho-chatbot.git
    cd botinho-chatbot
    ```

2.  **Create and activate a Python virtual environment:**
    * Highly recommended to keep project dependencies isolated.
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    * Ensure you have a `requirements.txt` file listing all necessary Python packages.
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have `requirements.txt` yet, create it from your activated virtual environment after installing packages: `pip freeze > requirements.txt`)*

4.  **Set up Environment Variables (API Key):**
    * Botinho uses the OpenAI API. You'll need an API key.
    * Copy the example environment file:
        ```bash
        cp .env.example .env
        ```
    * Open the `.env` file in a text editor and replace the placeholder with your actual OpenAI API key:
        ```
        OPENAI_API_KEY="your_actual_openai_api_key_here"
        ```
    * **Important:** The `.env` file should **NEVER** be committed to GitHub. Ensure `.env` is listed in your `.gitignore` file. The `.env.example` file *can* be committed as it only shows the structure.

### How to Run

1.  Ensure your virtual environment is activated.
2.  Make sure all dependencies from `requirements.txt` are installed.
3.  Run the Flask application from the project root directory:
    ```bash
    python app.py
    ```
4.  Open your web browser and navigate to: `http://127.0.0.1:5000/`

## 🎯 Future Improvements / To-Do

* [ ] Implement asynchronous processing for YouTube transcription to improve UX for longer videos.
* [ ] Allow direct audio file uploads (e.g., MP3, WAV) for transcription.
* [ ] Implement a "Restart Chat" button to clear history and context.
* [ ] Further enhance UI/UX based on user feedback.

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
*(GitHub will create the `LICENSE` file for you if you selected "MIT License" during repository creation).*

---