"""Generated from Smithy shape ``com.amazonaws.securityagent#ProviderType``."""

from typing import Literal, TypeAlias, cast

"""<p>Type of provider integration.</p>"""
ProviderType: TypeAlias = Literal[
    "SOURCE_CODE",
    "DOCUMENTATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProviderType) -> str:
    return value


def deserialize_json(data: str) -> ProviderType:
    return cast(ProviderType, data)
