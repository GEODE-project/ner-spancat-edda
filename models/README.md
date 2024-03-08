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
doc = nlp("* ALBI, (Géog.) ville de France, capitale de l'Albigeois, dans le haut Languedoc : elle est sur le Tarn. Long. 19. 49. lat. 43. 55. 44.")

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
 {'start': 58, 'end': 62, 'labels': ['Relation'], 'text': 'dans'},
 {'start': 92, 'end': 95, 'labels': ['Relation'], 'text': 'sur'},
 {'start': 9, 'end': 14, 'labels': ['Domain-mark'], 'text': 'Géog.'},
 {'start': 45, 'end': 56, 'labels': ['NP-Spatial'], 'text': "l'Albigeois"},
 {'start': 96, 'end': 103, 'labels': ['NP-Spatial'], 'text': 'le Tarn'},
 {'start': 16,
  'end': 31,
  'labels': ['ENE-Spatial'],
  'text': 'ville de France'},
 {'start': 63,
  'end': 80,
  'labels': ['NP-Spatial'],
  'text': 'le haut Languedoc'},
 {'start': 33,
  'end': 56,
  'labels': ['ENE-Spatial'],
  'text': "capitale de l'Albigeois"},
 {'start': 33,
  'end': 80,
  'labels': ['ENE-Spatial'],
  'text': "capitale de l'Albigeois, dans le haut Languedoc"},
 {'start': 16,
  'end': 80,
  'labels': ['ENE-Spatial'],
  'text': "ville de France, capitale de l'Albigeois, dans le haut Languedoc"}]
```


### Evaluation

Evaluation is performed using the spacy [evaluate](https://spacy.io/api/cli#evaluate) command line interface:

* Overall model performances (Test set)


|   | Precision | Recall | F-score |
|---|:---:|:---:|:---:|
|    | 94.09   | 79.91   | 86.42 | 



* Model performances by entity (Test set)

|   | Precision | Recall | F-score |
|---|:---:|:---:|:---:|
| NC-Spatial    |  96.50  |  93.24  |  94.84 |
| NP-Spatial    |  92.74  |  95.95  |  94.32 |
| ENE-Spatial   |  91.67  |  95.51  |  93.55 |
| Relation      |  97.33  |  64.60  |  77.66 |
| Latlong       |  0.00   |  0.00   |  0.00  |
| NC-Person     |  93.07  |  70.68  |  80.34 |
| NP-Person     |  92.47  |  90.00  |  91.22 |
| ENE-Person    |  92.16  |  82.46  |  87.04 |
| NP-Misc       |  93.24  |  71.88  |  81.18 |
| ENE-Misc      |  0.00   |  0.00   |  0.00  |
| Head          |  97.37  |  24.18  |  38.74 |
| Domain-mark   |  99.19  |  91.73  |  95.31 |