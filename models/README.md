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

* Overall model performances (Test set)

| Precision | Recall | F-score |
|:---:|:---:|:---:|
| 94.80 | 84.88 | 89.57 | 


* Model performances by entity (Test set)

|   | Precision | Recall | F-score |
|---|:---:|:---:|:---:|
| NC-Spatial    | 97.08   | 93.28   | 95.14 | 
| NP-Spatial    | 93.47   | 95.98   | 94.71 |
| ENE-Spatial   | 92.22   | 95.81   | 93.98 |
| Relation      | 96.69   | 64.60   | 77.45 |
| Latlong       |  0.00   |  0.00   |  0.00 |
| NC-Person     | 93.07   | 70.68   | 80.34 |
| NP-Person     | 93.06   | 89.33   | 91.16 |
| ENE-Person    | 92.16   | 82.46   | 87.04 |
| NP-Misc       | 93.24   | 71.88   | 81.18 |
| ENE-Misc      |  0.00   |  0.00   |  0.00 |
| Head          | 99.33   | 96.75   | 98.03 |
| Domain-mark   | 99.19   | 91.73   | 95.31 |
