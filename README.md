# Project 22 Medical image captioning

This is project work for the natural language processing and text mining course

## Initial setup

Create data directory and fetch the data

```bash
mkdir data
cd data
# Download and extract following files into data directory
# https://github.com/abachaa/VQA-Med-2019/blob/0fb58597a6704e10fb28f6ebce25af0e145bae2a/ImageClef-2019-VQA-Med-Training.zip
# https://github.com/abachaa/VQA-Med-2019/blob/0fb58597a6704e10fb28f6ebce25af0e145bae2a/ImageClef-2019-VQA-Med-Validation.zip
# After that ls should look like
ls
# ImageClef-2019-VQA-Med-Training      ImageClef-2019-VQA-Med-Validation
# ImageClef-2019-VQA-Med-Training.zip  ImageClef-2019-VQA-Med-Validation.zip
```

Create virtual env
```bash
# Depending on your machine python3 is either python3 or python
# Create python virtualenv named venv
python3 -m venv venv
# Activate virtualenv
source ./venv/bin/active
# Install required dependencies
pip install -r requirements.txt
```

Run the main script
```bash
python3 main.py
# Should output something that is not full of errors ;)
```

If possible use black formatter for the python code - [here](https://dev.to/adamlombard/how-to-use-the-black-python-code-formatter-in-vscode-3lo0) is a tutorial for setting it up.

## Project task description

VQA-Med 2019 dataset introduced a set of radiology images and four main related categories questions and answers about Modality, Plane, Organ system and Abnormality.  Each request considers one element only (e.g. what is the organ principally shown in this MRI? in what plane is this mammograph taken? is this a t1 weighted, t2 weighted, or flair image? what is most alarming about this ultrasound?). Then answers are made from the image content without requiring additional medical knowledge or domain-specific inference. These Q/A pairs could be explored to generate automatic captioning for their underlined images. Automatic image captioning aims at generating natural captions and meaningful textual description automatically for images, which is of great significance in scene understanding. The dataset can be downloaded from https://github.com/abachaa/VQA-Med-2019.

1. Download the dataset and visualize 15 Q/A pairs of your choice from different categories (Modality, Plane, Organ system and Abnormality). 
2. Use appropriate function to create tokens (with and without removing stop-words, and lemmatization).
3. Plot for each case, the word occurrence frequency curve after ranking the tokens. Check whether a power-law distribution can be fitted or not by plotting the log-log curve. Explain the results.
4. Now we would like to build a model for the Q/A system. Start with a simple string based matching process, imitating the example in Simple Question Answering (QA) Systems That Use Text Similarity Detection in Python - KDnuggets that uses string matching and naives Bayes’ classifier. You may notice that the system is quite limited but constitutes a good start. You may use one example in the validation test of the dataset to find out the type of outcome generated.
5. Instead of using string matching, modify the script in 4) to use Tfidf vectorizer and other types of classifiers (random forest, decision tree). Test the program on the same test query you used in 4). Discuss the limitations and how you may improve the results.  
Consider the query: “In What plane is this mammograph taken? Which part of the body does this represent, which modality and plane was used to take it and what abnormality is it seen in this image?”
6. Create tokens after preprocessing the query (removing stop-words and lemmatization).
7. Use the image id to refer to each Q/A pair, combine all categories to construct one line description for each image. Then create a matrix representation using the Boolean model and find the closest image to the query. 
8. Construct the tf-idf matrix representation of all Q/A pairs. Compute the similarity between the query and the images descriptions using different metrics. 
9. Expand the query by replacing the words with their synonyms (then using its Pos tagging when extracting the synonyms). 
10. Calculate the semantic similarity between new generated synonyms and the old tokens using one of the various available word-to-word semantic similarities.
11. Use the word2vec based similarity assuming that the vector associated to the whole new query corresponds to the average of the word2vec outputted vector associated to each token of the sentence, and then use the cosine similarity to compute the sentence-to-sentence similarity score. 
12. Use countVector or tf-idf to represent the new query and calculate the closest image description to the query. 
13. Identify appropriate literature in the field of medical image captioning to provide reasonable findings of the results in the previous steps. 