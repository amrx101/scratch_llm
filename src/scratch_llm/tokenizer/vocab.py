"""
This file is responsible for creating a vocabulary from the source text file. Each token in the source
text file is to be assigned a tokenID(numerical ID). A token can be repeated several times in the source file.

Hence we need a vocab(a dict) which maps the token to its token_id.

Text File -> Consists of Tokens.
Vocab is an enumeration of unique of tokens.
"""
import re
from typing import Dict

class Vocab:

    def __init__(self, src_filename: str):
        self._filename = src_filename
        self._vocab: Dict[str, int] = {}
        self._vocab_size: int = 0
        self._create_vocab()

    def _create_vocab(self):
        with open(self._filename, "r", encoding="utf-8") as fp:
            raw_text = fp.read()

        if not raw_text:
            print("no source text file")
            return

        pre_processed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
        pre_processed = [item.strip() for item in pre_processed if item.strip()]

        all_words = sorted(set(pre_processed))
        self._vocab_size = len(all_words)
        for index, word in enumerate(all_words):
            self._vocab[word] = index
