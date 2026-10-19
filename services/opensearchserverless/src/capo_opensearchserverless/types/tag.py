"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.tag_key
    import capo_opensearchserverless.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_opensearchserverless.types.tag_key.TagKey"
    """<p>The key to use in the tag.</p>"""
    value: "capo_opensearchserverless.types.tag_value.TagValue"
    """<p>The value of the tag.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
