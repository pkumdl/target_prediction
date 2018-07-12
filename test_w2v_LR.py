import sys
import numpy as np
from sklearn.externals import joblib

def process(fname):
	data=np.loadtxt(fname)
	return data



if __name__=='__main__':

	f=open('predict_result','w')
	fname=sys.argv[1]
	data=process(fname)
	model=joblib.load("train_LR_ol")
	predict=model.predict(data)
	for i in predict:
		if i==1:
			f.write('target'+'\n')
		else:
			f.write('non-target'+'\n')


