"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#EnvironmentVariableMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_microvms.types.environment_variable_key
    import capo_lambda_microvms.types.environment_variable_value

EnvironmentVariableMap: TypeAlias = dict[
    "capo_lambda_microvms.types.environment_variable_key.EnvironmentVariableKey",
    "capo_lambda_microvms.types.environment_variable_value.EnvironmentVariableValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EnvironmentVariableMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> EnvironmentVariableMap:
    out: EnvironmentVariableMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
