"""Generated from Smithy shape ``com.amazonaws.directoryservice#Attribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.attribute_name
    import capo_directory_service.types.attribute_value


class Attribute(TypedDict, closed=True):
    name: NotRequired["capo_directory_service.types.attribute_name.AttributeName"]
    """<p>The name of the attribute.</p>"""
    value: NotRequired["capo_directory_service.types.attribute_value.AttributeValue"]
    """<p>The value of the attribute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Attribute) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Attribute:
    out: Attribute = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Attribute) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> Attribute:
    out: Attribute = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
