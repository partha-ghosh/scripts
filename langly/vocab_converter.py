import json

with open('vocabulary2.json', 'r') as f:
    vocab = json.load(f) 

new_vocab = dict()
for lang_key in vocab:
    new_vocab.setdefault(lang_key, dict())
    for subsentence in vocab[lang_key]:
        meaning = vocab[lang_key][subsentence]['translation']
        new_vocab[lang_key][f"{(subsentence, meaning)}"] = dict(subsentence=subsentence, **vocab[lang_key][subsentence])


with open('vocabulary.json', 'w') as f:
    json.dump(new_vocab, f)
