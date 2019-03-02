from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from sematch.semantic.similarity import WordNetSimilarity
wns = WordNetSimilarity()

def getSimilarity(descMentee,splMentor):
    stop_words = set(stopwords.words('english')) 
  
    word_tokens = word_tokenize(descMentee) 

    filtered_sentence = [w for w in word_tokens if not w in stop_words] 

    filtered_sentence = [] 

    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w) 


    descMentee=" ".join(filtered_sentence)
    from rake_nltk import Rake

    r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.

    r.extract_keywords_from_text(descMentee)

    tfr = r.get_ranked_phrases() 
    
    for word in range(len(splMentor)):
        for word2 in range(len(tfr)):


            tfrw = tfr[word2].split(" ")
            for word3 in range(len(tfrw)):

                if(wns.word_similarity(splMentor[word], tfrw[word3]) > 0.7):
                    print(splMentor[word], tfrw[word3])
                    print("matched")



descMentee="If you’re a fan of tinkering and solving a problem, starting a plumbing, electrician work, or general handyperson-type business might be a good fit for you. While it’s not as simple as, hey, go start plumbing, if you’re looking for a hands-on career, you might want to consider seeking out a vocational degree in one of these fields and building a business around it. I’ve also linked our free sample plans below, including one specific to starting a plumbing business."
splMentor = ['linesman','plumber']

getSimilarity(descMentee,splMentor)
