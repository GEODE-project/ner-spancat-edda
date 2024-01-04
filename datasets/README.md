# Datasets

**Diderot & d’Alembert’s Encyclopédie**: Gold Standard Corpus for Named Entity Recognition and Span Categorization Annotations.


## Download

The dataset can be downloaded from the current [Github repository](https://github.com/GEODE-project/ner-spancat-edda/tree/main/datasets) and will be available on Zenodo soon.
The dataset is available in the following formats[^1]: 
* JSONL format provided by [Prodigy](https://prodi.gy)
* binary spaCy format (ready to use with the spaCy train pipeline)


[^1]: This is a work in progress. The dataset will be available in other formats soon.



## Dataset overview

The Gold Standard dataset is composed of 2200 paragraphs out of 2001 Encyclopédie's entries randomly selected. 
All paragraphs were written in French and are distributed as follows among the Encyclopédie knowledge domains:

| Knowledge domain | Paragraphs | 
|---|:---:|
| Géographie | 1096 | 
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
|Paragraphs| 1800 | 200 | 200|
| Tokens | 135857 | 15360 | 14271 |
| NC-Spatial | 3268 | 358 | 357 |
| NP-Spatial | 4719 | 464 | 522 |
| ENE-Spatial | 3044 | 326 | 334 |
| Relation | 2101 | 220 | 226 |
| Latlong | 553 | 66 | 72 |
| NC-Person | 1378 | 132 | 133 |
| NP-Person | 1603 | 170 | 150 |
| ENE-Person | 491 | 49 | 57 |
| NP-Misc | 953 | 108 | 96 |
| ENE-Misc | 255 | 31 | 22 |
| Head | 1264 | 143 | 154 |
| Domain-Mark | 1069 | 122 | 133 |

