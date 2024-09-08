import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summerizer(rowdocs, reduction):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rowdocs)

    wordFrequency = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in wordFrequency.keys():
                wordFrequency[word.text] = 1
            else:
                wordFrequency[word.text] += 1

    maxFrequency = max(wordFrequency.values())
    for word in wordFrequency.keys():
        wordFrequency[word] = wordFrequency[word] / maxFrequency

    sent_token = [sent for sent in doc.sents]

    sent_score = {}
    for sent in sent_token:
        for word in sent:
            if word.text in wordFrequency.keys():
                if sent not in sent_score.keys():
                    sent_score[sent] = wordFrequency[word.text]
                else:
                    sent_score[sent] += wordFrequency[word.text]

    select_len = int(len(sent_token) / reduction)

    summary = nlargest(select_len, sent_score, key=sent_score.get)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    return summary, doc, len(rowdocs.split(' ')), len(summary.split(' '))
