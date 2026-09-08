# Contributing to Education FAQ Chatbot 🤝

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## 📋 Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Report issues professionally
- No harassment or discrimination

## 🎯 How to Contribute

### 1. Report Bugs 🐛

Found a bug? Please create an issue with:

```markdown
**Description**: Clear description of the bug
**Steps to Reproduce**: 
1. Do this
2. Then this
3. Bug occurs

**Expected Behavior**: What should happen
**Actual Behavior**: What actually happens
**Environment**: OS, Python version, etc.
**Screenshots**: If applicable
```

### 2. Suggest Features ✨

Have an idea? Open an issue with:

```markdown
**Feature Request**: Clear title
**Description**: Detailed description of feature
**Use Case**: Why is this needed?
**Example**: How it would work
**Alternatives**: Other solutions considered
```

### 3. Submit Code Changes 💻

#### Step 1: Fork the Repository
```bash
# Click "Fork" on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/ml-chatbot.git
cd ml-chatbot
```

#### Step 2: Create a Branch
```bash
# Create a feature branch
git checkout -b feature/your-feature-name
# or for bug fixes
git checkout -b bugfix/bug-description
```

**Branch Naming Convention:**
- Features: `feature/feature-name`
- Bug fixes: `bugfix/bug-name`
- Documentation: `docs/doc-name`
- Tests: `test/test-name`

#### Step 3: Make Changes

Follow these guidelines:

**Python Style Guide:**
- Use PEP 8 style guide
- Max line length: 88 characters
- Use type hints where possible
- Write descriptive variable names

```python
# Good ✅
def get_faq_response(user_question: str) -> str:
    """Get chatbot response for user question."""
    processed_question = preprocess_text(user_question)
    faq_match, score = find_best_match(processed_question)
    return generate_response(faq_match)

# Bad ❌
def get_resp(q):
    p = preprocess_text(q)
    m, s = find_best_match(p)
    return gen_resp(m)
```

#### Step 4: Test Your Changes

```bash
# Run existing tests
python -m pytest test_chatbot.py -v

# Run specific test
python -m pytest test_chatbot.py::TestEducationChatbot::test_response_generation -v

# Run with coverage
python -m pytest test_chatbot.py --cov=. --cov-report=html
```

Write tests for new features:

```python
def test_new_feature(self):
    """Test description of what new feature does"""
    result = function_under_test(input_data)
    
    # Arrange: Set up test data
    expected = "expected_value"
    
    # Act: Execute the function
    actual = some_function()
    
    # Assert: Check results
    self.assertEqual(actual, expected)
```

#### Step 5: Commit Changes

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "Type: Brief description

More detailed explanation if needed.
- Point 1
- Point 2

Fixes #issue_number"
```

**Commit Message Format:**
```
Type: Description

Detailed explanation

- Bullet points
- More details

Fixes #123
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Build/config changes

#### Step 6: Push and Create Pull Request

```bash
# Push your branch
git push origin feature/your-feature-name
```

Then create PR on GitHub with:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## How Has This Been Tested?
- Test A: Pass/Fail
- Test B: Pass/Fail

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests pass

## Screenshots (if applicable)
[Add screenshots here]

## Related Issues
Closes #123
```

## 🧪 Testing Guidelines

### Test Structure
```python
class TestNewFeature(unittest.TestCase):
    """Test new feature functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        pass
    
    def test_happy_path(self):
        """Test normal operation"""
        pass
    
    def test_edge_cases(self):
        """Test edge cases"""
        pass
    
    def test_error_handling(self):
        """Test error handling"""
        pass
```

### Coverage Requirements
- Minimum 80% code coverage
- All public methods tested
- Edge cases covered
- Error conditions tested

### Running Tests
```bash
# Run all tests
python test_chatbot.py

# Run with verbose output
python -m unittest test_chatbot.py -v

# Run specific test class
python -m unittest test_chatbot.TestEducationChatbot

# Check coverage
python -m coverage run test_chatbot.py
python -m coverage report
python -m coverage html  # Generate HTML report
```

## 📝 Documentation Guidelines

### Docstrings
```python
def function_name(param1: str, param2: int) -> bool:
    """
    Brief description of function.
    
    Longer description explaining what the function does,
    why it does it, and any important details.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When this error occurs
        TypeError: When this error occurs
    
    Example:
        >>> result = function_name("test", 42)
        >>> print(result)
        True
    """
    pass
```

### README Updates
- Update SETUP.md if installation changed
- Update README.md for new features
- Add examples for new functionality
- Keep documentation up-to-date

## 🔄 Pull Request Process

1. **Fork** and create your branch
2. **Code** with style and tests
3. **Test** locally - all tests must pass
4. **Commit** with clear messages
5. **Push** to your fork
6. **Create PR** with description
7. **Review** - respond to feedback
8. **Merge** - after approval

## 👥 Review Process

### What Reviewers Look For
- ✅ Code follows style guidelines
- ✅ Tests are included and pass
- ✅ Documentation is updated
- ✅ No breaking changes without notice
- ✅ Changes are focused and single-purpose
- ✅ Performance implications considered

### Common Feedback

**"Need tests"**
→ Add unit tests covering your changes

**"Please update docs"**
→ Update README.md or relevant docs

**"This should be refactored"**
→ Simplify code, reduce complexity

**"Consider performance"**
→ Optimize loops, cache results

## 📚 Project Structure

```
ml-chatbot/
├── app.py                 # Main Streamlit app
├── chatbot.py             # Core chatbot logic
├── config.py              # Configuration settings
├── test_chatbot.py        # Unit tests
├── faq_data.json          # FAQ database
├── requirements.txt       # Dependencies
├── README.md              # Main documentation
├── SETUP.md               # Setup instructions
├── CONTRIBUTING.md        # This file
└── .gitignore             # Git ignore rules
```

## 🛠️ Development Setup

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/ml-chatbot.git
cd ml-chatbot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add development dependencies
pip install pytest pytest-cov black flake8

# Run tests
python test_chatbot.py

# Format code
black .

# Check style
flake8 .
```

## 🎓 Learning Resources

### NLP & Machine Learning
- [scikit-learn Documentation](https://scikit-learn.org)
- [NLTK Book](https://www.nltk.org/book/)
- [TF-IDF Explanation](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)

### Python
- [PEP 8 Style Guide](https://pep8.org/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)

### Web Development
- [Streamlit Docs](https://docs.streamlit.io)
- [Streamlit Components](https://streamlit.io/components)

## 🤔 Questions?

- Check existing GitHub issues
- Create a new issue with question tag
- Email: mm0477029@gmail.com
- Discussions tab on GitHub

## 🎉 Recognition

Contributors will be recognized in:
- This CONTRIBUTING.md file
- README.md contributors section
- GitHub contributors page

## 📄 License

By contributing, you agree your code is licensed under the MIT License.

---

**Happy Contributing! 🚀**

**Let's make this chatbot awesome together!**
