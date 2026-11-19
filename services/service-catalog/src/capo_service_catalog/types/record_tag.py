"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RecordTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.record_tag_key
    import capo_service_catalog.types.record_tag_value


class RecordTag(TypedDict, closed=True):
    key: NotRequired["capo_service_catalog.types.record_tag_key.RecordTagKey"]
    """<p>The key for this tag.</p>"""
    value: NotRequired["capo_service_catalog.types.record_tag_value.RecordTagValue"]
    """<p>The value for this tag.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordTag) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecordTag:
    out: RecordTag = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecordTag) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> RecordTag:
    out: RecordTag = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
