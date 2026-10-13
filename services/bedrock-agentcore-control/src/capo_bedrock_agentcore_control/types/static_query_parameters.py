"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StaticQueryParameters``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.static_query_parameter_name
    import capo_bedrock_agentcore_control.types.static_query_parameter_value

StaticQueryParameters: TypeAlias = dict[
    "capo_bedrock_agentcore_control.types.static_query_parameter_name.StaticQueryParameterName",
    "capo_bedrock_agentcore_control.types.static_query_parameter_value.StaticQueryParameterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: StaticQueryParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> StaticQueryParameters:
    out: StaticQueryParameters = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: StaticQueryParameters) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
