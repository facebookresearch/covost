# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

import argparse
import os
import os.path as op
import urllib.request
from tqdm import tqdm

LANG_CODE_2_TO_3 = {
    'fr': 'fra', 'de': 'deu', 'nl': 'nld', 'ru': 'rus', 'en': 'eng', 'es': 'spa'
}


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=str, default='data/tt/mp3',
                        help='root path for MP3 files')
    return parser.parse_args()


def _download_mp3(root: str, lang: str, s_id: str, overwrite=False):
    path = op.join(root, f'{s_id}.mp3')
    if not overwrite and op.isfile(path):
        return
    url = f'https://audio.tatoeba.org/sentences/{lang}/{s_id}.mp3'
    try:
        urllib.request.urlretrieve(url, path)
    except Exception as e:
        print(e, url)
        return str(e)


def main():
    args = get_args()
    if not op.isdir(args.root):
        os.makedirs(args.root)

    for lang in LANG_CODE_2_TO_3:
        print(f'Downloading {lang} speeches...')
        lang_3 = LANG_CODE_2_TO_3[lang]
        with open(f'data/tt/tatoeba20191004.s2t.{lang}_en.tsv') as f:
            next(f)
            ids = [r.strip().split('\t')[0] for r in f]

        for i in tqdm(ids):
            _download_mp3(args.root, lang_3, i)


if __name__ == '__main__':
    main()
