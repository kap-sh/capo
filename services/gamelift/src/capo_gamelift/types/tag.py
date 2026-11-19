"""Generated from Smithy shape ``com.amazonaws.gamelift#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.tag_key
    import capo_gamelift.types.tag_value


class Tag(TypedDict, closed=True):
    key: NotRequired["capo_gamelift.types.tag_key.TagKey"]
    """<p>The key for a developer-defined key value pair for tagging an Amazon Web Services resource. </p>"""
    value: NotRequired["capo_gamelift.types.tag_value.TagValue"]
    """<p>The value for a developer-defined key value pair for tagging an Amazon Web Services resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
