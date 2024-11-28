# Post Generator Web App
A web application built with Flask And Google Gemini that allows users to generate posts based on selected topic, length, and language.
The app uses Few-Shot Learning to guide a language model by leveraging past posts with specific attribute(such as topic, length and language).

## Features
Post Generation: Users can select from predefined tags, choose post length (Short, Medium, or Long), and select language (English or Hinglish) to generate a new post.
Few-Shot Learning: Past posts related to specific parameters (topic, length, and language) are used to guide the language model for generating more accurate and contextually relevant posts.
Google Generative AI: The app utilizes Google’s Generative AI models to generate posts based on user-selected inputs.

## Technical Architecture
Stage 1: Collect LinkedIn Posts
The first stage involves collecting past LinkedIn posts and analyzing them to extract key features, including Topic, Language, and Length.
Stage 2: Generate New Post
The app uses these features (topic, language, and length) to generate a new post.
Few-Shot Learning is applied by using past posts related to a specific topic, language, and length to guide Google Generative AI in producing more accurate content that follows the same style and context.



## Set-up
1. API Key Setup

To interact with Google Generative AI API, you need to create a Google Cloud project and obtain an API key.

Steps to get your API key:
Go to the Google Cloud Console.
Create a new project or select an existing one.
Enable Google Generative AI API (or the relevant API depending on your use case).
Obtain your API key from the Credentials section.

2. Install Dependencies

Install the required Python libraries:
pip install -r requirements.txt

3. Run the Flask App

After installing the dependencies, run the Flask app:
python app.py

This will start the Flask development server on http://127.0.0.1:5000/.



**Additional Terms:**
This software is licensed under the MIT License. However, commercial use of this software is strictly prohibited without prior written permission from the author. Attribution must be given in all copies or substantial portions of the software.
