Target_prediction
===================
__Author__: tlsun@pku.edu.cn<br>
__Usage__:
    embedding created named 'seq_emb'
- 1.python HLA-Vec_Object sequence_file
    the prediction result will be written in file 'prediction_result'
- 2.python test_w2v_LR.py seq_emb

__Requirements__:
- Python 2.7.14
- numpy1.13.3
- scikit_learn0.19.1
- gensim 3.1.0<br>

__Notes__:
- This is a program to predict druggable targets by using 3-gram word2vec and Logistic Regression.- 
- The trained embedding files HLA-Vec_Object did not contain 'WWC'. Therefore, this program could not predict sequences containing 'WWC'.
