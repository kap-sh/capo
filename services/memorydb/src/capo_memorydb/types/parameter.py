"""Generated from Smithy shape ``com.amazonaws.memorydb#Parameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string


class Parameter(TypedDict, closed=True):
    name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the parameter</p>"""
    value: NotRequired["capo_memorydb.types.string.String"]
    """<p>The value of the parameter</p>"""
    description: NotRequired["capo_memorydb.types.string.String"]
    """<p>A description of the parameter</p>"""
    data_type: NotRequired["capo_memorydb.types.string.String"]
    """<p>The parameter's data type</p>"""
    allowed_values: NotRequired["capo_memorydb.types.string.String"]
    """<p>The valid range of values for the parameter.</p>"""
    minimum_engine_version: NotRequired["capo_memorydb.types.string.String"]
    """<p>The earliest engine version to which the parameter can apply.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Parameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    if "description" in value:
        out["Description"] = value["description"]
    if "data_type" in value:
        out["DataType"] = value["data_type"]
    if "allowed_values" in value:
        out["AllowedValues"] = value["allowed_values"]
    if "minimum_engine_version" in value:
        out["MinimumEngineVersion"] = value["minimum_engine_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Parameter:
    out: Parameter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DataType") is not None:
        out["data_type"] = data["DataType"]
    if data.get("AllowedValues") is not None:
        out["allowed_values"] = data["AllowedValues"]
    if data.get("MinimumEngineVersion") is not None:
        out["minimum_engine_version"] = data["MinimumEngineVersion"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Parameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    if "description" in value:
        out["Description"] = value["description"]
    if "data_type" in value:
        out["DataType"] = value["data_type"]
    if "allowed_values" in value:
        out["AllowedValues"] = value["allowed_values"]
    if "minimum_engine_version" in value:
        out["MinimumEngineVersion"] = value["minimum_engine_version"]
    return out


def deserialize_cbor(data: dict) -> Parameter:
    out: Parameter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DataType") is not None:
        out["data_type"] = data["DataType"]
    if data.get("AllowedValues") is not None:
        out["allowed_values"] = data["AllowedValues"]
    if data.get("MinimumEngineVersion") is not None:
        out["minimum_engine_version"] = data["MinimumEngineVersion"]
    return out
