import unittest
from app.image_generator import generate_image

class TestImageGeneration(unittest.TestCase):
    def test_generate_image(self):
        image = generate_image("A taxi in NYC")
        self.assertEqual(image.size, (512, 512))

if __name__ == "__main__":
    unittest.main()
