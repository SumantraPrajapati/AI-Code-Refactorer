import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser , StrOutputParser
from pydantic import BaseModel

load_dotenv()

st.set_page_config(
    page_title = "AI Code Refractorer",
    page_icon = "🧹",
    layout = "wide"
)

LANGUAGE_MAP = {

    "py": {
        "name": "Python",
        "highlight": "python",
        "mime": "text/x-python"
    },


    "js": {
        "name": "JavaScript",
        "highlight": "javascript",
        "mime": "text/javascript"
    },

    "jsx": {
        "name": "JavaScript React",
        "highlight": "jsx",
        "mime": "text/jsx"
    },

    "ts": {
        "name": "TypeScript",
        "highlight": "typescript",
        "mime": "text/typescript"
    },

    "tsx": {
        "name": "TypeScript React",
        "highlight": "tsx",
        "mime": "text/tsx"
    },

 
    "c": {
        "name": "C",
        "highlight": "c",
        "mime": "text/x-c"
    },

    "h": {
        "name": "C Header",
        "highlight": "c",
        "mime": "text/plain"
    },

    "cpp": {
        "name": "C++",
        "highlight": "cpp",
        "mime": "text/x-c++src"
    },

    "cc": {
        "name": "C++",
        "highlight": "cpp",
        "mime": "text/x-c++src"
    },

    "cxx": {
        "name": "C++",
        "highlight": "cpp",
        "mime": "text/x-c++src"
    },

    "hpp": {
        "name": "C++ Header",
        "highlight": "cpp",
        "mime": "text/plain"
    },


    "java": {
        "name": "Java",
        "highlight": "java",
        "mime": "text/x-java-source"
    },

    "kt": {
        "name": "Kotlin",
        "highlight": "kotlin",
        "mime": "text/plain"
    },

    "kts": {
        "name": "Kotlin Script",
        "highlight": "kotlin",
        "mime": "text/plain"
    },

    "scala": {
        "name": "Scala",
        "highlight": "scala",
        "mime": "text/plain"
    },

    "groovy": {
        "name": "Groovy",
        "highlight": "groovy",
        "mime": "text/plain"
    },


    "cs": {
        "name": "C#",
        "highlight": "csharp",
        "mime": "text/plain"
    },


    "go": {
        "name": "Go",
        "highlight": "go",
        "mime": "text/plain"
    },


    "rs": {
        "name": "Rust",
        "highlight": "rust",
        "mime": "text/plain"
    },


    "swift": {
        "name": "Swift",
        "highlight": "swift",
        "mime": "text/plain"
    },


    "dart": {
        "name": "Dart",
        "highlight": "dart",
        "mime": "text/plain"
    },

    "php": {
        "name": "PHP",
        "highlight": "php",
        "mime": "text/plain"
    },

  
    "rb": {
        "name": "Ruby",
        "highlight": "ruby",
        "mime": "text/x-ruby"
    },


    "r": {
        "name": "R",
        "highlight": "r",
        "mime": "text/plain"
    },


    "m": {
        "name": "MATLAB",
        "highlight": "matlab",
        "mime": "text/plain"
    },

 
    "jl": {
        "name": "Julia",
        "highlight": "julia",
        "mime": "text/plain"
    },

    "lua": {
        "name": "Lua",
        "highlight": "lua",
        "mime": "text/plain"
    },


    "pl": {
        "name": "Perl",
        "highlight": "perl",
        "mime": "text/plain"
    },


    "sh": {
        "name": "Shell",
        "highlight": "bash",
        "mime": "text/x-shellscript"
    },

    "bash": {
        "name": "Bash",
        "highlight": "bash",
        "mime": "text/x-shellscript"
    },

    "zsh": {
        "name": "Zsh",
        "highlight": "bash",
        "mime": "text/x-shellscript"
    },

    "ps1": {
        "name": "PowerShell",
        "highlight": "powershell",
        "mime": "text/plain"
    },

    "bat": {
        "name": "Batch",
        "highlight": "batch",
        "mime": "text/plain"
    },

    "cmd": {
        "name": "Windows CMD",
        "highlight": "batch",
        "mime": "text/plain"
    },

    "sql": {
        "name": "SQL",
        "highlight": "sql",
        "mime": "application/sql"
    },


    "html": {
        "name": "HTML",
        "highlight": "html",
        "mime": "text/html"
    },

    "htm": {
        "name": "HTML",
        "highlight": "html",
        "mime": "text/html"
    },

    "css": {
        "name": "CSS",
        "highlight": "css",
        "mime": "text/css"
    },

    "scss": {
        "name": "SCSS",
        "highlight": "scss",
        "mime": "text/plain"
    },

    "sass": {
        "name": "Sass",
        "highlight": "sass",
        "mime": "text/plain"
    },

    "less": {
        "name": "Less",
        "highlight": "less",
        "mime": "text/plain"
    },

    "m": {
        "name": "Objective-C",
        "highlight": "objective-c",
        "mime": "text/plain"
    },

    "mm": {
        "name": "Objective-C++",
        "highlight": "objective-cpp",
        "mime": "text/plain"
    },


    "ex": {
        "name": "Elixir",
        "highlight": "elixir",
        "mime": "text/plain"
    },

    "exs": {
        "name": "Elixir",
        "highlight": "elixir",
        "mime": "text/plain"
    },

    "erl": {
        "name": "Erlang",
        "highlight": "erlang",
        "mime": "text/plain"
    },


    "hs": {
        "name": "Haskell",
        "highlight": "haskell",
        "mime": "text/plain"
    },


    "clj": {
        "name": "Clojure",
        "highlight": "clojure",
        "mime": "text/plain"
    },

    "fs": {
        "name": "F#",
        "highlight": "fsharp",
        "mime": "text/plain"
    },

    "fsx": {
        "name": "F# Script",
        "highlight": "fsharp",
        "mime": "text/plain"
    },


    "vb": {
        "name": "Visual Basic",
        "highlight": "vbnet",
        "mime": "text/plain"
    },


    "sol": {
        "name": "Solidity",
        "highlight": "solidity",
        "mime": "text/plain"
    },


    "asm": {
        "name": "Assembly",
        "highlight": "asm",
        "mime": "text/plain"
    },

    "s": {
        "name": "Assembly",
        "highlight": "asm",
        "mime": "text/plain"
    },

    "f": {
        "name": "Fortran",
        "highlight": "fortran",
        "mime": "text/plain"
    },

    "f90": {
        "name": "Fortran",
        "highlight": "fortran",
        "mime": "text/plain"
    },

    "f95": {
        "name": "Fortran",
        "highlight": "fortran",
        "mime": "text/plain"
    },

    "cob": {
        "name": "COBOL",
        "highlight": "cobol",
        "mime": "text/plain"
    },
    
    "pro": {
        "name": "Prolog",
        "highlight": "prolog",
        "mime": "text/plain"
    },


    "solidity": {
        "name": "Solidity",
        "highlight": "solidity",
        "mime": "text/plain"
    },


    "json": {
        "name": "JSON",
        "highlight": "json",
        "mime": "application/json"
    },

    "xml": {
        "name": "XML",
        "highlight": "xml",
        "mime": "application/xml"
    },

    "yaml": {
        "name": "YAML",
        "highlight": "yaml",
        "mime": "text/yaml"
    },

    "yml": {
        "name": "YAML",
        "highlight": "yaml",
        "mime": "text/yaml"
    },

    "toml": {
        "name": "TOML",
        "highlight": "toml",
        "mime": "text/plain"
    },


    "md": {
        "name": "Markdown",
        "highlight": "markdown",
        "mime": "text/markdown"
    }
}

def detect_language(filename):
    extension = filename.split(".")[-1].lower()
    return LANGUAGE_MAP.get(extension,
                            {
                                "name":"Unknown",
                                "highlight":"text"
                            })

@st.cache_resource
def load_model():
    llm = HuggingFaceEndpoint(
        repo_id="Qwen/Qwen3-Coder-30B-A3B-Instruct",
        task="conversational",
        max_new_tokens=1024,
        temperature=0.2
    )

    return ChatHuggingFace(llm=llm)


model = load_model()

prompt = PromptTemplate(
    template="""
You are an expert code refactoring engine.

Analyze and refactor the following {language} code.

You MUST follow this exact format:

BUG:
<each real defect found, or exactly NONE if there are none>

EXPLANATION:
<what you changed, or "No changes required" if the code is already correct>

REFACTORED_CODE:
<complete code, raw, with no markdown fences>

IMPROVEMENTS:
<one bullet per change you actually made, or exactly NONE>

Rules:
- A bug is ONLY: a crash, a wrong result, a resource leak, a security issue, or undefined behavior.
- Missing features, missing tests, missing error handling for impossible inputs, or
  "this code does nothing useful" are NOT bugs. Never report them.
- If the code is already correct, write BUG: NONE and return the code unchanged.
- Never invent defects. Never add features or suggest new functionality.
- Never change public APIs, signatures, or behavior.
- Do not provide multiple solutions.
- Preserve the intended behavior.
- Always provide the complete refactored code.
- Do not add any text before BUG: and no text after the improvements.

CODE:

{code}
""",
    input_variables=['code', 'language'],
)

parser = StrOutputParser()

chain = prompt | model | parser


st.title("AI Code Refactorer")

st.write(
    "Upload source code and let AI Improve its"
    "readability , maintainability and structure"
)

uploaded_file = st.file_uploader(
    "Upload your source code",
    type=[
        "py",
        "js",
        "jsx",
        "ts",
        "tsx",
        "java",
        "cpp",
        "cc",
        "cxx",
        "c",
        "cs",
        "go",
        "rs",
        "php",
        "rb",
        "swift",
        "kt",
        "kts",
        "scala",
        "sh",
        "bash",
        "sql",
        "html",
        "css"
    ]
)

if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")
    
    language = detect_language(
        uploaded_file.name
    )
    language_name = language["name"]
    language_highlight = language["highlight"]
    language_mime = language["mime"]
    
    st.success(
        f"Detected Language:{language_name}"
    )
    st.subheader("Original Code")
    
    st.code(
        code,
        language =  language_highlight
    )

    if st.button(
        "Refactor Code",
        type = 'primary'
    ):
        with st.spinner("AI is refactoring your code..."):
            try:
                result = chain.invoke({
                    "code":code,
                    "language": language_name
                })
                
                st.subheader("Refactored Code")
                st.code(
                    result,
                    language = language_highlight
                )
                
                st.download_button(
                    label = "Download Refactored Code",
                    data = result,
                    file_name = f"refactored_{uploaded_file.name}",
                    mime = language_mime
                )
                
            except  UnicodeDecodeError:
                st.error(
                    "Could not read this file"
                    "Please upload a UTF-8 encoded source file "
                )
                
            except Exception as e:
                st.error (
                    f"Something went wrong:\n\n{str(e)}"
                )


