@echo off
REM Setup script for PDF Chat App (Windows)

echo 🚀 Setting up PDF Chat App...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    exit /b 1
)

echo ✅ Python found
python --version
echo.

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Create .env file if it doesn't exist
if not exist .env (
    echo 📝 Creating .env file...
    copy .env.example .env
    echo.
    echo ⚠️  IMPORTANT: Edit .env and add your OpenAI API key!
    echo    Get your API key from: https://platform.openai.com/api-keys
) else (
    echo ✅ .env file already exists
)

REM Create pdfs folder if it doesn't exist
if not exist pdfs (
    mkdir pdfs
    echo 📁 Created pdfs folder
) else (
    echo ✅ pdfs folder already exists
)

echo.
echo ✨ Setup complete!
echo.
echo Next steps:
echo 1. Edit .env and add your OpenAI API key
echo 2. Add PDF files to the 'pdfs' folder
echo 3. Run: chainlit run app.py
echo.
echo For detailed instructions, see README.md or QUICKSTART.md
echo.
pause
