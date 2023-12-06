# Convolutional Data Storage
Data storage using convolutional neural networks, implemented with Tensorflow 2.0.

# Current Results
1. Straightforward Approach: 
     - batchA: 
             - Epochs: 100
             - Accuracy: 97.826087474823
     - batchB:
             - Epochs: 50
             - Accuracy: 88.98147940635681
     - batchC:
             - Epochs: 10
             - Accuracy: 75.71428418159485
             - Duplicate Precision: 62.142857142857146
     - batchD:
             - Epochs: 5
             - Accuracy: 97.27280139923096
2. Directory Optimization Approach:
     - batchA:
             - Epochs: 100
             - Accuracy: 96.7391312122345
     - batchB:
             - Epochs: 50
             - Accuracy: 88.14814686775208
     - batchC:
             - Epochs: 100
             - Accuracy: 96.42857313156128
             - Duplicate Precision: 100.0
     - batchD:
             - Epochs: 5
             - Accuracy: 98.62837791442871
3. Fourier Features Approach:
     - batchA:
             - Epochs: 5
             - Accuracy: 98.36956262588501
     - batchB:
             - Epochs: 5
             - Accuracy: 91.4814829826355
     - batchC:
             - Epochs: 5
             - Accuracy: 76.42857432365417
             - Duplicate Precision: 62.857142857142854
     - batchD:
             - Epochs: 3
             - Accuracy: 92.41597652435303

# Citations
```
@misc{tancik2020fourier,
    title={Fourier Features Let Networks Learn High Frequency Functions in Low Dimensional Domains},
    author={Matthew Tancik and Pratul P. Srinivasan and Ben Mildenhall and Sara Fridovich-Keil and Nithin Raghavan and Utkarsh Singhal and Ravi Ramamoorthi and Jonathan T. Barron and Ren Ng},
    year={2020},
    eprint={2006.10739},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```

# Packages
 - tensorflow 2.10.1
 - numpy 1.23.5
