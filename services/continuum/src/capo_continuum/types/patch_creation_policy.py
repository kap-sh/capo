"""Generated from Smithy shape ``com.amazonaws.continuum#PatchCreationPolicy``."""

from typing import Literal, TypeAlias, cast

"""Policy governing whether Continuum creates a patch for a proposed remediation."""
PatchCreationPolicy: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PatchCreationPolicy) -> str:
    return value


def deserialize_json(data: str) -> PatchCreationPolicy:
    return cast(PatchCreationPolicy, data)
