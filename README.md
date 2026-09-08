# Education FAQ Chatbot 🤖

An intelligent FAQ chatbot built with Machine Learning and Natural Language Processing to help students with questions about courses, admissions, and fees.

## 📋 Features

- **NLP-based Question Matching** - Uses TF-IDF vectorization to understand user questions
- **Smart FAQ Matching** - Finds the most relevant answer using cosine similarity
- **Beautiful Web Interface** - Built with Streamlit for easy interaction
- **Real-time Chat** - Instant responses to student queries
- **Suggested Questions** - Contextual suggestions for better user experience
- **Easy to Customize** - Simply update `faq_data.json` to add more FAQs

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** - Web UI framework
- **Scikit-learn** - Machine Learning library
- **NLTK** - Natural Language Processing
- **JSON** - FAQ data storage

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/mm0477029-ctrl/ml-chatbot.git
cd ml-chatbot
```

### Step 2: Create Virtual Environment
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

### Local Development
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
ml-chatbot/
├── app.py              # Streamlit web application
├── chatbot.py          # Chatbot logic and NLP model
├── faq_data.json       # FAQ database
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## 🧠 How It Works

### 1. **Question Preprocessing**
- Converts user input to lowercase
- Removes special characters
- Tokenizes the text

### 2. **TF-IDF Vectorization**
- Creates numerical vectors from FAQ questions
- Represents text as a matrix of term frequencies

### 3. **Similarity Matching**
- Uses cosine similarity to compare user question with FAQ questions
- Finds the best matching FAQ with similarity score

### 4. **Response Generation**
- Returns the answer from matching FAQ
- If no match found, shows helpful suggestions

## 📊 Example FAQs Included

The chatbot currently has FAQs about:
- Course offerings
- Admission requirements
- Application fees
- Tuition fees
- Scholarships
- Admission deadlines
- Application process
- Required documents
- Admission deferment
- Hostel facilities

## 🎯 Adding New FAQs

To add new questions and answers, edit `faq_data.json`:

```json
{
  "id": 11,
  "question": "Your question here?",
  "keywords": ["keyword1", "keyword2"],
  "answer": "Your answer here"
}
```

Then restart the app - it will automatically pick up the new FAQ!

## 🌐 Deployment Options

### Option 1: Streamlit Cloud (Recommended - Free)
1. Push code to GitHub
2. Go to https://share.streamlit.io/
3. Connect your GitHub repo
4. Deploy in one click!
5. Get a live URL like: `https://your-app-streamlit.app`

### Option 2: Heroku
```bash
# Create Heroku app
heroku create your-app-name

# Deploy
git push heroku main
```

### Option 3: AWS/Google Cloud
Deploy Docker container or use their ML services

## 💡 How to Present This Project

### In Resume/LinkedIn
"Developed an NLP-based FAQ chatbot using TF-IDF vectorization and cosine similarity to match student questions with educational content. Built responsive web interface using Streamlit with real-time chat functionality."

### Interview Talking Points
1. **NLP Techniques Used**: TF-IDF, Cosine Similarity
2. **Why TF-IDF?**: Lightweight, fast, effective for FAQ matching
3. **Scalability**: Can handle 1000+ FAQs easily
4. **Future Improvements**: 
   - Add BERT for better semantic understanding
   - Implement user feedback loop
   - Add multiple languages
   - Database integration for FAQ management

## 🔧 Customization Guide

### Change Similarity Threshold
Edit in `chatbot.py` line 51:
```python
if best_score >= 0.3:  # Change 0.3 to your desired value
```

### Modify UI
Edit `app.py` to customize:
- Colors and styling
- Chat interface layout
- Sidebar content
- Example questions

### Add More Features
- Add database (SQLite, PostgreSQL)
- Implement user feedback
- Add analytics dashboard
- Multi-language support

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Abhishek**
- GitHub: [@mm0477029-ctrl](https://github.com/mm0477029-ctrl)
- Email: mm0477029@gmail.com

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📧 Support

For questions or issues, please:
1. Check existing GitHub issues
2. Create a new issue with details
3. Provide error messages and steps to reproduce

## 🎓 Learning Resources

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [NLTK Tutorial](https://www.nltk.org/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [NLP Concepts](https://www.coursera.org/learn/natural-language-processing)

---

**Made with ❤️ using Python, ML, and Streamlit**
