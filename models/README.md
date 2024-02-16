# Models

* spaCy Custom Spancat trained on Diderot & d’Alembert’s Encyclopédie entries



## spaCy Custom Spancat trained on Diderot & d’Alembert’s Encyclopédie entries

The Gold Standard dataset was used to train and evaluate a custom spancat model for French using [spaCy](https://spacy.io).
The model is also available on HuggingFace's model hub: [https://huggingface.co/GEODE/fr_spacy_custom_spancat_edda](https://huggingface.co/GEODE/fr_spacy_custom_spancat_edda).


### How to Get Started with the model

Use the code below to get started with the model.

```bash
pip install https://huggingface.co/GEODE/fr_spacy_custom_spancat_edda/resolve/main/fr_spacy_custom_spancat_edda-any-py3-none-any.whl
```

```python
# Using spacy.load().
import spacy
nlp = spacy.load("fr_spacy_custom_spancat_edda")

# Importing as module.
import fr_spacy_custom_spancat_edda
nlp = fr_spacy_custom_spancat_edda.load()
doc = nlp("* ALBI, (Géog.) ville de France, capitale de  l'Albigeois, dans le haut Languedoc : elle est sur le Tarn. Long. 19. 49. lat. 43. 55. 44.")

spans = []

for span in doc.spans['sc']:
  spans.append({
      "start": span.start_char,
      "end": span.end_char,
      "labels": [span.label_],
      "text": span.text
  })

print(spans)

# Output
[{'start': 2, 'end': 6, 'labels': ['Head'], 'text': 'ALBI'},
 {'start': 16, 'end': 21, 'labels': ['NC-Spatial'], 'text': 'ville'},
 {'start': 25, 'end': 31, 'labels': ['NP-Spatial'], 'text': 'France'},
 {'start': 33, 'end': 41, 'labels': ['NC-Spatial'], 'text': 'capitale'},
 {'start': 59, 'end': 63, 'labels': ['Relation'], 'text': 'dans'},
 {'start': 93, 'end': 96, 'labels': ['Relation'], 'text': 'sur'},
 {'start': 9, 'end': 14, 'labels': ['Domain-mark'], 'text': 'Géog.'},
 {'start': 46, 'end': 57, 'labels': ['NP-Spatial'], 'text': "l'Albigeois"},
 {'start': 97, 'end': 104, 'labels': ['NP-Spatial'], 'text': 'le Tarn'},
 {'start': 16,
  'end': 31,
  'labels': ['ENE-Spatial'],
  'text': 'ville de France'},
 {'start': 64,
  'end': 81,
  'labels': ['NP-Spatial'],
  'text': 'le haut Languedoc'},
 {'start': 33,
  'end': 57,
  'labels': ['ENE-Spatial'],
  'text': "capitale de  l'Albigeois"},
 {'start': 33,
  'end': 81,
  'labels': ['ENE-Spatial'],
  'text': "capitale de  l'Albigeois, dans le haut Languedoc"},
 {'start': 16,
  'end': 81,
  'labels': ['ENE-Spatial'],
  'text': "ville de France, capitale de  l'Albigeois, dans le haut Languedoc"}]
```


### Evaluation

Evaluation is performed using the spacy [evaluate](https://spacy.io/api/cli#evaluate) command line interface:

* Overall model performances (Test set)


| Precision | Recall | F-score |
|:---:|:---:|:---:|
| 88.33   | 79.40   | 83.63 | 



* Model performances by entity (Test set)

|   | Precision | Recall | F-score |
|---|:---:|:---:|:---:|
| NC-Spatial    |  89.21  |  93.01  |  91.07 |
| NP-Spatial    |  87.34  |  96.30  |  91.60 |
| ENE-Spatial   |  85.30  |  96.42  |  90.52 |
| Relation      |  87.42  |  62.56  |  72.93 |
| Latlong       |  0.00   |  0.00   |  0.00  |
| NC-Person     |  92.08  |  70.45  |  79.83 |
| NP-Person     |  90.34  |  89.12  |  89.73 |
| ENE-Person    |  90.20  |  82.14  |  85.98 |
| NP-Misc       |  90.54  |  72.04  |  80.24 |
| ENE-Misc      |  0.00   |  0.00   |  0.00  |
| Head          |  76.92  |  20.83  |  32.79 |
| Domain-mark   |  95.93  |  91.47  |  93.65 |
