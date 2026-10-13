"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#OAuthCustomParameters``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.o_auth_custom_parameters_key
    import capo_bedrock_agentcore.types.o_auth_custom_parameters_value

OAuthCustomParameters: TypeAlias = dict[
    "capo_bedrock_agentcore.types.o_auth_custom_parameters_key.OAuthCustomParametersKey",
    "capo_bedrock_agentcore.types.o_auth_custom_parameters_value.OAuthCustomParametersValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: OAuthCustomParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> OAuthCustomParameters:
    out: OAuthCustomParameters = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: OAuthCustomParameters) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
