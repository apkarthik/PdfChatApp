#!/bin/bash

# Setup script for PDF Chat App

echo "🚀 Setting up PDF Chat App..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and add your OpenAI API key!"
    echo "   Get your API key from: https://platform.openai.com/api-keys"
else
    echo "✅ .env file already exists"
fi

# Create pdfs folder if it doesn't exist
if [ ! -d pdfs ]; then
    mkdir -p pdfs
    echo "📁 Created pdfs folder"
else
    echo "✅ pdfs folder already exists"
fi

echo ""
echo "✨ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env and add your OpenAI API key"
echo "2. Add PDF files to the 'pdfs' folder"
echo "3. Run: chainlit run app.py"
echo ""
echo "For detailed instructions, see README.md or QUICKSTART.md"
