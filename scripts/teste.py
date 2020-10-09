import numpy as np
from sklearn.metrics import precision_recall_fscore_support

with open('spool-teste.txt', 'r') as infile:
    true_values = infile.read()
    true_values = list(true_values)
with open('detectado.txt', 'r') as infile:
    predictions = infile.read()
    predictions = list(predictions)

labels = ['A','B','C','D','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','-','!',')','(','0','1','2','3','4','5','6','7','8','9'] #PREENCHER COM O ALFABETO CORRESPONDENTE

print (precision_recall_fscore_support(true_values, predictions, average='macro', labels=labels))
