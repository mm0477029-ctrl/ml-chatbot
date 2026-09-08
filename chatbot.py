import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


class EducationChatbot:
    def __init__(self, faq_file='faq_data.json'):
        """Initialize chatbot with FAQ data"""
        self.faq_data = self.load_faq(faq_file)
        self.vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')
        self.prepare_vectors()
        
    def load_faq(self, faq_file):
        """Load FAQ data from JSON file"""
        try:
            with open(faq_file, 'r') as f:
                data = json.load(f)
            return data['faqs']
        except FileNotFoundError:
            print(f"Error: {faq_file} not found!")
            return []
    
    def prepare_vectors(self):
        """Create TF-IDF vectors for all FAQ questions"""
        if not self.faq_data:
            return
        
        questions = [faq['question'] for faq in self.faq_data]
        self.tfidf_matrix = self.vectorizer.fit_transform(questions)
    
    def preprocess_text(self, text):
        """Clean and preprocess user input"""
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return text
    
    def find_best_match(self, user_input, threshold=0.3):
        """Find the best matching FAQ using TF-IDF similarity"""
        if not self.faq_data:
            return None, 0
        
        processed_input = self.preprocess_text(user_input)
        input_vector = self.vectorizer.transform([processed_input])
        
        similarities = cosine_similarity(input_vector, self.tfidf_matrix)[0]
        best_idx = similarities.argmax()
        best_score = similarities[best_idx]
        
        if best_score >= threshold:
            return self.faq_data[best_idx], best_score
        
        return None, best_score
    
    def get_response(self, user_input):
        """Get chatbot response for user input"""
        if not user_input.strip():
            return "Please ask a question about our courses, admission, or fees."
        
        faq_match, score = self.find_best_match(user_input)
        
        if faq_match:
            return faq_match['answer']
        else:
            return ("I'm not sure about that. Please try asking about:\n"
                   "- Courses offered\n"
                   "- Admission requirements\n"
                   "- Fees and scholarships\n"
                   "- Application process\n"
                   "- Hostel facilities\n\n"
                   "Or contact our admissions office directly.")
    
    def get_suggestions(self, partial_input):
        """Get FAQ suggestions based on partial input"""
        suggestions = []
        processed_input = self.preprocess_text(partial_input)
        
        for faq in self.faq_data:
            question_lower = faq['question'].lower()
            if processed_input in question_lower or any(keyword in question_lower 
                                                         for keyword in faq.get('keywords', [])):
                suggestions.append(faq['question'])
        
        return suggestions[:5]  # Return top 5 suggestions
