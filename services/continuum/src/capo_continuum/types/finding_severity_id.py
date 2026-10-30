"""Generated from Smithy shape ``com.amazonaws.continuum#FindingSeverityId``."""

from typing import Literal, TypeAlias, cast

"""A finding's severity, on the canonical numeric scale OCSF defines (UNKNOWN=0, INFORMATIONAL=1, LOW=2, MEDIUM=3, HIGH=4, CRITICAL=5, FATAL=6, OTHER=99). Named rather than numeric so callers never map the scale themselves, and identical across producers."""
FindingSeverityId: TypeAlias = Literal[
    "UNKNOWN",
    "INFORMATIONAL",
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
    "FATAL",
    "OTHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingSeverityId) -> str:
    return value


def deserialize_json(data: str) -> FindingSeverityId:
    return cast(FindingSeverityId, data)
