# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    seq = seq.upper()
    transcribed_seq = ''
    for base in seq:
        if base not in ALLOWED_NUC:
            raise ValueError(f"Unidentified nucleotide {base} detected")
        transcribed_seq += TRANSCRIPTION_MAPPING[base]
    return(transcribed_seq)
    pass

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    seq = seq.upper()
    transcribed_seq = ''
    for base in seq:
        if base not in ALLOWED_NUC:
            raise ValueError(f"Unidentified nucleotide {base} detected")
        transcribed_seq += TRANSCRIPTION_MAPPING[base]
    return(transcribed_seq[::-1])
    pass