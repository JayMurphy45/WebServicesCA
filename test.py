import unittest
from fastapi.testclient import TestClient
from main import app
from reportlab.pdfgen import canvas
from io import StringIO

class TestFastAPIApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Hello": "World"})

    def test_get_single_product(self):
        response = self.client.get("/getSingleProduct/AUTO008")
        self.assertEqual(response.status_code, 200)

    def test_get_all_products(self):
        response = self.client.get("/getAll")
        self.assertEqual(response.status_code, 200)

    def test_add_new(self):
        response = self.client.post("/addNew/AUTO008/Motor/1.0/1/test")
        self.assertEqual(response.status_code, 200)

    def test_delete_one(self):
        response = self.client.delete("/deleteOne/AUTO008")
        self.assertEqual(response.status_code, 200)

    def test_starts_with(self):
        response = self.client.get("/startsWith/m")
        self.assertEqual(response.status_code, 200)

    def test_paginate(self):
        response = self.client.get("/paginate/1/2")
        self.assertEqual(response.status_code, 200)

    def test_convert(self):
        response = self.client.get("/convert/AUTO008")
        self.assertEqual(response.status_code, 200)

# Function to generate a PDF with test results
def generate_pdf(file_name: str, test_results: str):
    pdf = canvas.Canvas(file_name)
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 750, "Test Results")
    pdf.drawString(100, 730, "-----------------------------")

    y = 710
    for line in test_results.split("\n"):
        pdf.drawString(100, y, line)
        y -= 15
        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y = 750

    pdf.save()
    print(f"PDF generated: {file_name}")

if __name__ == "__main__":
    # Capture test results
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestFastAPIApp)
    test_runner = unittest.TextTestRunner(resultclass=unittest.TextTestResult, stream=StringIO())
    result_buffer = StringIO()
    test_runner = unittest.TextTestRunner(stream=result_buffer, verbosity=2)
    test_runner.run(test_suite)

    # Generate the PDF with test results
    test_results = result_buffer.getvalue()
    generate_pdf("test_results.pdf", test_results)

    # Print test results to the console
    print(test_results)