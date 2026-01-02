# PDF Chat App 🤖📄

A simple and intuitive chatbot application that allows you to chat with your PDF documents using AI. Built with [Chainlit](https://chainlit.io/) and powered by OpenAI's language models.

## Features

- 📁 Automatically loads all PDF files from a designated folder
- 💬 Natural conversation interface for asking questions about your documents
- 🔍 Intelligent context-aware responses with source citations
- 🚀 Simple setup and easy to use
- 💾 Persistent vector database for fast retrieval

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (get one at https://platform.openai.com/api-keys)

## Installation

### Quick Setup (Recommended)

For the fastest setup, use the provided setup scripts:

**On macOS/Linux:**
```bash
./setup.sh
```

**On Windows:**
```bash
setup.bat
```

The setup script will:
- Create a virtual environment
- Install all dependencies
- Create the `.env` file for you to add your API key
- Create the `pdfs` folder

**Then:**
1. Edit `.env` and add your OpenAI API key
2. Add PDF files to the `pdfs` folder
3. Run: `chainlit run app.py`

See [QUICKSTART.md](QUICKSTART.md) for a quick start guide.

### Manual Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/apkarthik/PdfChatApp.git
   cd PdfChatApp
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```

## Usage

### Step 1: Add Your PDF Files

1. The app will automatically create a `pdfs` folder when you first run it
2. Place all your PDF files in the `pdfs` folder
3. You can add multiple PDF files - the app will process all of them

### Step 2: Start the Application

Run the Chainlit app:
```bash
chainlit run app.py
```

The app will:
- Automatically open in your default browser at `http://localhost:8000`
- Load and process all PDF files from the `pdfs` folder
- Create a vector database for efficient searching
- Display a ready message when everything is loaded

### Step 3: Chat with Your PDFs

1. Type your question in the chat input at the bottom
2. Press Enter or click the send button
3. The AI will analyze your PDFs and provide an answer with source citations
4. Continue the conversation - the app remembers your chat history!

### Example Questions

- "What is the main topic of these documents?"
- "Can you summarize the key points?"
- "What does the document say about [specific topic]?"
- "Are there any recommendations mentioned?"

## Configuration

You can customize the app by modifying the `.env` file:

- **OPENAI_MODEL**: Change the AI model (default: `gpt-3.5-turbo`)
  - For better quality: `gpt-4`
  - For faster/cheaper: `gpt-3.5-turbo`

- **OPENAI_EMBEDDING_MODEL**: Change the embedding model (default: `text-embedding-ada-002`)

## Project Structure

```
PdfChatApp/
├── app.py                 # Main Chainlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment variables
├── .env                  # Your environment variables (create this)
├── .gitignore           # Git ignore file
├── README.md            # This file
├── pdfs/                # Folder for your PDF files (auto-created)
└── chroma_db/           # Vector database (auto-created)
```

## How It Works

1. **Document Loading**: The app reads all PDF files from the `pdfs` folder
2. **Text Extraction**: Extracts text content from each page of the PDFs
3. **Chunking**: Splits the text into smaller chunks for better processing
4. **Embeddings**: Creates vector embeddings using OpenAI's embedding model
5. **Vector Store**: Stores embeddings in a Chroma database for fast retrieval
6. **Question Answering**: When you ask a question:
   - Finds the most relevant chunks from your PDFs
   - Sends them to the AI model along with your question
   - Generates an accurate answer with source citations

## Troubleshooting

### No PDF files found
- Make sure you've placed PDF files in the `pdfs` folder
- Check that the files have a `.pdf` extension
- Restart the app after adding new files

### API Key Error
- Verify your OpenAI API key is correct in the `.env` file
- Ensure you have credits available in your OpenAI account
- Check that there are no extra spaces in the API key

### Memory Issues with Large PDFs
- If processing large PDFs, the initial load may take some time
- Consider splitting very large PDFs into smaller files
- The vector database is persistent, so subsequent starts are faster

### Port Already in Use
- If port 8000 is already in use, you can specify a different port:
  ```bash
  chainlit run app.py --port 8001
  ```

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Chainlit](https://chainlit.io/)
- Powered by [LangChain](https://www.langchain.com/)
- Uses [OpenAI](https://openai.com/) models
- Vector storage by [Chroma](https://www.trychroma.com/)

## Support

If you encounter any issues or have questions:
1. Check the Troubleshooting section above
2. Review existing GitHub issues
3. Create a new issue with detailed information about your problem

---

**Happy chatting with your PDFs! 📄💬**