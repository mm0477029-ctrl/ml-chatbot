"""
Configuration File for Education FAQ Chatbot
Contains all configurable settings for the chatbot
"""

# ============================================
# APPLICATION SETTINGS
# ============================================

APP_NAME = "Education FAQ Chatbot"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Abhishek"
APP_EMAIL = "mm0477029@gmail.com"

# ============================================
# STREAMLIT SETTINGS
# ============================================

# Page configuration
PAGE_TITLE = "Education FAQ Chatbot"
PAGE_ICON = "🤖"
LAYOUT = "centered"  # "centered" or "wide"
INITIAL_SIDEBAR_STATE = "auto"  # "auto", "expanded", "collapsed"

# Streamlit theme
THEME = {
    "primaryColor": "#FF6B6B",
    "backgroundColor": "#F5F5F5",
    "secondaryBackgroundColor": "#FFFFFF",
    "textColor": "#1F1F1F",
    "font": "sans serif"
}

# ============================================
# NLP & MATCHING SETTINGS
# ============================================

# Similarity threshold for FAQ matching
# Range: 0.0 to 1.0 (higher = stricter matching)
SIMILARITY_THRESHOLD = 0.3

# Minimum character length for input
MIN_INPUT_LENGTH = 3

# Maximum suggestions to show
MAX_SUGGESTIONS = 5

# TF-IDF vectorizer settings
TFIDF_MAX_FEATURES = 500
TFIDF_NGRAM_RANGE = (1, 2)

# ============================================
# FAQ DATA SETTINGS
# ============================================

# Path to FAQ data file
FAQ_DATA_FILE = "faq_data.json"

# Required fields in FAQ data
FAQ_REQUIRED_FIELDS = ["id", "question", "keywords", "answer"]

# ============================================
# CHAT INTERFACE SETTINGS
# ============================================

# Chat history settings
CHAT_HISTORY_MAX = 50  # Maximum messages to keep in history
ENABLE_CHAT_HISTORY = True

# Message display
USER_MESSAGE_PREFIX = "👤 You: "
BOT_MESSAGE_PREFIX = "🤖 Chatbot: "
SUGGESTION_PREFIX = "💡 Suggested: "

# Default messages
DEFAULT_GREETING = "Hello! 👋 I'm your Education FAQ Chatbot. Ask me anything about our courses, admissions, fees, and more!"
DEFAULT_NO_MATCH = "I'm not sure about that. Could you rephrase your question?"
DEFAULT_ERROR = "Sorry, something went wrong. Please try again."
EMPTY_INPUT_MESSAGE = "Please ask a question to get started!"

# ============================================
# STYLING & UI SETTINGS
# ============================================

# Color scheme
COLORS = {
    "primary": "#FF6B6B",
    "secondary": "#4ECDC4",
    "success": "#95E1D3",
    "warning": "#FFA07A",
    "error": "#FF6B6B",
    "info": "#87CEEB",
    "light": "#F0F0F0",
    "dark": "#2C3E50"
}

# Font sizes
FONT_SIZES = {
    "title": "2.5rem",
    "heading": "1.5rem",
    "subheading": "1.2rem",
    "body": "1rem",
    "small": "0.9rem"
}

# ============================================
# FAQ CATEGORIES
# ============================================

FAQ_CATEGORIES = [
    "Courses",
    "Admissions",
    "Fees & Payments",
    "Scholarships",
    "Deadlines",
    "Documents Required",
    "Campus Facilities",
    "Other"
]

# ============================================
# EXAMPLE QUESTIONS
# ============================================

EXAMPLE_QUESTIONS = [
    "What courses do you offer?",
    "What are the admission requirements?",
    "How much is the tuition fee?",
    "Are scholarships available?",
    "When is the admission deadline?",
    "What documents do I need?",
    "Tell me about hostel facilities",
    "How can I apply?"
]

# ============================================
# LOGGING SETTINGS
# ============================================

# Enable logging
ENABLE_LOGGING = True

# Log file path
LOG_FILE = "chatbot.log"

# Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL = "INFO"

# Log format
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# ============================================
# DEPLOYMENT SETTINGS
# ============================================

# Server settings
SERVER_PORT = 8501
SERVER_ADDRESS = "localhost"

# API settings (if using API backend)
API_ENABLED = False
API_URL = "http://localhost:5000"
API_TIMEOUT = 10  # seconds

# ============================================
# PERFORMANCE SETTINGS
# ============================================

# Caching
ENABLE_CACHING = True
CACHE_TTL = 3600  # Cache Time To Live in seconds

# Rate limiting
RATE_LIMIT_ENABLED = False
RATE_LIMIT_REQUESTS = 100  # requests
RATE_LIMIT_PERIOD = 3600  # seconds (1 hour)

# ============================================
# SECURITY SETTINGS
# ============================================

# Input validation
MAX_INPUT_LENGTH = 500  # Maximum characters allowed in input
SANITIZE_INPUT = True  # Remove potentially harmful characters

# CORS settings
CORS_ALLOWED_ORIGINS = ["localhost", "127.0.0.1"]

# ============================================
# FEATURE FLAGS
# ============================================

# Enable/disable features
FEATURES = {
    "chat_history": True,
    "suggestions": True,
    "feedback": False,
    "analytics": False,
    "export_chat": False,
    "dark_mode": False,
    "multi_language": False
}

# ============================================
# DATABASE SETTINGS (Future Use)
# ============================================

# Database type: "json", "sqlite", "postgresql", "mongodb"
DATABASE_TYPE = "json"

# SQLite settings (if using SQLite)
SQLITE_DB_PATH = "chatbot_data.db"

# PostgreSQL settings (if using PostgreSQL)
POSTGRES_HOST = "localhost"
POSTGRES_PORT = 5432
POSTGRES_DB = "faq_chatbot"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "password"

# ============================================
# EMAIL SETTINGS (For Notifications)
# ============================================

EMAIL_ENABLED = False
EMAIL_SMTP_SERVER = "smtp.gmail.com"
EMAIL_SMTP_PORT = 587
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"

# ============================================
# FEEDBACK SETTINGS (For Future Use)
# ============================================

# Feedback collection
COLLECT_FEEDBACK = False
FEEDBACK_FILE = "feedback.json"

# Helpful/Unhelpful threshold
FEEDBACK_THRESHOLD = 0.5

# ============================================
# CONSTANTS
# ============================================

# Similarity scoring constants
MIN_SIMILARITY_SCORE = 0.0
MAX_SIMILARITY_SCORE = 1.0

# Timeout settings
DEFAULT_TIMEOUT = 30  # seconds

# ============================================
# ENVIRONMENT-SPECIFIC SETTINGS
# ============================================

ENVIRONMENT = "development"  # "development", "staging", "production"

if ENVIRONMENT == "production":
    # Production settings
    DEBUG = False
    ENABLE_LOGGING = True
    CACHE_TTL = 7200
else:
    # Development settings
    DEBUG = True
    ENABLE_LOGGING = True
    CACHE_TTL = 3600

# ============================================
# HELPER FUNCTIONS
# ============================================

def get_config(key, default=None):
    """Get configuration value by key"""
    return globals().get(key, default)

def update_config(key, value):
    """Update configuration value"""
    globals()[key] = value

def print_config():
    """Print all configuration settings"""
    print("\n" + "="*60)
    print("Chatbot Configuration")
    print("="*60)
    
    config_items = {k: v for k, v in globals().items() 
                   if not k.startswith('_') and not callable(v)}
    
    for key, value in sorted(config_items.items()):
        print(f"{key}: {value}")
    
    print("="*60 + "\n")

# ============================================
# VALIDATE CONFIGURATION
# ============================================

def validate_config():
    """Validate configuration settings"""
    errors = []
    
    # Check similarity threshold
    if not (0.0 <= SIMILARITY_THRESHOLD <= 1.0):
        errors.append("SIMILARITY_THRESHOLD must be between 0.0 and 1.0")
    
    # Check FAQ file exists
    import os
    if not os.path.exists(FAQ_DATA_FILE):
        errors.append(f"FAQ data file not found: {FAQ_DATA_FILE}")
    
    # Check max suggestions
    if MAX_SUGGESTIONS < 1:
        errors.append("MAX_SUGGESTIONS must be at least 1")
    
    if errors:
        print("Configuration Errors:")
        for error in errors:
            print(f"  ❌ {error}")
        return False
    
    return True

if __name__ == "__main__":
    print_config()
    if validate_config():
        print("✅ Configuration is valid!")
    else:
        print("❌ Configuration has errors!")
