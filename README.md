# ReelFeel - Sentiment Analysis Application

![Reelfeel Logo]()

A Sentiment Analysis Project for classification of positive and negative movie reviews and comments using Natural Language Processing(NLP)

## Descripton 🎬🎭

- This project compares the accuracies obtained between different neural network models including- Simple Neural Network(SNN),Convolutional Neural Network(CNN) and Re-current Neural Networks(RNN)
- It also analyzes performance between using TF-IDF vectorizer and Glove-embedding on a SNN.
- Used different stages of Machine Learning pipeline to analyze the Sentiment

#### 1. Data Collection

- Collected the IMDB dataset (50,000 movie reviews).
- Stored in MongoDB for efficient management.

#### 2. Data Preprocessing

- Cleaned and normalized text (removed HTML tags, punctuation, stop words, etc.).
- Applied lemmatization to reduce words to root forms.

#### 3. Feature Extraction

- Implemented Bag of Words (BoW), TF-IDF, and GloVe word embeddings for text vectorization.

#### 4. Model Development

- Developed three models: Simple Neural Network (SNN), Convolutional Neural Network (CNN), and Recurrent Neural Network (RNN) with LSTM.

#### 5. Model Integration

- Integrated the best-performing RNN-LSTM model into the backend using Python.
- Frontend developed using React.js.

![Sentiment Analysis Workflow](https://github.com/SahilTuladhar/ReelFeel/blob/master/images/Flowchart.jpg)

[Check this PDF for the full report](https://raw.githubusercontent.com/SahilTuladhar/ReelFeel/master/docs/ReelFeel-sentiment-analyis-Report-final%20.pdf)

## Limitations ⛔️

- It may not accurately identify sarcasm or irony in reviews.
- The system may struggle to understand slangs, idioms, and context specific to the movie

## Code Requirements 📱

You can install Conda for python which resolves all the dependencies for machine learning.

## Setup 🖥️

- Create directories to organize the files
- Environmental Setup: Install all the required dependencies such as pandas,numpy,matplotlib etc.
- Development Workflow
  - Preprocess data in data_preprocessing.py.
  - Develop the model in model.py, train in train.py, and evaluate in evaluate.py.
  - Use Jupyter notebooks for experimentation.

## Execution ▶️

Finally, Run the scripts or files in the correct order using the Jupyter Notebook.

## Results 📈

![Results and Outcomes](https://github.com/SahilTuladhar/ReelFeel/blob/master/images/results.png)
