# tf2-transformer
TensorFlow2 NLP transformer.  
No Keras used to create the model

## Requirements
Jupyter Notebook  

TensorFlow==2.12.0  
Sentencepiece==0.1.99  
TensorFlow-text==2.12.1  
Numpy==1.23.5  

## How to use
1. Download your dataset, save it to datasets/dataset.txt.
2. Run [train_bpe.py](https://github.com/ilnikolaev/tf2-transformer/blob/main/train_bpe.py) script on it, to create model vocabulary.
3. Split sentences in dataset with some special token.
4. Launch Google Colab or Jupyter Notebook on local machine and upload [spawn.ipynb] (https://github.com/ilnikolaev/tf2-transformer/blob/main/spawn.ipynb) to it with your vocabulary and dataset.
5. Define hyperparameters in this notebook to open dataset, create model and train it.
6. The model will be saved after training, download it if you using Google Colab, and run [sample.ipynb] (https://github.com/ilnikolaev/tf2-transformer/blob/main/sample.ipynb) with your model to perform top-k sampling and infer it.
