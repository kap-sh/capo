"""Generated from Smithy shape ``com.amazonaws.continuum#IntegrationType``."""

from typing import Literal, TypeAlias, cast

"""The immutable provider type for an integration."""
IntegrationType: TypeAlias = Literal[
    "GITHUB",
    "GITLAB",
    "S3",
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationType) -> str:
    return value


def deserialize_json(data: str) -> IntegrationType:
    return cast(IntegrationType, data)
