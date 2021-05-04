# Scraping News Articles Using Selenium

## **Libraries and packages used**
  
  
### **1. Selenium**
Selenium is an open-source web-based automation tool.

    pip install Selenium 

### **2. Chrome WebDriver**
[Download](https://chromedriver.chromium.org/downloads) the version depending on your chrome version that you are using

Then you have multiple [options](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.chrome.webdriver):\
* put it in the same directory as your python script\
* specify the location directly via executable_path\

        driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")


### **3.Valence Aware Dictionary and sEntiment Reasoner**  

**VADER** Sentiment Analysis. VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media, and works well on texts from other domains.


    pip install vaderSentiment


### 4.  **Latent Dirichlet Allocation (LDA)** 

Latent Dirichlet Allocation (LDA) is an example of topic model and is used to classify text in a document to a particular topic. It builds a topic per document model and words per topic model, modeled as Dirichlet distributions.

**Gensim** is a Python library for topic modelling, document indexing and similarity retrieval with large corpora. Target audience is the natural language processing (NLP) and information retrieval (IR) community

    pip install gensim