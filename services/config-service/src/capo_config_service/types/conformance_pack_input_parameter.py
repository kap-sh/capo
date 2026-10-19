"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackInputParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.parameter_name
    import capo_config_service.types.parameter_value


class ConformancePackInputParameter(TypedDict, closed=True):
    parameter_name: "capo_config_service.types.parameter_name.ParameterName"
    """<p>One part of a key-value pair.</p>"""
    parameter_value: "capo_config_service.types.parameter_value.ParameterValue"
    """<p>Another part of the key-value pair. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackInputParameter) -> dict:
    out: dict = {}
    out["ParameterName"] = value["parameter_name"]
    out["ParameterValue"] = value["parameter_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackInputParameter:
    out: ConformancePackInputParameter = {}  # type: ignore[typeddict-item]
    if data.get("ParameterName") is not None:
        out["parameter_name"] = data["ParameterName"]
    else:
        out["parameter_name"] = ""
    if data.get("ParameterValue") is not None:
        out["parameter_value"] = data["ParameterValue"]
    else:
        out["parameter_value"] = ""
    return out
