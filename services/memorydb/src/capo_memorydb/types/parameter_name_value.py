"""Generated from Smithy shape ``com.amazonaws.memorydb#ParameterNameValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string


class ParameterNameValue(TypedDict, closed=True):
    parameter_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the parameter</p>"""
    parameter_value: NotRequired["capo_memorydb.types.string.String"]
    """<p>The value of the parameter</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterNameValue) -> dict:
    out: dict = {}
    if "parameter_name" in value:
        out["ParameterName"] = value["parameter_name"]
    if "parameter_value" in value:
        out["ParameterValue"] = value["parameter_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterNameValue:
    out: ParameterNameValue = {}  # type: ignore[typeddict-item]
    if data.get("ParameterName") is not None:
        out["parameter_name"] = data["ParameterName"]
    if data.get("ParameterValue") is not None:
        out["parameter_value"] = data["ParameterValue"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ParameterNameValue) -> dict:
    out: dict = {}
    if "parameter_name" in value:
        out["ParameterName"] = value["parameter_name"]
    if "parameter_value" in value:
        out["ParameterValue"] = value["parameter_value"]
    return out


def deserialize_cbor(data: dict) -> ParameterNameValue:
    out: ParameterNameValue = {}  # type: ignore[typeddict-item]
    if data.get("ParameterName") is not None:
        out["parameter_name"] = data["ParameterName"]
    if data.get("ParameterValue") is not None:
        out["parameter_value"] = data["ParameterValue"]
    return out
