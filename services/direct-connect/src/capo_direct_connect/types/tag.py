"""Generated from Smithy shape ``com.amazonaws.directconnect#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.tag_key
    import capo_direct_connect.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_direct_connect.types.tag_key.TagKey"
    """<p>The key.</p>"""
    value: NotRequired["capo_direct_connect.types.tag_value.TagValue"]
    """<p>The value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
