"""
This file is responsible for a very simple Tokenizer class is initialized using a vocabulary enumeration.

The  class is  initialized with a Vocabulary with tokens and its token id.

The class is responsible to provide encode and decode methods.

Requirements:
    The encode method is used to convert tokens(string) to tokenIDs(numbers).
    The decode method is used to convert tokenIDs to tokens.
    The class should be able to handle tokens which are not part of the vocabulary.

"""
import re
from typing import Dict, List


class SimpleTokenizer:

    def __init__(self, vocab: Dict[str, int]):


        self._str_to_int = vocab
        self._int_to_str = {v: k for k, v in self._str_to_int.items()}

    def encode(self, text: str) -> List[int]:
        """
        Encode the string to tokens
        :param text: str
        :return: List of token ids
        """

        pre_processed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        pre_processed = [
            item.strip() for item in pre_processed if item.strip()
        ]
        pre_processed = [item if item in self._str_to_int else "<unk>" for item in pre_processed]
        ids = [self._str_to_int[item] for item in pre_processed]
        return ids


    def decode(self, ids: List[int]) -> str:
        text = " ".join([self._int_to_str[item] for item in ids])

        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
        return text