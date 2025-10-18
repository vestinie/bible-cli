# 📖 Bible CLI

![Tests](https://github.com/vestinie/bible-cli/workflows/Tests/badge.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)

A professional command-line interface for fetching Bible verses, built with Python and developed using AI assistance.

## ✨ Features

- 📜 **Fetch specific verses** - Get any Bible verse by reference
- 🎲 **Random verses** - Discover scripture with random verse generation
- 📚 **Full chapters** - Read entire chapters at once
- 🔍 **Search functionality** - Find verses by keyword
- 🌍 **Multiple translations** - Support for different Bible translations (default: KJV)
- ✅ **Fully tested** - Comprehensive test suite with mocked API calls
- 🚀 **CI/CD enabled** - Automated testing with GitHub Actions

## 🚀 Quick Start

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/vestinie/bible-cli.git
cd bible-cli
```

2. **Create and activate a virtual environment (recommended)**

**Windows:**
```bash
py -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**
```bash
py -m pip install -r requirements.txt
```

## 📋 Usage

**Note:** All commands use the King James Version (KJV) translation by default. Use `--translation` or `-t` to specify a different version.

### Get a Specific Verse
```bash
py -m src.main verse "John 3:16"
```

**Output:**
```
📖 John 3:16 (King James Version)

For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life.
```

### Get a Random Verse
```bash
py -m src.main random
```

### Read an Entire Chapter
```bash
py -m src.main chapter "Psalm 23"
```

### Search for Verses
```bash
py -m src.main search "love" --limit 3
```

### Use Different Translations
```bash
py -m src.main verse "John 3:16" --translation niv
py -m src.main random -t esv
```

## 🔧 Commands Overview

| Command | Description | Example |
|---------|-------------|---------|
| `verse` | Fetch a specific Bible verse | `py -m src.main verse "John 3:16"` |
| `random` | Get a random Bible verse | `py -m src.main random` |
| `chapter` | Read an entire chapter | `py -m src.main chapter "Psalm 23"` |
| `search` | Search verses by keyword | `py -m src.main search "love" --limit 5` |

### Available Options

- `--translation, -t`: Specify Bible translation (default: kjv)
- `--limit, -l`: Limit search results (default: 5)
- `--help, -h`: Show help message

## 🌐 API Information

This project uses the **Bible API** (bible-api.com):
- **Base URL**: https://bible-api.com
- **Rate Limit**: 15 requests per 30 seconds
- **Authentication**: None required (public API)
- **Translations**: Supports KJV, NIV, ESV, and more
- **Rate Limiting**: CLI implements 2-second delays between requests to respect API limits

## 🧪 Testing

Run the complete test suite:
```bash
py -m pytest tests/ -v
```

Run with coverage report:
```bash
py -m pytest tests/ --cov=src --cov-report=term-missing
```

**Notes:**
- All external HTTP calls are mocked in tests
- No real API requests are made during testing or CI/CD
- Tests achieve high coverage of all functions
- All tests passing locally and in CI/CD

## 📁 Project Structure
```
bible-cli/
├── .github/
│   └── workflows/
│       └── tests.yml          # GitHub Actions CI/CD
├── src/
│   ├── __init__.py
│   ├── main.py                # CLI entry point
│   └── api.py                 # API integration
├── tests/
│   ├── __init__.py
│   ├── test_main.py           # CLI tests
│   └── test_api.py            # API tests with mocking
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── AGENTS.md                  # AI development documentation
└── .gitignore                 # Git ignore patterns
```

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

**Local development setup:**
```bash
git clone https://github.com/vestinie/bible-cli.git
cd bible-cli
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py -m pytest tests/ -v
```

**Code standards:**
- Follow PEP 8 style guidelines
- Include docstrings (Google style) for all functions and classes
- Mock external API calls in tests
- Ensure all tests pass before submitting pull requests

## ⚠️ Troubleshooting

### Rate Limit Issues
- The Bible API enforces rate limits (~15 requests per 30 seconds)
- If you receive HTTP 429 errors, wait a few seconds and retry
- The CLI implements 2-second delays between requests to help avoid limits

### Network Errors
- Verify internet connectivity
- Ensure https://bible-api.com is reachable
- Check firewall settings if requests are blocked

### Command Not Found
- Make sure you're in the `bible-cli` directory
- Verify Python is installed: `py --version`
- Ensure dependencies are installed: `py -m pip install -r requirements.txt`

## 🤖 AI-Assisted Development

This project was developed with assistance from **Claude (Anthropic)**. For detailed documentation of the AI-assisted development process, see [AGENTS.md](AGENTS.md).

**Key AI contributions:**
- Project structure and scaffolding
- API integration implementation
- Comprehensive test suite with mocking
- CI/CD configuration
- Professional documentation

## 🎓 Course Project

- **Course:** IS4010 - Software Development
- **Institution:** University of Cincinnati
- **Semester:** Fall 2024
- **Focus:** CLI development, API integration, testing, and CI/CD

## 🙏 Acknowledgments

- **Bible API** by Tim Morgan (bible-api.com) - Providing free access to Bible verses
- **Claude (Anthropic)** - AI assistance throughout development
- **Course instructors** - For assignment guidance and requirements

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Built with ❤️ and AI assistance for educational purposes**