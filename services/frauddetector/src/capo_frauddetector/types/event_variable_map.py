"""Generated from Smithy shape ``com.amazonaws.frauddetector#EventVariableMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.variable_name
    import capo_frauddetector.types.variable_value

EventVariableMap: TypeAlias = dict[
    "capo_frauddetector.types.variable_name.variableName",
    "capo_frauddetector.types.variable_value.variableValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: EventVariableMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> EventVariableMap:
    out: EventVariableMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: EventVariableMap) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
