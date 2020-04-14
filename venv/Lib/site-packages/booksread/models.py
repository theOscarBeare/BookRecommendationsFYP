"""
	We will train our predictive models here
	Load model and save model will be here
"""

import os
import pickle
import collections
from helpers import *

WORDS = []
WORD_TUPLES = []
WORDS_MODEL = {}
WORD_TUPLES_MODEL = {}

def train_models(corpus, model_name="models_compressed.pkl"):
	''' -> Take in a long string from training data
	    -> Split that string into a list
		-> 2-elem list - Dictionary where each key = first elem and each value = counter
		-> Will save model by 'model_compressed.pkl'
		-> Set second argument as False if you dont want to save model
	'''

	global WORDS
	WORDS = re_split(corpus)

	global WORDS_MODEL
	WORDS_MODEL = collections.Counter(WORDS)

	global WORD_TUPLES
	WORD_TUPLES = list(chunks(WORDS, 2))

	global WORD_TUPLES_MODEL
	WORD_TUPLES_MODEL = {first: collections.Counter() for first, second in WORD_TUPLES}

	for tup in WORD_TUPLES:
		try:
			WORD_TUPLES_MODEL[tup[0]].update([tup[1]])
		except:
			pass
	
	if model_name:
		save_model(os.path.join(os.path.dirname(__file__), model_name))

def save_model(path=None):
	if path == None:
		path = os.path.join(os.path.dirname(__file__), 'models_compressed.pkl')
	
	print("Saving to: ", path)
	pickle.dump({'words_model': WORDS_MODEL,
				'word_tuple_model': WORD_TUPLES_MODEL},
				open(path, 'wb'),
				protocol=2)

def load_models(load_path = None):
	'''work remain'''
	pass

def train_txt():
	'''work remain'''
	pass