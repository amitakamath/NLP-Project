import nltk
from nltk.corpus import wordnet

def containsAntonym(word, maybe_ant_list):
	synonyms = []
	antonyms = []

	for syn in wordnet.synsets(word):
		for l in syn.lemmas():
			synonyms.append(l.name())
			if l.antonyms():
				antonyms.append(l.antonyms()[0].name())

	for maybe_ant in maybe_ant_list:
		if maybe_ant in antonyms:
			return True

	return False



def containsAntonym2(word, maybe_ant_list):
	for maybe_ant in maybe_ant_list:
		synonyms = []
		antonyms = []
		for syn in wordnet.synsets(maybe_ant):
			for l in syn.lemmas():
				synonyms.append(l.name())
				if l.antonyms():
					antonyms.append(l.antonyms()[0].name())
		if word in antonyms:
			return True

	return False


def containsSynonym(word, maybe_syn_list):
	synonyms = []

	for syn in wordnet.synsets(word):
		for l in syn.lemmas():
			synonyms.append(l.name())

	for maybe_syn in maybe_syn_list:
		if maybe_syn in synonyms:
			return True

	return False


def containsSynonym2(word, maybe_syn_list):
	for maybe_syn in maybe_syn_list:
		synonyms = []
		for syn in wordnet.synsets(maybe_syn):
			for l in syn.lemmas():
				synonyms.append(l.name())
			
		if word in synonyms:
			return True

	return False


"""




"""