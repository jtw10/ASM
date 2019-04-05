import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
from scrapers import *


def findfrequency(document, stopwords):
    word_frequencies = {}
    for word in document:
        if word.text not in stopwords and word.text not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1
    return word_frequencies


def summary(url):
    stopwords = list(STOP_WORDS)
    document1 = nbc_scraper(url)
    nlp = spacy.load("en_core_web_sm")

    docx = nlp(document1)

    # build word frequency
    # word.text is tokenization in spacy
    word_frequencies = findfrequency(docx, stopwords)

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
    # print(sentence_scores)

    summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
    # print(summarized_sentences)

    # convert sentences from spacy span to strings for joining entire sentence
    # for w in summarized_sentences:
    #     print(w.text)

    # List Comprehension of Sentences Converted From Spacy.span to strings
    final_sentences = [w.text for w in summarized_sentences]
    summary = ' '.join(final_sentences)
    return summary

    # print('The original document had', len(document1), 'words, the summary has', len(summary), 'words.')
