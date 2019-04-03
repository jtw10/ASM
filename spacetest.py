import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

# GOTTA CHANGE ALL TEXT TO LOWER AND STRIP PUNCTUATION

# build a list of stopwords
stopwords = list(STOP_WORDS)

document1 ="""Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning.In its application across business problems, machine learning is also referred to as predictive analytics."""

document2 = """Our Father who art in heaven, hallowed be thy name. Thy kingdom come. Thy will be done, on earth as it is in heaven. Give us this day our daily bread; and forgive us our trespasses, as we forgive those who trespass against us; and lead us not into temptation, but deliver us from evil"""

nlp = spacy.load("en_core_web_sm")

# build an NLP object
docx = nlp(document1)

# tokenization of text
mytokens = [token.text for token in docx]

# build word frequency
# word.text is tokenization in spacy
word_frequencies = {}
for word in docx:
    if word.text not in stopwords:
        if word.text not in word_frequencies.keys():
            word_frequencies[word.text] = 1
        else:
            word_frequencies[word.text] += 1

# maximum word frequency
max_f = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/max_f)

# frequency table
# print(word_frequencies)

# sentence tokens
sentence_list = [sentence for sentence in docx.sents]

# sentence score via comparison between words and sentence
sentence_scores = {}
for sent in sentence_list:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

# sentence score table
print(sentence_scores)

summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
print(summarized_sentences)

# convert sentences from spacy span to strings for joining entire sentence
for w in summarized_sentences:
    print(w.text)

# List Comprehension of Sentences Converted From Spacy.span to strings
final_sentences = [w.text for w in summarized_sentences]
summary = ' '.join(final_sentences)
print(summary)

print('The original document had', len(document1), 'words, the summary has', len(summary), 'words.')

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
for token in doc:
    print(token.text, token.pos_, token.dep_)

