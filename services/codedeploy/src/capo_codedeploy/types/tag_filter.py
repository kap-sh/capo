"""Generated from Smithy shape ``com.amazonaws.codedeploy#TagFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.key
    import capo_codedeploy.types.tag_filter_type
    import capo_codedeploy.types.value


class TagFilter(TypedDict, closed=True):
    key: NotRequired["capo_codedeploy.types.key.Key"]
    """<p>The on-premises instance tag filter key.</p>"""
    value: NotRequired["capo_codedeploy.types.value.Value"]
    """<p>The on-premises instance tag filter value.</p>"""
    type: NotRequired["capo_codedeploy.types.tag_filter_type.TagFilterType"]
    """<p>The on-premises instance tag filter type:</p> <ul> <li> <p>KEY_ONLY: Key only.</p> </li> <li> <p>VALUE_ONLY: Value only.</p> </li> <li> <p>KEY_AND_VALUE: Key and value.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    if "type" in value:
        import capo_codedeploy.types.tag_filter_type

        out["Type"] = capo_codedeploy.types.tag_filter_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagFilter:
    out: TagFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Type") is not None:
        import capo_codedeploy.types.tag_filter_type

        out["type"] = capo_codedeploy.types.tag_filter_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    if "type" in value:
        import capo_codedeploy.types.tag_filter_type

        out["Type"] = capo_codedeploy.types.tag_filter_type.serialize_cbor(
            value["type"]
        )
    return out


def deserialize_cbor(data: dict) -> TagFilter:
    out: TagFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Type") is not None:
        import capo_codedeploy.types.tag_filter_type

        out["type"] = capo_codedeploy.types.tag_filter_type.deserialize_cbor(
            data["Type"]
        )
    return out
