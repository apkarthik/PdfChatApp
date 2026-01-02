# Quick Start Guide

Get started with PDF Chat App in 5 minutes!

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Set Up Your API Key

Copy the example environment file and add your OpenAI API key:

```bash
cp .env.example .env
```

Edit `.env` and replace `your_openai_api_key_here` with your actual OpenAI API key.

**Don't have an API key?** Get one at: https://platform.openai.com/api-keys

## 3. Add PDF Files

Place your PDF files in the `pdfs` folder:

```bash
# The pdfs folder already exists
ls pdfs/
```

Copy or move your PDF files into this folder.

## 4. Run the App

```bash
chainlit run app.py
```

The app will automatically:
- Open in your browser at http://localhost:8000
- Load and process your PDF files
- Display a ready message when complete

## 5. Start Chatting!

Type your questions in the chat and press Enter. Examples:

- "What is this document about?"
- "Summarize the main points"
- "What does it say about [specific topic]?"

The AI will answer based on your PDF content and show you which file and page the information came from.

## Troubleshooting

### Command not found: chainlit
If you get this error, chainlit may not be in your PATH. Try:
```bash
python -m chainlit run app.py
```

### No PDF files found
Make sure:
- PDF files are in the `pdfs` folder
- Files have `.pdf` extension
- You restart the app after adding files

### API Key Issues
Check that:
- You copied the API key correctly (no extra spaces)
- The API key is valid and has credits
- The `.env` file is in the same folder as `app.py`

## Need More Help?

See the full [README.md](README.md) for detailed information.
