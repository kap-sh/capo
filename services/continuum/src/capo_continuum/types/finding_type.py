"""Generated from Smithy shape ``com.amazonaws.continuum#FindingType``."""

from typing import Literal, TypeAlias, cast

"""What kind of finding this is, and who produced it."""
FindingType: TypeAlias = Literal[
    "CONTINUUM_CODE_VULN",
    "CUSTOMER_CODE_VULN",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingType) -> str:
    return value


def deserialize_json(data: str) -> FindingType:
    return cast(FindingType, data)
