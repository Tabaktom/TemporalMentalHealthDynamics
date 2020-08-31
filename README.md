# TemporalMentalHealthDynamics

The Auxiliary Files during the course of the Temporal Mental Health Dynamics on Social Media research project are categorised into 3 main areas: Data Mining, Preprocessing and Classifier Analysis and Monitoring. All code is written in python 3.7. Files contain a mixture of scrips (.py) and Jupyter Notebooks (.ipynb).

Notes: 
---------------------
* Data has not been included in this submission however we plan to share the datasets with full adherence to the Twitter Developer user agreement. 

* Minor adjustments may be required for replication, particularly those relating to file paths. 
---------------------

1. Data Mining: used for extracting initial tweets (extract_initial_tweets_and_usernames.ipynb) for annotators to handle, where applicable, and then gather the historical tweets (get_development_data.py and get_experiment_data.py) as specified in the research paper.

2. Preprocessing: This contains three main sections: 
a) Language Validation (language_validation.ipynb) used for filtering as per out main language of instruction requirement. 
b) Cleaning (Cleaning.ipynb) used for preprocessing of text as per preprocessing steps described in research paper. 
c) Dataset creation (development_creation.ipynb) used for creating the datasets, adding labels (where applicable) and creating specified sample representations (where necessary).
D) Annonimization of user identities inline with Twitter Developer user agreement.

3. Classifier Analysis and Monitoring:
- All files included in this section were run on Google's Colabratory environment and may be required for replication for the enhanced computing power.



Benchmark Classifier: Our Benchmark Classifier, Support Vector Machine (SVM), experiments were conducted in Dataset_experiment_SVM.ipynb

Classifier Experiment on U.K. Dataset: Classifier architectures were defined in exploring_models.ipynb to conduct the Classifier Experiment on U.K. Dataset as well as annotate datasets from other countries. The code for the BERT classifier implementation has been adapted from the supporting material of Queen Mary University of London's Neural Networks and NLP (ECS7001) delivered by Prof M Poessi and Dr M Purver.

tokenization.py is an auxiliary file used in the tokenization of inputs to the BERT model. This is not our own work but has rather been taken from the supporting materials of Queen Mary University of London's Neural Networks and NLP (ECS7001) delivered by Prof M Poessi and Dr M Purver. All credits relating to the code included in this file is reserevd to them. 

Significance testing: We use chi_squared.ipynb to conduct our Chi-squared significance test.

Temporal Mental Health Dynamics: We use Disp_exp_results.ipynb to calculate the rates of depression from annotated experiment datasets created in exploring_models.ipynb and visualise the temporal mental health dynamics.



Setup Specification:
Package                 Version       
----------------------- --------------
             
beautifulsoup4          4.9.1         
Cython                  0.29.15       
dateparser              0.7.6         
docopt                  0.6.2         
docplex                 2.12.182      
docutils                0.15.2        
GetOldTweets3           0.0.11        
iniconfig               1.0.1                       
ipykernel               5.1.4         
ipython                 7.12.0        
ipython-genutils        0.2.0         
Keras                   2.3.1         
Keras-Applications      1.0.8         
Keras-Preprocessing     1.1.0         
langdetect              1.0.8         
matplotlib              3.1.3         
nltk                    3.4.5         
notebook                6.0.3         
ntlm-auth               1.4.0         
numpy                   1.18.1        
pandas                  1.0.1         
Pillow                  7.0.0         
pip                     19.2.3                
python-dateutil         2.8.1         
regex                   2020.7.14     
reportlab               3.5.34        
requests                2.24.0              
scikit-learn            0.22.1        
scipy                   1.4.1         
sentencepiece           0.1.91        
setuptools              41.2.0        
tensorflow              1.15.0        
tensorflow-estimator    1.15.1        
tensorflow-hub          0.7.0         
tokenizers              0.8.1rc1      
tornado                 6.0.3         
tqdm                    4.43.0        
tweepy                  3.8.0         
tweet-preprocessor      0.5.0         
Twisted                 20.3.0        
urllib3                 1.25.8        
Werkzeug                1.0.0         
wheel                   0.34.2 
