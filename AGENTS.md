# Project Name: Bible CLI

## Overview
A command-line tool to fetch and display Bible verses, chapters, and search for verses by keyword. Users can retrieve specific verses, get random verses, read entire chapters, and search for verses containing specific keywords. Built with AI assistance as part of a software development course project.

## API Integration
- **API:** Bible API (bible-api.com)
- **Base URL:** https://bible-api.com
- **Authentication:** None required (public API)
- **Rate Limit:** 15 requests per 30 seconds
- **Key endpoints:**
  - `/{reference}` - Get specific verse or chapter (e.g., "John 3:16", "Psalm 23")
  - `/?random=verse` - Get a random Bible verse
  - Supports translation parameter for different Bible versions
- **Data format:** JSON with reference, text, translation, and verses array

## CLI Commands
- `verse [reference]` - Get a specific Bible verse (e.g., "John 3:16")
  - Optional: `--translation/-t` flag for different Bible versions
- `random` - Get a random Bible verse
  - Optional: `--translation/-t` flag
- `chapter [reference]` - Get an entire chapter (e.g., "Psalm 23")
  - Optional: `--translation/-t` flag
- `search [keyword]` - Search for verses containing a keyword
  - Optional: `--limit/-l` flag to control number of results (default: 5)

## Technical Stack
- Python 3.9+
- argparse for CLI argument parsing
- requests library for API calls
- pytest for testing with mocking
- pytest-cov for test coverage reporting
- GitHub Actions for CI/CD automation

## Code Organization
- `src/main.py` - Entry point and argparse CLI setup with all 4 commands
- `src/api.py` - API interaction functions (get_verse, get_random_verse, get_chapter, search_verses)
- `src/__init__.py` - Package initialization
- `tests/test_main.py` - CLI command tests with mocked functions
- `tests/test_api.py` - API function tests with mocked HTTP requests
- `tests/__init__.py` - Test package initialization
- `.github/workflows/tests.yml` - GitHub Actions CI/CD configuration
- `requirements.txt` - Python dependencies
- `README.md` - Professional documentation
- `.gitignore` - Git ignore patterns

## Standards
- Use docstrings for all functions and classes (Google style)
- Follow PEP 8 style guidelines
- Handle errors gracefully with try/except blocks
- Mock all API calls in tests (no real requests during testing)
- Rate limiting implemented (2-second delay between requests)
- Comprehensive error handling for network issues and invalid inputs
- User-friendly output with emojis and clear formatting

## AI-Assisted Development Process

### Tools Used
- **Primary AI Assistant:** Claude (Anthropic)
- **Development Environment:** VS Code
- **Version Control:** Git & GitHub

### Phase 1: Planning (AI-Assisted)
**Conversation with AI:**
- Started by asking for help understanding CLI, API, and arguments concepts
- Discussed faith-based API options
- AI researched and recommended Bible API (bible-api.com) for:
  - No authentication required
  - Simple REST endpoints
  - Free tier suitable for educational use
  - Good documentation

**AI Contribution:**
- Explained fundamental programming concepts clearly
- Researched multiple API options
- Recommended best API for assignment requirements

### Phase 2: Project Structure (AI-Generated)
**What AI Created:**
- Complete directory structure following Python best practices
- Proper package setup with `__init__.py` files
- Separation of concerns (CLI logic vs API logic)
- GitHub Actions workflow configuration

**Learning Outcome:**
- Understanding of professional Python project organization
- Importance of proper package structure

### Phase 3: Core Development (AI-Assisted)
**CLI Implementation (main.py):**
- AI generated complete argparse setup with 4 subcommands
- Implemented help text and usage examples
- Added error handling with appropriate exit codes
- Created user-friendly output formatting

**API Integration (api.py):**
- AI implemented all API interaction functions
- Added rate limiting to respect API constraints
- Implemented comprehensive error handling
- Created consistent return formats across functions

**Key Patterns Learned:**
- Argparse subcommands and argument parsing
- HTTP request error handling
- JSON response parsing
- Rate limiting strategies

### Phase 4: Testing (AI-Generated)
**Testing Strategy:**
- AI wrote comprehensive test suite with pytest
- Implemented mocking for all API calls using unittest.mock
- Created tests for success cases, error cases, and edge cases
- Achieved 100% test coverage

**Mocking Approach:**
```python
@patch('src.api.requests.get')
@patch('src.api.time.sleep')
def test_function(mock_sleep, mock_get):
    # Mock API responses
    # Test function behavior
```

**Learning Outcome:**
- Understanding of test-driven development
- How to mock external dependencies
- Writing comprehensive test suites

### Phase 5: CI/CD (AI-Configured)
**GitHub Actions Setup:**
- AI created complete workflow file
- Configured Python environment setup
- Added dependency installation
- Included pytest execution with coverage
- Added CLI smoke test

**Learning Outcome:**
- Understanding of continuous integration
- Automated testing workflows
- GitHub Actions configuration

### Phase 6: Documentation (AI-Generated)
**README.md:**
- Professional documentation with all required sections
- Clear installation and usage instructions
- Code examples for all commands
- Status badges for tests and Python version

**AGENTS.md:**
- Complete documentation of AI-assisted development
- Detailed explanation of each phase
- Learning outcomes and reflections

## Effective Prompting Strategies Used

### What Worked Well:
1. **Starting with concepts:** Asked AI to explain CLI, API, arguments before diving into code
2. **Sharing complete requirements:** Provided full assignment rubric upfront
3. **Iterative approach:** Built project step-by-step rather than all at once
4. **Asking for explanations:** Requested clarification when concepts were unclear
5. **Conversational mode:** Used step-by-step guidance when feeling overwhelmed

### Example Effective Prompts:
- "What is CLI, API and arguments - I don't understand those terms"
- "Can you do something faith based for an API if that exists?"
- "I have specific instructions on what my code needs to pass for my assignment"
- "Can we go step by step like convo mode" (when overwhelmed)

## Key Learning Outcomes

### Technical Skills:
- API integration with REST endpoints
- CLI development using argparse
- Test-driven development with pytest
- Mocking external dependencies
- CI/CD with GitHub Actions
- Professional Python project structure

### AI Collaboration Skills:
- How to effectively prompt AI assistants
- When to ask for explanations vs. code
- Breaking down complex tasks into manageable steps
- Verifying and testing AI-generated code
- Using AI as a learning tool, not just a code generator

### Professional Development:
- Writing comprehensive documentation
- Following coding standards (PEP 8)
- Version control best practices
- Creating portfolio-worthy projects

## Challenges and Solutions

### Challenge 1: Understanding Core Concepts
**Problem:** Didn't understand CLI, API, arguments initially
**Solution:** Asked AI to explain concepts before writing code
**Outcome:** Strong foundational understanding enabled better collaboration

### Challenge 2: Feeling Overwhelmed
**Problem:** Too many steps felt overwhelming
**Solution:** Switched to conversational, step-by-step mode with AI
**Outcome:** Completed project systematically without stress

### Challenge 3: Environment Setup
**Problem:** Python command not found, pip not recognized
**Solution:** AI helped troubleshoot and find `py` command for Windows
**Outcome:** Successfully installed dependencies and ran tests

## Time Investment
- **Phase 1 (Planning):** ~30 minutes
- **Phase 2 (Setup):** ~20 minutes
- **Phase 3 (Development):** ~45 minutes (AI-generated, verified locally)
- **Phase 4 (Testing):** ~15 minutes (AI-generated tests)
- **Phase 5 (Documentation):** ~30 minutes
- **Total:** ~2.5 hours (vs estimated 7-10 hours without AI)

## Reflection

### What AI Did Exceptionally Well:
- Generated production-quality, well-documented code
- Explained complex concepts in understandable terms
- Provided comprehensive test coverage
- Created professional documentation
- Adapted to my learning pace and style

### What Required Human Input:
- Choosing project direction (faith-based API)
- Making design decisions
- Verifying code works correctly
- Understanding concepts deeply
- Academic integrity decisions (public vs private repo)

### Key Takeaway:
AI is an exceptional learning partner and productivity multiplier. It excels at generating boilerplate code, writing tests, and creating documentation. However, human judgment, understanding, and verification remain essential. The most effective approach is collaboration - using AI to accelerate development while maintaining understanding and ownership of the codebase.

### Would I Use AI Again?
Absolutely! This project demonstrated that AI can:
- Dramatically reduce development time
- Teach best practices and patterns
- Generate comprehensive tests and documentation
- Help overcome knowledge gaps
- Make learning more interactive and engaging

The key is using AI as a teaching tool and collaborator, not just a code generator.

---

**Student:** Ishimwe Vestine 
**Course:** IS4010  
**Institution:** University of Cincinnati  
**Semester:** Fall 2024  
**Date:** October 2024  
**AI Assistant:** Claude (Anthropic)