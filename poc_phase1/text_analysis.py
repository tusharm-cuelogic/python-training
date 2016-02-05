from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

text = '''
I am very good but vey bad at heart
'''

blob = TextBlob(text)
#blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

#blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])

#for sentence in blob.sentences:
    #print(sentence.sentiment.polarity)

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

print blob.sentiment
print blob.sentiment[0]