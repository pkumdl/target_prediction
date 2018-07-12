import numpy as np
from gensim.models import Word2Vec
import os
from sklearn import preprocessing
import sys

def ol_gram(fname):
	set1=[]
	set2=[]
	f=open(fname)
	for i in f.readlines():
		i=i.strip()
		for j in range(0,len(list(i))-2):
			set1.append(''.join(list(i)[j:j+3]))
		set2.append(set1)
	return set2

def hla(parameter):
	hla_vec_obj = Word2Vec.load(parameter)
	return hla_vec_obj.wv

def embedding(train_data,hla_weight):
	new=[]
	for i in train_data:
		k=[]
		for j in i:
			indiv=hla_weight[j]
			k.append(indiv)
		k1=np.array(k)
		k2=k1.sum(axis=0)
		k3=k2.tolist()
		new.append(k3)
	new1=np.array(new)
	return new1

def norm(train_data_emb,dim):
	l=train_data_emb.shape[0]
	a=np.zeros((l,dim))
	for i in range(0,l):
		for j in range(0,dim):
			a[i,j]=(train_data_emb[i,j]-np.min(train_data_emb[i,:]))/(np.max(train_data_emb[i,:])-np.min(train_data_emb[i,:]))
	return a

if __name__=='__main__':
	dim=200
	parameter=sys.argv[1]   #trained w2v
	data=sys.argv[2]        #sequence
	data_process=ol_gram(data)
	hla_weight=hla(parameter)
	data_embedding=embedding(data_process,hla_weight)
	data_norm=norm(data_embedding,dim)
	np.savetxt('try1',data_norm,'%.3f')
