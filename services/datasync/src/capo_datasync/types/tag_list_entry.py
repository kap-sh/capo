"""Generated from Smithy shape ``com.amazonaws.datasync#TagListEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.tag_key
    import capo_datasync.types.tag_value


class TagListEntry(TypedDict, closed=True):
    key: "capo_datasync.types.tag_key.TagKey"
    """<p>The key for an Amazon Web Services resource tag.</p>"""
    value: NotRequired["capo_datasync.types.tag_value.TagValue"]
    """<p>The value for an Amazon Web Services resource tag.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagListEntry) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TagListEntry:
    out: TagListEntry = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
