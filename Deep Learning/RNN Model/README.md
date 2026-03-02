# BERT Chatbot

A simple chatbot application powered by BERT (Bidirectional Encoder Representations from Transformers) built with Streamlit. This app uses BERT to understand user queries and provide context-aware responses based on a predefined set of questions and answers.

## Features

- **BERT-Powered Responses**: Utilizes BERT embeddings and cosine similarity to match user inputs to the most relevant predefined responses.
- **Streamlit Interface**: Clean and interactive web-based UI for easy interaction.
- **Custom Background**: Features a custom background image for an enhanced user experience.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/munnakona/NareshIT-AI.git
   cd "Deep Learning/RNN Model"
   ```

2. Install the required dependencies:
   ```bash
   pip install streamlit transformers torch scikit-learn
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run bert_chatbot.py
   ```

2. Open your browser and navigate to the provided local URL (usually `http://localhost:8501`).

3. Type your queries in the text input field and receive responses from the chatbot.

## How It Works

- The app loads a pre-trained BERT model and tokenizer.
- Predefined question-answer pairs are embedded using BERT.
- User inputs are embedded and compared to predefined embeddings using cosine similarity.
- The response with the highest similarity score above a threshold is returned.

## Predefined Questions

The chatbot can respond to questions like:
- What is your name?
- How are you?
- What is BERT?
- Tell me a joke.
- What is data science?
- What is your use?
- What is AI?
- What is Microsoft Azure?

## Requirements

- Python 3.7+
- Streamlit
- Transformers
- PyTorch
- Scikit-learn

## Contributing

Feel free to contribute by adding more Q&A pairs or improving the matching algorithm.

## License

This project is open-source. Feel free to use and modify it.