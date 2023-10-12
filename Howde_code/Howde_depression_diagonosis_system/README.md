# HOWDE_DEPRESSION_DIAGONIS 
## Fine tuning Bert model from the Hugging Faces 
* To diagnose and classify whether the text in the Howde networking shows stress or not. After comparing Bert, TF-IDF, Word2Vec + TF-IDF, since Bert shows the best results on the test set, it will be used for classification. 
* Fine-tune a deep learning BERT model in NLP Deep Learning to effectively classify conversations, discerning stress levels for comprehensive user health monitoring. 
- Based on those accuratecy (precision, recall, F1-score) we can conclude Bert is the most stable and precisive model. However, we still keep TF-IDF and Word2Vec + TF-IDF models as submodels to continue update the accuratecy over time and check it with Bert. 
- Since Bert is the most stable model, we will run and only need to execute code in Stress_Analysis_Bert Jupiter notebook. 
- After the first training which take quite long, we will input the some sentences and the output is to classify wether that user is stress or not. The confidence output on the left represents the nonstress probabilities (normalization) while the other represents the stress probabilies(normalization). The closer the confidence get to 0, to more likely the bert model labels it.

## How to run 
For more information, please check out the code run demo [Link](https://drive.google.com/drive/u/0/folders/1D9U4fQvjhhWA_4W9OUkcG5Ea_3xk8XwL)

## Requisites
- MacOS or Linux
- Python 3.7.4
- conda 
- pip
- GPU (To run BERT model)

## Setup
This project requires Python 3.7.4 and conda environment. To setup the environment, please follow these steps:

- Create a new conda virtual environment in local or cloud services
```
conda create -n new_env python=3.7.4 
conda activate new_env 
```
- Clone the github repository
```
- Install the required packages in the conda environment
```
cd Insight_Stress_Analysis/build
conda install pip
pip install -r requirements.txt
```
- If have problem install BentoML with requirement.txt file
```
pip install bentoml
```
- For first time using running the project, you need to download some important data packages
```
cd Insight_Stress_Analysis
python config.py
```
### Additional Setup
- If you have GPU and would like to run the BERT model, install:
```
* pip install tensorflow-gpu==1.15
* download the hub module from tensorflow
* run the cells in the Stress_Analysis_BERT.ipynb 
* predict, saved model with tensorflow_server.


