
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt  
import pandas
import numpy as np

with open('spool-teste.txt', 'r') as infile:
    true_values = infile.read()
    true_values = list(true_values)
with open('detectado.txt', 'r') as infile:
    predictions = infile.read()
    predictions = list(predictions)

labels = ['A','B','C','D','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','-','!',')','(','0','1','2','3','4','5','6','7','8','9'] #PREENCHER COM O ALFABETO CORRESPONDENTE

cm = confusion_matrix(true_values, predictions, labels)

print(cm)


fig, ax = plt.subplots()
im = ax.imshow(cm)


ax.set_xticks(np.arange(len(labels)))
ax.set_yticks(np.arange(len(labels)))
ax.set_xticklabels(labels)
ax.set_yticklabels(labels)

# labels
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# por o valor nas celulas
for i in range(len(labels)):
    for j in range(len(labels)):
        text = ax.text(j, i, cm[i, j],
                       ha="center", va="center", color="w", size="smaller")

ax.set_title("Matriz")
fig.tight_layout()

plt.show()