"""
Byte Pair Tokenizer.
Byte Pair Tokenizer that tokenizes tokens which are not part of vocab as well by breaking
it to smaller recongisable token
With our previous simple Tokenizer, all unknown tokens used to get the same  tokenID.
For example: str -> "Hello World"
And both Hello and World are not in Vocab, and so we <unknw>, <unkwn> for both
This makes token Id 79390, 79390 for both Hello and World tokens and many other tokens which were not part of the
vocab
"""

import tiktoken
from typing import List

class BytePairTokenizer:

    def __init__(self, *args, **kwargs):
        self._tokenizer = tiktoken.get_encoding("gpt2")

    def encode(self, text: str) -> List[int]:
        return self._tokenizer.encode(text)

    def decode(self, ids: List[str]) -> str:
        return self._tokenizer.decode(ids)
