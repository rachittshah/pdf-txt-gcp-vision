# pdf-txt-gcp-vision

To test the script locally, you'll need to install the Google Cloud SDK and the Google Cloud Vision client library for Python.

Here are the steps:

Install the Google Cloud SDK: Follow the instructions at https://cloud.google.com/sdk/docs/install to install the Google Cloud SDK.

Set up the Google Cloud SDK: Run the following command to initialize the SDK and set up default configuration settings:

```gcloud init```

Install the Google Cloud Vision library: Run the following command to install the Google Cloud Vision client library for Python:


```pip install -r requiremnts.txt```

Set the ```GOOGLE_APPLICATION_CREDENTIALS environment variable: Set the GOOGLE_APPLICATION_CREDENTIALS``` environment variable to the path of your Google Cloud 

service account key. For example:


```export GOOGLE_APPLICATION_CREDENTIALS='path/to/service-account-key.json'```

Run the script: Run the script from the command line using the input and output directory paths as arguments. For example:


```python extract.py path/to/input/directory path/to/output/directory```

This should convert the PDF files in the input directory to text files and save them in the output directory.
