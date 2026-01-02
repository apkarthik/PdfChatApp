# Example Usage

This document shows example conversations and use cases for the PDF Chat App.

## Example 1: Simple Question

**User:** What is the main topic of these documents?

**Bot:** Based on the PDF documents you've provided, the main topic is... [answer based on actual PDFs]

📚 **Sources:**
- document1.pdf (Page 1)
- document2.pdf (Page 3)

## Example 2: Specific Information

**User:** What does the document say about machine learning?

**Bot:** The documents mention machine learning in the context of... [detailed answer]

📚 **Sources:**
- technical_report.pdf (Page 15)
- technical_report.pdf (Page 18)

## Example 3: Summarization

**User:** Can you summarize the key findings?

**Bot:** The key findings from the documents are:
1. [Finding 1]
2. [Finding 2]
3. [Finding 3]

[Detailed explanation]

📚 **Sources:**
- research_paper.pdf (Page 7)
- research_paper.pdf (Page 12)

## Example 4: Comparison

**User:** How do these documents compare in their approaches?

**Bot:** The documents take different approaches:
- Document A focuses on...
- Document B emphasizes...
[Detailed comparison]

📚 **Sources:**
- document_a.pdf (Page 5)
- document_b.pdf (Page 3)

## Tips for Better Results

### Ask Specific Questions
❌ "Tell me about this"
✅ "What are the main recommendations in the report?"

### Use Context from Previous Messages
The bot remembers your conversation history, so you can:
1. Ask an initial question
2. Follow up with "Can you elaborate on that?"
3. Ask "What else does it mention about this topic?"

### Reference Multiple Documents
✅ "Compare the findings across all documents"
✅ "What do all the reports say about X?"

### Ask for Evidence
✅ "Which specific sections discuss this?"
✅ "Can you quote the relevant part?"

## Common Use Cases

### 📚 Research
- Analyze multiple research papers
- Extract key findings
- Compare methodologies
- Find specific citations

### 📄 Reports
- Summarize long reports
- Extract action items
- Find specific data points
- Compare recommendations

### 📖 Documentation
- Search technical documentation
- Find specific procedures
- Understand concepts
- Locate examples

### 📋 Legal/Contracts
- Search for specific clauses
- Understand terms
- Compare documents
- Extract key dates and obligations

### 📊 Business Documents
- Analyze financial reports
- Extract metrics
- Compare quarterly results
- Find specific information

## Advanced Tips

### Multi-turn Conversations
Build on previous questions:
```
You: What products are mentioned?
Bot: [Lists products]

You: Tell me more about product A
Bot: [Detailed info about product A]

You: How does it compare to product B?
Bot: [Comparison]
```

### Asking for Specific Formats
- "List the key points as bullet points"
- "Create a summary table"
- "Explain this in simple terms"
- "Give me a step-by-step guide"

### Verifying Information
- "Which page mentions this?"
- "Are you sure about that?"
- "Show me the exact quote"
- "What's your confidence level?"

## Limitations

### What the App Can Do
✅ Answer questions based on text in PDFs
✅ Provide source citations
✅ Remember conversation history
✅ Handle multiple PDFs simultaneously

### What the App Cannot Do
❌ Read scanned images (need OCR preprocessing)
❌ Understand charts/graphs without text
❌ Access information outside the PDFs
❌ Generate information not in the documents

## Best Practices

1. **Quality PDFs**: Use text-based PDFs, not scanned images
2. **Descriptive Names**: Give PDFs meaningful filenames
3. **Organized Content**: Group related PDFs together
4. **Clear Questions**: Be specific about what you want to know
5. **Verify Critical Info**: For important decisions, verify the sources
6. **Restart for New Docs**: Restart the app when adding new PDFs

## Troubleshooting Common Issues

### Bot gives generic answers
- Check that your PDFs loaded correctly
- Look at the initial loading message for errors
- Ensure PDFs contain actual text (not just images)

### Bot can't find information
- Try rephrasing your question
- Ask more specific questions
- Check if that information exists in the PDFs

### Sources are wrong
- This is rare but can happen
- Always verify critical information from the source PDFs
- Report unusual behavior

## Getting the Most Out of the App

1. Start with a broad question to understand what's in the docs
2. Ask follow-up questions to drill down
3. Request summaries for overview
4. Ask for specific details when needed
5. Use the conversation history to your advantage
6. Check the sources to verify information

---

**Need Help?** See [README.md](README.md) for setup and configuration or [QUICKSTART.md](QUICKSTART.md) for quick start guide.
