# Setup Guide - Education FAQ Chatbot 🚀

Complete step-by-step guide to set up and run the chatbot locally.

## ⚙️ System Requirements

- **OS**: Windows, macOS, or Linux
- **Python**: 3.8 or higher
- **RAM**: 2GB minimum
- **Disk Space**: 500MB free

## 📥 Step 1: Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/mm0477029-ctrl/ml-chatbot.git
cd ml-chatbot
```

## 🐍 Step 2: Set Up Python Virtual Environment

A virtual environment keeps dependencies isolated from your system Python.

### On Windows:
```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate
```

### On macOS/Linux:
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt when active.

## 📦 Step 3: Install Dependencies

With the virtual environment activated, run:

```bash
pip install -r requirements.txt
```

This will install:
- streamlit (web framework)
- scikit-learn (ML library)
- nltk (NLP library)
- numpy & pandas (data processing)

Wait for installation to complete (might take 2-5 minutes).

## ✅ Verification

Check if everything is installed correctly:

```bash
python -c "import streamlit; import sklearn; import nltk; print('All dependencies installed!')"
```

## 🎯 Step 4: Run the Application

Execute this command:

```bash
streamlit run app.py
```

Expected output:
```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

## 🌐 Step 5: Access the App

Automatically opens in your default browser at `http://localhost:8501`

If not, manually open that URL in your browser.

## 🧪 Testing the Chatbot

Try these example questions:

1. "What courses are available?"
2. "What are admission requirements?"
3. "How much is the tuition fee?"
4. "Are scholarships available?"
5. "When is the admission deadline?"

## 🛠️ Troubleshooting

### Issue: Command not found - `python`

**Solution**: Use `python3` instead on macOS/Linux
```bash
python3 -m venv venv
python3 -m pip install -r requirements.txt
```

### Issue: ModuleNotFoundError when running app.py

**Solution**: Make sure virtual environment is activated
```bash
# Check if (venv) appears in your terminal prompt
# If not, activate it:
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### Issue: Port 8501 already in use

**Solution**: Run on a different port
```bash
streamlit run app.py --server.port 8502
```

### Issue: nltk data not found

**Solution**: Download NLTK data manually
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### Issue: JSON file not found error

**Make sure `faq_data.json` is in the same directory as `app.py`**

## 📝 Project Structure After Setup

```
ml-chatbot/
├── venv/                 # Virtual environment (created after setup)
├── __pycache__/          # Python cache (created after running)
├── app.py                # Main Streamlit app
├── chatbot.py            # Chatbot logic
├── faq_data.json         # FAQ database
├── requirements.txt      # Dependencies
├── .gitignore            # Git ignore rules
├── README.md             # Main documentation
└── SETUP.md              # This file
```

## 🔄 Daily Usage

After first setup, to run the app again:

```bash
# 1. Navigate to project directory
cd ml-chatbot

# 2. Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# 3. Run the app
streamlit run app.py
```

## 📱 Adding More FAQs

Edit `faq_data.json` to add new questions:

```json
{
  "id": 11,
  "question": "What is the scholarship amount?",
  "keywords": ["scholarship", "amount", "award"],
  "answer": "Scholarships range from 25% to 50% of tuition fees based on merit."
}
```

Restart the app to load new FAQs automatically.

## 🌐 Deploy to Production

### Option 1: Streamlit Cloud (Easiest)

1. Push code to GitHub
2. Go to https://share.streamlit.io
3. Sign in with GitHub
4. Click "New app"
5. Select your repo: `mm0477029-ctrl/ml-chatbot`
6. Main file: `app.py`
7. Deploy!

Get a shareable link like: `https://ml-chatbot-abhishek.streamlit.app`

### Option 2: Heroku

1. Install Heroku CLI
2. Create `Procfile`:
```
web: streamlit run app.py
```
3. Run:
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### Option 3: Local Server (Advanced)

Use ngrok to expose local server:
```bash
# Install ngrok from https://ngrok.com
ngrok http 8501
```

## 🆘 Getting Help

1. **Check GitHub Issues**: https://github.com/mm0477029-ctrl/ml-chatbot/issues
2. **Read Documentation**: Check README.md
3. **Stack Overflow**: Tag with `streamlit`, `nltk`, `scikit-learn`
4. **Email**: mm0477029@gmail.com

## ✨ Next Steps

After successful setup:

1. **Customize FAQ**: Add domain-specific questions
2. **Improve Matching**: Adjust threshold in `chatbot.py`
3. **Add Features**: Implement feedback, analytics, or database
4. **Deploy**: Share with others using Streamlit Cloud
5. **Learn**: Understand TF-IDF and cosine similarity in detail

## 📚 Learning Resources

- [Streamlit Docs](https://docs.streamlit.io/)
- [NLTK Book](https://www.nltk.org/book/)
- [Scikit-learn TF-IDF](https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

**Happy Chatbot Building! 🤖✨**
