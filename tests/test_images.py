import unittest
from unittest.mock import patch
from app.image_generator import generate_stable_diffusion_image

class TestImageGeneration(unittest.TestCase):
    @patch('requests.post')
    def test_generate_stable_diffusion_image(self, mock_post):
        # Mock response
        mock_response = type('Response', (), {
            'raise_for_status': lambda: None,
            'json': lambda: {'output': ['base64_encoded_image_data']}
        })
        mock_post.return_value = mock_response

        response = generate_stable_diffusion_image("A taxi in NYC")
        self.assertIsInstance(response, dict)
        self.assertTrue('output' in response)
        
        # Verify API was called with correct parameters
        mock_post.assert_called_once()
        _, kwargs = mock_post.call_args
        self.assertEqual(kwargs['json']['prompt'], "A taxi in NYC")

if __name__ == "__main__":
    unittest.main()
