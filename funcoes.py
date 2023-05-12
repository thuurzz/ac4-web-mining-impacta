# importando uma das principais bibliotecas de tratamento de texto
import pandas as pd
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
# importando o modelo que vamos usar para classificar a frase
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')
nltk.download('stopwords')


def traduz(frase):
    exemplo = TextBlob(frase)
    exemplo = exemplo.translate(from_lang='pt', to='en')
    return exemplo


def trata(frase):
    text_tokens = word_tokenize(str(frase))
    tokens_without_sw = [
        word for word in text_tokens if not word in stopwords.words('portuguese')]
    filtered_sentence = (" ").join(tokens_without_sw)
    return filtered_sentence


def previsao(frase):
    exemplo = TextBlob(frase)
    polaridade = exemplo.sentiment[0]
    subjetividade = exemplo.sentiment[1]
    df = pd.DataFrame([[frase, polaridade, subjetividade]], columns=[
                      'frase', 'polaridade', 'subjetividade'])
    df['sentimento'] = 'neutro'
    df.loc[df.polaridade < -0.25, 'sentimento'] = 'negativo'
    df.loc[df.polaridade > 0.25, 'sentimento'] = 'positivo'
    return df.to_json('dados.json', orient='columns'), polaridade, subjetividade
