import os
import io
from google.cloud import vision
from google.cloud.vision import types
import shutil

def pdf_to_text(input_dir, output_dir):
    # Create a client for the Vision API
    client = vision.ImageAnnotatorClient()

    # Loop through the files in the input directory
    for filename in os.listdir(input_dir):
        # Check if the file is a PDF
        if filename.endswith('.pdf'):
            # Open the PDF file
            with io.open(os.path.join(input_dir, filename), 'rb') as pdf_file:
                content = pdf_file.read()

                # Convert the PDF to an image
                image = types.Image(content=content)

                # Use the Vision API to extract text from the image
                response = client.document_text_detection(image=image)
                text = response.full_text_annotation.text

                # Save the text to a file in the output directory
                with io.open(os.path.join(output_dir, filename.replace('.pdf', '.txt')), 'w', encoding='utf-8') as text_file:
                    text_file.write(text)

    # Copy all other files from input to output
    for filename in os.listdir(input_dir):
        if not filename.endswith('.pdf'):
            shutil.copy(os.path.join(input_dir, filename), os.path.join(output_dir, filename))

# Call the function
input_dir = 'path/to/input/directory'
output_dir = 'path/to/output/directory'
pdf_to_text(input_dir, output_dir)
