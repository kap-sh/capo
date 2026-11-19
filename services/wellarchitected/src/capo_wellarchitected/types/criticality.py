"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Criticality``."""

from typing import Literal, TypeAlias, cast

"""<p>The business criticality of an application context.</p>"""
Criticality: TypeAlias = Literal[
    "MISSION_CRITICAL",
    "BUSINESS_CRITICAL",
    "NON_CRITICAL",
    "TEST_DEVELOPMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: Criticality) -> str:
    return value


def deserialize_json(data: str) -> Criticality:
    return cast(Criticality, data)
