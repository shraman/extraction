import nltk
import os
import re
import sys
from pprint import pprint
from nltk.corpus import stopwords

def filter(tokens):
  stop_words = stopwords.words('english')
  stemmer = nltk.PorterStemmer()

  number = re.compile(r'^[0-9]*\.?$')

  filtered = []
  for token in tokens:
    if len(token) == 1:
      continue
    if number.match(token):
      continue
    if token in stop_words:
      continue

    token = stemmer.stem(token)
    filtered.append(token)
  return filtered

def sent_to_tokens(sent):
  return filter(nltk.word_tokenize(sent))

def get_sent_score(sent,target_tokens):
  sent_tokens = sent_to_tokens(sent)
  score = 0
  for token in sent_tokens:
    if token in target_tokens:
      score += 1
  return (sent,score)


def get_text_files():
  textfiles = []
  files = os.listdir('./input/')
  for file in files:
    if(file.endswith('.txt')):
      textfiles.append(file)
  return textfiles

# for each in  get_text_files():
#   print each

def get_scores():
  incl_sents = open("./excl_sents.txt").read().splitlines()
  count = 0

  for each in get_text_files():
    incl_sent = incl_sents[count]
    count += 1

    print each
    print incl_sent
    
    if incl_sent=="--":
      continue

    target_tokens = sent_to_tokens(incl_sent)

    for token in target_tokens:
      print token

    sents = open("./input/"+each).read().decode('utf8').splitlines()
    scores = [ get_sent_score(sent,target_tokens) for sent in sents]

    scores = sorted(scores, key=lambda item: item[1], reverse=True)

    out_file = open("./results_excl/"+each.replace('.txt','')+"_scores.txt",'w')

    out_file.write(incl_sent+'\n')

    for score in scores:
      out_file.write(score[0]+"\n"+"score --> "+str(score[1])+"\n")




if __name__=="__main__":

  reload(sys)
  sys.setdefaultencoding('utf8')

  get_scores()

  # inclusion = "COPD clinically stable between 55 and 85 y unaccustomed of a walking aid presence of associated medical conditions that limited exercise tolerance; inability to communicate English"

  # tokens = nltk.word_tokenize(inclusion)
  # target_tokens = filter(tokens)

  # for token in target_tokens:
  #   print token

  # sents = open("./input/"+sys.argv[1]+".txt").read().decode('utf8').splitlines()
  # scores = [score(sent,target_tokens) for sent in sents]

  # scores = sorted(scores, key=lambda item: item[1], reverse=True)

  # out_file = open("./results/"+sys.argv[1]+"_scores.txt",'w')
  # for score in scores:
  #   out_file.write(score[0]+"\n"+"score --> "+str(score[1])+"\n")

  # pprint(scores)

