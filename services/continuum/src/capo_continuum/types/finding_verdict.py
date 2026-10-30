"""Generated from Smithy shape ``com.amazonaws.continuum#FindingVerdict``."""

from typing import Literal, TypeAlias, cast

"""A validator's conclusion about whether a finding is real."""
FindingVerdict: TypeAlias = Literal[
    "TRUE_POSITIVE",
    "FALSE_POSITIVE",
    "BENIGN_TRUE_POSITIVE",
    "NEEDS_REVIEW",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingVerdict) -> str:
    return value


def deserialize_json(data: str) -> FindingVerdict:
    return cast(FindingVerdict, data)
