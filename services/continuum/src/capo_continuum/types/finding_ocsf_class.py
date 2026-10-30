"""Generated from Smithy shape ``com.amazonaws.continuum#FindingOcsfClass``."""

from typing import Literal, TypeAlias, cast

"""The OCSF Finding class a submitted document declared. Continuum validates against, and accepts, only these classes; a document declaring any other class_uid is rejected at CreateCodeFinding, so this is a closed set rather than a pass-through of OCSF's full class registry."""
FindingOcsfClass: TypeAlias = Literal[
    "VULNERABILITY_FINDING",
    "APPLICATION_SECURITY_POSTURE_FINDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingOcsfClass) -> str:
    return value


def deserialize_json(data: str) -> FindingOcsfClass:
    return cast(FindingOcsfClass, data)
