Target_prediction
===================
__Author__: tlsun@pku.edu.cn<br>
__Usage__:
- 1.embedding created named 'seq_emb'<br>
python embed.py HLA-Vec_Object sequence_file
- 2.the prediction result will be written in file 'prediction_result'<br>
python test_w2v_LR.py seq_emb

__Requirements__:
- Python 2.7.14
- numpy1.13.3
- scikit_learn0.19.1
- gensim 3.1.0<br>

__Notes__:
- This is a program to predict druggable targets by using 3-gram word2vec and Logistic Regression.- 
- The trained embedding files HLA-Vec_Object did not contain 'WWC'. Therefore, this program could not predict sequences containing 'WWC'.
