CoVoST: A Diverse Multilingual Speech-To-Text Translation Corpus
======
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-green.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

CoVoST is built on [Common Voice](https://arxiv.org/abs/1912.06670) (2019-06-12 release). It includes speeches in
11 languages (French, German, Dutch, Russian, Spanish, Italian, Turkish, Persian, Swedish, Mongolian and Chinese),
their transcripts and English translations. We also provide an additional out-of-domain evaluation set
from [Tatoeba](https://tatoeba.org/eng) for 5 languages (French, German, Dutch, Russian and Spanish).

Please also check out [our paper](https://arxiv.org/abs/2002.01320) for more details.

<p align="center"><img src="stats.png" alt="CoVoST Statistics" width="640"></p>

## Getting Data

### CoVoST
1. Download the 2019-06-12 release of Common Voice (NOT the latest 2019-12-10 one from the web page) for speeches and transcripts:
    - [French (fr)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/fr.tar.gz)
    - [German (de)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/de.tar.gz)
    - [Dutch (nl)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/nl.tar.gz)
    - [Russian (ru)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/ru.tar.gz)
    - [Spanish (es)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/es.tar.gz)
    - [Italian (it)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/it.tar.gz)
    - [Turkish (tr)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/tr.tar.gz)
    - [Persian (fa)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/fa.tar.gz)
    - [Swedish (sv-SE)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/sv-SE.tar.gz)
    - [Mongolian (mn)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/mn.tar.gz)
    - [Chinese (zh-CN)](https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-3/zh-CN.tar.gz)

2. [Download translations](https://dl.fbaipublicfiles.com/covost/covost.zip) for all the 11 languages,
where `validated.<lang>_en.en` are matched with the transcripts in `validated.tsv`.

### Tatoeba Evaluation Data
1. [Download transcripts and translations](https://dl.fbaipublicfiles.com/covost/tatoeba.zip) and extract files
to `data/tt/*`.

2. Download speech data:
```bash
python get_tt_speech.py --root <mp3 download root (default to data/tt/mp3)>
```

## License
|  | License |
| ------------- |:-------------:|
| CoVoST data | [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/) |
| Tatoeba sentences | [CC BY 2.0 FR](https://creativecommons.org/licenses/by/2.0/fr/) |
| Tatoeba speeches | Various CC licenses (please check out `data/tt/tatoeba_s2t.<lang>_en.<lang>_lic`) |
| Anything else | [CC BY-NC 4.0](https://github.com/facebookresearch/covost/blob/master/LICENSE) |

## Citation
Please cite as
```
@misc{wang2020covost,
    title={CoVoST: A Diverse Multilingual Speech-To-Text Translation Corpus},
    author={Changhan Wang and Juan Pino and Anne Wu and Jiatao Gu},
    year={2020},
    eprint={2002.01320},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

## Contact
Changhan Wang ([changhan@fb.com](mailto:changhan@fb.com)),
Juan Miguel Pino ([juancarabina@fb.com](mailto:juancarabina@fb.com)),
Jiatao Gu ([jgu@fb.com](mailto:jgu@fb.com))
