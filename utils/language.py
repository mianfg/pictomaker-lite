from enum import Enum

IMPORTANCES = ['VERB', 'NOUN', 'ADJ', 'ADV', 'DET', 'PRON', 'INTJ', 'CONJ', 'ADP', 'OTHER']
SIMPLIFIER = {
    'ADJ' :     "ADJ",
    'ADP' :     "ADP",
    'ADV' :     "ADV",
    'AUX' :     "VERB",
    'CONJ' :    "CONJ",
    'CCONJ' :   "CONJ",
    'DET' :     "DET",
    'INTJ' :    "INTJ",
    'NOUN' :    "NOUN",
    'NUM' :     "NOUN",
    'PART' :    "OTHER",
    'PRON' :    "PRON",
    'PROPN' :   "NOUN",
    'PUNCT' :   "OTHER",
    'SCONJ' :   "CONJ",
    'SYM' :     "OTHER",
    'VERB' :    "VERB",
    'X' :       "OTHER",
    'SPACE' :   "OTHER"     # space -- note: tokenizer deletes this
}

class POS(Enum):
    PRON = "PRON"
    CONJ = "CONJ"
    ADV = "ADV"
    ADP = "ADP"
    ADJ = "ADJ"
    VERB = "VERB"
    DET = "DET"
    INTJ = "INTJ"
    NOUN = "NOUN"
    OTHER = "OTHER"

class ISOString(Enum):
    EN = 'en'
    ES = 'es'
    PL = 'pl'

PACKAGES = {
    ISOString.EN: 'en_core_web_sm',
    ISOString.ES: 'es_core_news_sm',
    ISOString.PL: 'pl_core_news_sm'
}
