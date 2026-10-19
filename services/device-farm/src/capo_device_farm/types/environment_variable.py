"""Generated from Smithy shape ``com.amazonaws.devicefarm#EnvironmentVariable``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.environment_variable_name
    import capo_device_farm.types.environment_variable_value


class EnvironmentVariable(TypedDict, closed=True):
    name: "capo_device_farm.types.environment_variable_name.EnvironmentVariableName"
    """<p>The name of the environment variable.</p>"""
    value: "capo_device_farm.types.environment_variable_value.EnvironmentVariableValue"
    """<p>The value of the environment variable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentVariable) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentVariable:
    out: EnvironmentVariable = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
