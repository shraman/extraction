import nltk
import os
import pprint
import sys  


def segment(filepath):
  raw = open(filepath).read().decode('utf8')
  raw = raw.replace('\n',' ')

  sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
  sents = sent_tokenizer.tokenize(raw)

  return sents

def get_text_files():
  textfiles = []
  files = os.listdir('./to_process/')
  for file in files:
    if(file.endswith('.txt')):
      textfiles.append(file)
  return textfiles

if __name__ == "__main__":

  reload(sys)
  sys.setdefaultencoding('utf8')

  textfiles = get_text_files()

  count = 0

  for file in textfiles:

    output_file_path = "./processed/"+file
    output_file = open(output_file_path, 'w')

    try:
      sents = segment('./to_process/'+file)
      print "done --> " + file
      count += 1
    except:
      print "problem --> " + file

    # output_file.write(file+"------")
    for sent in sents:
      output_file.write(sent + "\n")
    # output_file.write("--------------")

    output_file.close()

  print "successful --> " +str(count)


