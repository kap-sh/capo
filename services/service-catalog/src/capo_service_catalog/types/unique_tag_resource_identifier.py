"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UniqueTagResourceIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.unique_tag_key
    import capo_service_catalog.types.unique_tag_value


class UniqueTagResourceIdentifier(TypedDict, closed=True):
    key: NotRequired["capo_service_catalog.types.unique_tag_key.UniqueTagKey"]
    """<p> A unique key that's attached to a resource. </p>"""
    value: NotRequired["capo_service_catalog.types.unique_tag_value.UniqueTagValue"]
    """<p> A unique value that's attached to a resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UniqueTagResourceIdentifier) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UniqueTagResourceIdentifier:
    out: UniqueTagResourceIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UniqueTagResourceIdentifier) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> UniqueTagResourceIdentifier:
    out: UniqueTagResourceIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
