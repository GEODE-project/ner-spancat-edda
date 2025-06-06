# Diderot & d’Alembert’s Encyclopédie: Gold Standard Corpus for Named Entity Recognition and Span Categorization Annotations

This repository contains a gold standard corpus for named entity recognition and span categorization annotations from Diderot & d’Alembert’s Encyclopédie entries.

**Developed by:** [Ludovic Moncla](https://ludovicmoncla.github.io), [Katherine McDonough](https://www.lancaster.ac.uk/dsi/about-us/members/katherine-mcdonough#projects) and [Denis Vigier](http://www.icar.cnrs.fr/membre/dvigier/) within the framework of the [GEODE](https://geode-project.github.io) project.


## Dataset and methodology

### Tagset

- **NC-Spatial**: a common noun that identifies a spatial entity (nominal spatial entity) including natural features, e.g. `ville`, `la rivière`, `royaume`.
- **NP-Spatial**: a proper noun identifying the name of a place (spatial named entities), e.g. `France`, `Paris`, `la Chine`.
- **ENE-Spatial**: nested spatial entity , e.g. `ville de France`, `royaume de Naples`, `la mer Baltique`.
- **Relation**: spatial relation, e.g. `dans`, `sur`, `à 10 lieues de`.
- **Latlong**: geographic coordinates, e.g. `Long. 19. 49. lat. 43. 55. 44.`
- **NC-Person**: a common noun that identifies a person (nominal spatial entity), e.g. `roi`, `l'empereur`, `les auteurs`.
- **NP-Person**: a proper noun identifying the name of a person (person named entities), e.g. `Louis XIV`, `Pline`, `les Romains`.
- **ENE-Person**: nested people entity, e.g. `le czar Pierre`, `roi de Macédoine`
- **NP-Misc**: a proper noun identifying entities not classified as spatial or person, e.g. `l'Eglise`, `1702`, `Pélasgique`.
- **ENE-Misc**: nested named entity not classified as spatial or person, e.g. `l'ordre de S. Jacques`, `la déclaration du 21 Mars 1671`.
- **Head**: entry name
- **Domain-Mark**: words indicating the knowledge domain (usually after the head and between parenthesis), e.g. `Géographie`, `Geog.`, `en Anatomie`


### Dataset overview

The Gold Standard dataset is composed of 2,200 paragraphs out of 2,001 Encyclopédie's entries randomly selected. 
All paragraphs were written in French and are distributed as follows among the Encyclopédie knowledge domains:

| Knowledge domain | Paragraphs | 
|---|:---:|
| Géographie | 1,096 | 
| Histoire | 259 | 
| Droit Jurisprudence | 113 | 
| Physique | 92 | 
| Métiers | 92 | 
| Médecine | 88 | 
| Philosophie | 69 | 
| Histoire naturelle | 65 | 
| Belles-lettres | 65 | 
| Militaire | 62 | 
| Commerce | 48 | 
| Beaux-arts | 44 | 
| Agriculture | 36 | 
| Chasse | 31 | 
| Religion | 23 | 
| Musique | 17 | 


The spans/entities were labeled by the project team along with using pre-labelling with early models to speed up the labelling process. 
A train/val/test split was used.
Validation and test sets are composed of 200 paragraphs each: 100 classified as 'Géographie' and 100 from another knowledge domain.
The datasets have the following breakdown of tokens and spans/entities. 

|   | Train | Validation | Test|
|---|:---:|:---:|:---:|
|Paragraphs| 1,800 | 200 | 200|
| Tokens | 132,398 | 14,959 | 13,881 |
| NC-Spatial | 3,252 | 358 | 355 |
| NP-Spatial | 4,707 | 464 | 519 |
| ENE-Spatial | 3,033 | 326 | 334 |
| Relation | 2,093 | 219 | 226 |
| Latlong | 553 | 66 | 72 |
| NC-Person | 1,378 | 132 | 133 |
| NP-Person | 1,599 | 170 | 150 |
| ENE-Person | 492 | 49 | 57 |
| NP-Misc | 948 | 108 | 96 |
| ENE-Misc | 255 | 31 | 22 |
| Head | 1,261 | 142 | 153 |
| Domain-Mark | 1,069 | 122 | 133 |


### Download

The dataset can be downloaded from the current [Github repository](), Zenodo ([https://zenodo.org/records/10530178](https://zenodo.org/records/10530178)) and HuggingFace [https://huggingface.co/datasets/GEODE/GeoEDdA](https://huggingface.co/datasets/GEODE/GeoEDdA).
The dataset is available in the following formats[^1]: 
* JSONL format provided by [Prodigy](https://prodi.gy)
* binary spaCy format (ready to use with the spaCy train pipeline)


[^1]: This is a work in progress. The dataset will be available in other formats soon.




## spaCy Custom Spancat trained on Diderot & d’Alembert’s Encyclopédie entries

This dataset was used to train and evaluate a custom spancat model for French using [spaCy](https://spacy.io).
The model is available on HuggingFace's model hub: [https://huggingface.co/GEODE/fr_spacy_custom_spancat_edda](https://huggingface.co/GEODE/fr_spacy_custom_spancat_edda).



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


## Cite this work

> Moncla, L., Vigier, D., & McDonough, K. (2024). GeoEDdA: A Gold Standard Dataset for Geo-semantic Annotation of Diderot & d’Alembert’s Encyclopédie. In proceedings of the 2nd International Workshop on Geographic Information Extraction from Texts (GeoExT'24), ECIR Conference, Glasgow, UK.

> Moncla, L., Vigier, D., & McDonough, K. (2024). Diderot & d'Alembert's Encyclopédie: Gold Standard Corpus for Named Entity Recognition and Span Categorization Annotations (1.0.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.10530178



## Acknowledgement

The authors are grateful to the [ASLAN project](https://aslan.universite-lyon.fr) (ANR-10-LABX-0081) of the Université de Lyon, for its financial support within the French program "Investments for the Future" operated by the National Research Agency (ANR). Data courtesy the [ARTFL Encyclopédie Project](https://artfl-project.uchicago.edu), University of Chicago.