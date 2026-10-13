"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CustomRequestParametersType``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.custom_request_key_type
    import capo_bedrock_agentcore.types.custom_request_value_type

CustomRequestParametersType: TypeAlias = dict[
    "capo_bedrock_agentcore.types.custom_request_key_type.CustomRequestKeyType",
    "capo_bedrock_agentcore.types.custom_request_value_type.CustomRequestValueType",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CustomRequestParametersType) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> CustomRequestParametersType:
    out: CustomRequestParametersType = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: CustomRequestParametersType) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
