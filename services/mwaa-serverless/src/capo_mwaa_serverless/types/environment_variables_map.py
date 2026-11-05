"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#EnvironmentVariablesMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.environment_variable_key
    import capo_mwaa_serverless.types.environment_variable_value

EnvironmentVariablesMap: TypeAlias = dict[
    "capo_mwaa_serverless.types.environment_variable_key.EnvironmentVariableKey",
    "capo_mwaa_serverless.types.environment_variable_value.EnvironmentVariableValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: EnvironmentVariablesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> EnvironmentVariablesMap:
    out: EnvironmentVariablesMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: EnvironmentVariablesMap) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
