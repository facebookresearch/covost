CoVoST: A Large-Scale Multilingual Speech-To-Text Translation Corpus
======
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-green.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
<a href="https://colab.research.google.com/drive/11GK7k7G1CG1qHbdA9Pz1RtQ3vlCkuohV">
    <img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg?style=flat-square">
</a>


[End-to-end speech-to-text translation](https://github.com/kahne/SpeechTransProgress) (ST) has recently witnessed an
increased interest given its system simplicity, lower inference latency and less compounding errors compared to cascaded
ST (i.e. speech recognition + machine translation). End-to-end ST model training, however, is often hampered by the
lack of parallel data. Thus, we created [CoVoST](https://arxiv.org/abs/2002.01320), a large-scale multilingual ST corpus
based on [Common Voice](https://arxiv.org/abs/1912.06670), to foster ST research with the largest ever open dataset.
Its latest version covers translations from English into 15 languages---Arabic, Catalan, Welsh, German, Estonian, Persian,
Indonesian, Japanese, Latvian, Mongolian, Slovenian, Swedish, Tamil, Turkish, Chinese---and from 21 languages into English,
including the 15 target languages as well as Spanish, French, Italian, Dutch, Portuguese, Russian. It has total 2880 hours
of speech and is diversified with 78K speakers.

<p align="center"><img src="overview.png" alt="CoVoST Overview" width="480"></p>

Please check out our papers ([CoVoST 1](https://arxiv.org/abs/2002.01320), [CoVoST 2](https://arxiv.org/pdf/2007.10310)) for more details and
the [VizSeq example](https://colab.research.google.com/drive/11GK7k7G1CG1qHbdA9Pz1RtQ3vlCkuohV) for exploring CoVoST data.

<p align="center"><img src="stats2.png" alt="CoVoST Statistics" width="560"></p>

We also provide an additional out-of-domain evaluation set
from [Tatoeba](https://tatoeba.org/eng) for 5 languages (French, German, Dutch, Russian and Spanish) into English.

## What's New
- __2020-07-21__: CoVoST 2 released ([arXiv paper](https://arxiv.org/pdf/2007.10310)).
- __2020-02-27__: [Example](https://colab.research.google.com/drive/11GK7k7G1CG1qHbdA9Pz1RtQ3vlCkuohV) added for
exploring CoVoST data with [VizSeq](https://github.com/facebookresearch/vizseq).
- __2020-02-13__: [Paper](https://arxiv.org/abs/2002.01320) accepted to LREC 2020.
- __2020-02-07__: CoVoST released.

## Getting Data

### CoVoST 2
1. Get voice clips and transcripts from Common Voice 2019-12-10 release:
[French (fr)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/fr.tar.gz),
[German (de)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/de.tar.gz),
[Spanish (es)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/es.tar.gz),
[Catalan (ca)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/ca.tar.gz),
[Italian (it)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/it.tar.gz),
[Russian (ru)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/ru.tar.gz),
[Chinese (zh-CN)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/zh-CN.tar.gz),
[Portuguese (pt)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/pt.tar.gz),
[Persian (fa)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/fa.tar.gz),
[Estonian (et)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/et.tar.gz),
[Mongolian (mn)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/mn.tar.gz),
[Dutch (nl)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/nl.tar.gz),
[Turkish (tr)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/tr.tar.gz),
[Arabic (ar)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/ar.tar.gz),
[Swedish (sv-SE)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/sv-SE.tar.gz),
[Latvian (lv)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/lv.tar.gz),
[Slovenian (sl)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/sl.tar.gz),
[Tamil (ta)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/ta.tar.gz),
[Japanese (ja)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/ja.tar.gz),
[Indonesian (id)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/id.tar.gz),
[Welsh (cy)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-4-2019-12-10/cy.tar.gz).
2. Download [CoVoST 2 translations](https://dl.fbaipublicfiles.com/covost/covost2.zip),
where `validated.<lang>_en.en` and `validated.en_<lang>.<lang>` are matched with the transcripts in `validated.tsv`.

### CoVoST 1
1. Get voice clips and transcripts from Common Voice 2019-06-12 release:
[French (fr)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/fr.tar.gz),
[German (de)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/de.tar.gz),
[Dutch (nl)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/nl.tar.gz),
[Russian (ru)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/ru.tar.gz),
[Spanish (es)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/es.tar.gz),
[Italian (it)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/it.tar.gz),
[Turkish (tr)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/tr.tar.gz),
[Persian (fa)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/fa.tar.gz),
[Swedish (sv-SE)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/sv-SE.tar.gz),
[Mongolian (mn)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/mn.tar.gz),
[Chinese (zh-CN)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/zh-CN.tar.gz).

2. Download [CoVoST translations](https://dl.fbaipublicfiles.com/covost/covost.zip),
where `validated.<lang>_en.en` are matched with the transcripts in `validated.tsv`.

### Tatoeba Evaluation Data
1. [Download transcripts and translations](https://dl.fbaipublicfiles.com/covost/tatoeba.zip) and extract files
to `data/tt/*`.

2. Download speech data:
```bash
python get_tt_speech.py --root <mp3 download root (default to data/tt/mp3)>
```

## Exploring Data
[VizSeq Example](https://colab.research.google.com/drive/11GK7k7G1CG1qHbdA9Pz1RtQ3vlCkuohV)
<a href="https://colab.research.google.com/drive/11GK7k7G1CG1qHbdA9Pz1RtQ3vlCkuohV">
    <img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg?style=flat-square">
</a>

## License
|  | License |
| ------------- |:-------------:|
| CoVoST data | [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/) |
| Tatoeba sentences | [CC BY 2.0 FR](https://creativecommons.org/licenses/by/2.0/fr/) |
| Tatoeba speeches | Various CC licenses (please check out the "audio_license" column in `data/tt/tatoeba20191004.s2t.<lang>_en.tsv`) |
| Anything else | [CC BY-NC 4.0](https://github.com/facebookresearch/covost/blob/master/LICENSE) |

## Citation
Please cite as (CoVoST 2)
```
@misc{wang2020covost,
    title={CoVoST 2: A Massively Multilingual Speech-to-Text Translation Corpus},
    author={Changhan Wang and Anne Wu and Juan Pino},
    year={2020},
    eprint={2007.10310},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
and (CoVoST 1)
```
@inproceedings{wang-etal-2020-covost,
    title = "{C}o{V}o{ST}: A Diverse Multilingual Speech-To-Text Translation Corpus",
    author = "Wang, Changhan  and
      Pino, Juan  and
      Wu, Anne  and
      Gu, Jiatao",
    booktitle = "Proceedings of The 12th Language Resources and Evaluation Conference",
    month = may,
    year = "2020",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://www.aclweb.org/anthology/2020.lrec-1.517",
    pages = "4197--4203",
    abstract = "Spoken language translation has recently witnessed a resurgence in popularity, thanks to the development of end-to-end models and the creation of new corpora, such as Augmented LibriSpeech and MuST-C. Existing datasets involve language pairs with English as a source language, involve very specific domains or are low resource. We introduce CoVoST, a multilingual speech-to-text translation corpus from 11 languages into English, diversified with over 11,000 speakers and over 60 accents. We describe the dataset creation methodology and provide empirical evidence of the quality of the data. We also provide initial benchmarks, including, to our knowledge, the first end-to-end many-to-one multilingual models for spoken language translation. CoVoST is released under CC0 license and free to use. We also provide additional evaluation data derived from Tatoeba under CC licenses.",
    language = "English",
    ISBN = "979-10-95546-34-4",
}
```

## Contact
Changhan Wang ([changhan@fb.com](mailto:changhan@fb.com)),
Juan Miguel Pino ([juancarabina@fb.com](mailto:juancarabina@fb.com)),
Jiatao Gu ([jgu@fb.com](mailto:jgu@fb.com))
