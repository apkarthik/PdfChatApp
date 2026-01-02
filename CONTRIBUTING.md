# Contributing to PDF Chat App

Thank you for your interest in contributing to PDF Chat App! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, etc.)
- Any relevant error messages or logs

### Suggesting Features

Feature suggestions are welcome! Please:
- Check if the feature has already been requested
- Clearly describe the feature and its use case
- Explain why it would be valuable

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature/fix
3. Make your changes
4. Test your changes thoroughly
5. Update documentation if needed
6. Submit a pull request

#### Code Style

- Follow PEP 8 style guidelines for Python
- Add comments for complex logic
- Keep functions focused and single-purpose
- Use meaningful variable and function names

#### Testing

- Test your changes locally before submitting
- Ensure existing functionality still works
- Test with different types of PDF files

### Areas for Contribution

We welcome contributions in these areas:

#### Features
- Support for additional document formats (DOCX, TXT, etc.)
- OCR support for scanned PDFs
- Multiple language support
- Advanced search and filtering
- Export chat history
- Custom chunking strategies

#### Documentation
- Improve installation guides
- Add more examples
- Create video tutorials
- Translate documentation

#### Code Quality
- Add unit tests
- Improve error handling
- Optimize performance
- Refactor complex code

#### UI/UX
- Improve Chainlit interface
- Add custom styling
- Better mobile support
- Accessibility improvements

## Development Setup

1. Fork and clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Make your changes
5. Test locally:
   ```bash
   chainlit run app.py
   ```

## Questions?

If you have questions about contributing, feel free to:
- Open an issue with your question
- Start a discussion in GitHub Discussions

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn and grow

Thank you for contributing! 🎉
