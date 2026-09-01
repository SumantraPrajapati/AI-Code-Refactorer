# AI Code Refactorer

An AI-powered code refactoring application that analyzes source code and generates cleaner, more readable, maintainable, and efficient versions using **Qwen3-Coder** and **LangChain**.

The application provides a simple **Streamlit interface** where users can upload source-code files and get an AI-refactored version of their code.

---

## Features

* Upload source-code files directly through the UI
*  Supports multiple programming languages
*  AI-powered code refactoring using Qwen3-Coder
*  Automatic programming-language detection based on file extension
*  Improves code readability and maintainability
*  Suggests structural and efficiency improvements
*  Displays original and refactored code
*  Download the refactored source code
*  Cached LLM initialization using Streamlit
*  Built using LangChain's LCEL pipeline

---

## Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Application development         |
| Streamlit     | Web interface                   |
| LangChain     | LLM orchestration               |
| Hugging Face  | Model inference                 |
| Qwen3-Coder   | Code analysis and refactoring   |
| Pydantic      | Data validation                 |
| python-dotenv | Environment variable management |

---

##  Architecture

```text
                   ┌────────────────────┐
                   │      User          │
                   │  Uploads Source    │
                   │       Code         │
                   └─────────┬──────────┘
                             │
                             ▼
                   ┌────────────────────┐
                   │ Language Detection │
                   │   File Extension   │
                   └─────────┬──────────┘
                             │
                             ▼
                   ┌────────────────────┐
                   │   PromptTemplate   │
                   │                    │
                   │ Code + Language    │
                   └─────────┬──────────┘
                             │
                             ▼
                   ┌────────────────────┐
                   │    Qwen3-Coder     │
                   │  Hugging Face LLM  │
                   └─────────┬──────────┘
                             │
                             ▼
                   ┌────────────────────┐
                   │  Output Parser     │
                   │   String Output    │
                   └─────────┬──────────┘
                             │
                             ▼
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
      Refactored Code                 Download File
```

---

##  Supported Languages

The application supports a wide range of common programming and scripting languages

---

##  Project Structure

```text
Code-Refactorer/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---
## Prerequisites
HuggingFace API Token 

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/SumantraPrajapati/AI-Code-Refactorer.git
cd Code-Refactorer
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

For CMD:

```cmd
.venv\Scripts\activate.bat
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install streamlit
pip install langchain
pip install langchain-core
pip install langchain-huggingface
pip install huggingface-hub
pip install python-dotenv
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
```

Never commit your `.env` file to GitHub.

Add this to `.gitignore`:

```text
.env
.venv/
__pycache__/
*.pyc
```

---

## Run the Application

Start Streamlit:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---


## LangChain Pipeline

The core application uses LangChain's LCEL pipeline:

```python
chain = prompt | model | parser
```

Conceptually:

```text
PromptTemplate
      ↓
ChatHuggingFace
      ↓
Qwen3-Coder
      ↓
StrOutputParser
      ↓
Refactored Code
```

The uploaded source code is passed dynamically:

```python
result = chain.invoke({
    "code": code,
    "language": language_name
})
```

---

## Future Improvements

This project is currently focused on AI-powered code refactoring. Future versions can extend it into a complete AI code analysis platform.

### Static Code Analysis

Integrate language-specific tools:

```text
Python     → AST / Ruff / Pylint
JavaScript → ESLint
C++        → Clang-Tidy
Java       → Checkstyle / SpotBugs
Go         → go vet / staticcheck
Rust       → Clippy
```

### Automated Testing

Generate and execute tests automatically:

```text
Original Code
      ↓
Generate Tests
      ↓
Run Tests
      ↓
Refactor
      ↓
Run Tests Again
      ↓
Compare Results
```

###  Agentic Architecture

Introduce specialized tools/agents:

```text
                 AI Code Agent
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
   Code Analyzer   Bug Detector   Refactorer
        │              │              │
        └──────────────┼──────────────┘
                       ↓
                  Test Runner
                       │
                       ↓
                  Validator
```

---

## Limitations

AI-generated refactoring should **not be blindly trusted**.

The model may:

* Misinterpret intended behavior
* Introduce subtle bugs
* Miss language-specific issues
* Make unnecessary changes
* Produce incorrect optimizations

For production usage, generated code should be validated using:

* Compilers
* Linters
* Static analyzers
* Unit tests
* Integration tests
* Sandboxed execution

---

## Security

Do not upload sensitive source code containing:

* API keys
* Passwords
* Private credentials
* Database credentials
* Private certificates
* Proprietary source code

Never commit secrets to the repository.

---

##  Roadmap

* [x] Multi-language file upload
* [x] Automatic language detection
* [x] AI-powered refactoring
* [x] Refactored code preview
* [x] Download refactored code
* [ ] Syntax validation
* [ ] Static code analysis
* [ ] Automated test generation
* [ ] Test execution
* [ ] Code quality scoring
* [ ] Security analysis
* [ ] Agentic workflow
* [ ] GitHub repository integration
* [ ] Docker support
* [ ] Production deployment

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

## License

This project is open-source.

---



## Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
