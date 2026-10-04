"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FoundationModelConfigurationType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of foundation model configuration.</p>"""
FoundationModelConfigurationType: TypeAlias = Literal[
    "BEDROCK_FOUNDATION_MODEL",
    "MANTLE_FOUNDATION_MODEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: FoundationModelConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> FoundationModelConfigurationType:
    return cast(FoundationModelConfigurationType, data)
