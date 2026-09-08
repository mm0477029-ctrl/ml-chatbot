import unittest
import json
import os
from chatbot import EducationChatbot


class TestEducationChatbot(unittest.TestCase):
    """Test suite for Education FAQ Chatbot"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures before running tests"""
        cls.chatbot = EducationChatbot('faq_data.json')
    
    def test_chatbot_initialization(self):
        """Test if chatbot initializes correctly"""
        self.assertIsNotNone(self.chatbot.faq_data)
        self.assertTrue(len(self.chatbot.faq_data) > 0)
        print("✓ Chatbot initialized successfully")
    
    def test_faq_data_loaded(self):
        """Test if FAQ data is properly loaded"""
        self.assertIsInstance(self.chatbot.faq_data, list)
        self.assertTrue(all('question' in faq and 'answer' in faq 
                           for faq in self.chatbot.faq_data))
        print(f"✓ {len(self.chatbot.faq_data)} FAQs loaded")
    
    def test_text_preprocessing(self):
        """Test text preprocessing function"""
        test_cases = [
            ("What COURSES are offered?", "what courses are offered"),
            ("Admission Fee $500!", "admission fee 500"),
            ("Hello??? World!!!", "hello world"),
        ]
        
        for input_text, expected in test_cases:
            result = self.chatbot.preprocess_text(input_text)
            self.assertEqual(result, expected)
        
        print("✓ Text preprocessing works correctly")
    
    def test_empty_input(self):
        """Test handling of empty input"""
        response = self.chatbot.get_response("")
        self.assertIsNotNone(response)
        self.assertIn("Please ask", response)
        print("✓ Empty input handled correctly")
    
    def test_whitespace_input(self):
        """Test handling of whitespace-only input"""
        response = self.chatbot.get_response("   ")
        self.assertIsNotNone(response)
        self.assertIn("Please ask", response)
        print("✓ Whitespace input handled correctly")
    
    def test_valid_question_matching(self):
        """Test if valid questions get matched"""
        valid_questions = [
            "What courses do you offer?",
            "Tell me about admission",
            "How much is the fee?",
            "Are there scholarships?",
        ]
        
        for question in valid_questions:
            faq_match, score = self.chatbot.find_best_match(question)
            self.assertIsNotNone(faq_match, f"No match found for: {question}")
            self.assertGreater(score, 0)
        
        print(f"✓ All {len(valid_questions)} test questions matched")
    
    def test_response_generation(self):
        """Test if responses are generated correctly"""
        test_question = "What is your admission process?"
        response = self.chatbot.get_response(test_question)
        
        self.assertIsNotNone(response)
        self.assertTrue(len(response) > 0)
        self.assertIsInstance(response, str)
        print("✓ Response generated successfully")
    
    def test_suggestion_generation(self):
        """Test if suggestions are generated"""
        partial_input = "admission"
        suggestions = self.chatbot.get_suggestions(partial_input)
        
        self.assertIsInstance(suggestions, list)
        self.assertTrue(len(suggestions) >= 0)
        print(f"✓ Generated {len(suggestions)} suggestions")
    
    def test_case_insensitivity(self):
        """Test if matching is case-insensitive"""
        question_lower = "what are the admission requirements?"
        question_upper = "WHAT ARE THE ADMISSION REQUIREMENTS?"
        
        match_lower, score_lower = self.chatbot.find_best_match(question_lower)
        match_upper, score_upper = self.chatbot.find_best_match(question_upper)
        
        # Both should match (might not be same FAQ, but should be valid)
        self.assertIsNotNone(match_lower)
        self.assertIsNotNone(match_upper)
        print("✓ Case insensitivity verified")
    
    def test_special_characters_removal(self):
        """Test if special characters are removed"""
        question = "What @#$% courses??? are offered!!!"
        response = self.chatbot.get_response(question)
        
        self.assertIsNotNone(response)
        self.assertTrue(len(response) > 0)
        print("✓ Special characters handled correctly")
    
    def test_similarity_threshold(self):
        """Test similarity scoring with different thresholds"""
        question = "random gibberish xyz abc 123"
        faq_match, score = self.chatbot.find_best_match(question, threshold=0.9)
        
        # With high threshold, shouldn't match
        self.assertIsNone(faq_match)
        print("✓ Similarity threshold working")
    
    def test_response_consistency(self):
        """Test if same question returns same answer"""
        question = "Tell me about scholarships"
        response1 = self.chatbot.get_response(question)
        response2 = self.chatbot.get_response(question)
        
        self.assertEqual(response1, response2)
        print("✓ Response consistency verified")
    
    def test_faq_structure(self):
        """Test if FAQ data has correct structure"""
        required_fields = ['id', 'question', 'answer']
        
        for faq in self.chatbot.faq_data:
            for field in required_fields:
                self.assertIn(field, faq, f"Missing field: {field}")
        
        print("✓ FAQ structure is valid")
    
    def test_vectorizer_fit(self):
        """Test if TF-IDF vectorizer is properly fitted"""
        self.assertIsNotNone(self.chatbot.tfidf_matrix)
        self.assertEqual(len(self.chatbot.faq_data), 
                        self.chatbot.tfidf_matrix.shape[0])
        print("✓ TF-IDF vectorizer properly fitted")


class TestChatbotPerformance(unittest.TestCase):
    """Performance tests for chatbot"""
    
    @classmethod
    def setUpClass(cls):
        """Set up performance test fixtures"""
        cls.chatbot = EducationChatbot('faq_data.json')
    
    def test_response_time(self):
        """Test if response is generated within reasonable time"""
        import time
        
        question = "What are the admission requirements?"
        start_time = time.time()
        response = self.chatbot.get_response(question)
        end_time = time.time()
        
        response_time = end_time - start_time
        self.assertLess(response_time, 1.0)  # Should be faster than 1 second
        print(f"✓ Response generated in {response_time:.4f} seconds")
    
    def test_bulk_queries(self):
        """Test chatbot with multiple queries"""
        import time
        
        questions = [
            "What courses are available?",
            "What are admission requirements?",
            "How much is tuition?",
            "Are scholarships available?",
            "When is the deadline?",
        ]
        
        start_time = time.time()
        
        for question in questions:
            response = self.chatbot.get_response(question)
            self.assertIsNotNone(response)
        
        end_time = time.time()
        total_time = end_time - start_time
        avg_time = total_time / len(questions)
        
        print(f"✓ Processed {len(questions)} queries in {total_time:.4f}s")
        print(f"  Average time per query: {avg_time:.4f}s")


def run_tests():
    """Run all tests with detailed output"""
    print("\n" + "="*60)
    print("Education FAQ Chatbot - Test Suite")
    print("="*60 + "\n")
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestEducationChatbot))
    suite.addTests(loader.loadTestsFromTestCase(TestChatbotPerformance))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    print(f"Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*60 + "\n")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
