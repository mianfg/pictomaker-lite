import spacy, requests, json, urllib
from utils.language import SIMPLIFIER, IMPORTANCES, PACKAGES


class PictoLanguage:
    def __init__(self):
        self.__NLP = {}

        for language in PACKAGES.keys():
            try:
                self.__NLP[language] = spacy.load(PACKAGES[language])
            except:
                spacy.cli.download(PACKAGES[language])
                self.__NLP[language] = spacy.load(PACKAGES[language])

    def pictograms(self, word, language):
        req = requests.get(f'https://api.arasaac.org/api/pictograms/{language.value}/bestsearch/{urllib.parse.quote(word)}')
        if req.status_code == 200:
            return [pic['_id'] for pic in json.loads(req.text)]
        else:
            return []

    def tokenize(self, sentence, language):
        """
        Tokenizes sentence into an array of PictoWords:
        """

        # iterate over words
        nlp = self.__NLP[language](sentence)

        split = sentence.split()
        tokens = [{
            'text': token.text,
            'lemma': token.lemma_,
            'pos': SIMPLIFIER[token.pos_],
            'arasaac_ids': self.pictograms(token.lemma_, language)
        } for token in nlp]
        tokens_pos = []

        i = 0
        for token in tokens:
            if split[i] == token['text']:
                tokens_pos.append(i)
                i += 1
            elif split[i].startswith(token['text']):
                tokens_pos.append(i)
                split[i] = split[i][len(token['text']):]
            else:
                print(f"ERROR tokenizing sentence \"{sentence}\"")

        findall = lambda list, element: [i for i, x in enumerate(list) if x == element]
        return [{
          'text': text,
          'pos': sorted([tokens[j]['pos'] for j in findall(tokens_pos, i)],
            key=lambda el: IMPORTANCES.index(el))[0],
          'lemma': "".join([tokens[j]['lemma'] for j in findall(tokens_pos, i)]),
          'arasaac_ids': list(set().union(*[tokens[j]['arasaac_ids'] for j in findall(tokens_pos, i)]))
        } for i, text in enumerate(sentence.split())]
