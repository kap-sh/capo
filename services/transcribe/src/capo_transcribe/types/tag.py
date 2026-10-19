"""Generated from Smithy shape ``com.amazonaws.transcribe#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.tag_key
    import capo_transcribe.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_transcribe.types.tag_key.TagKey"
    """<p>The first part of a key:value pair that forms a tag associated with a given resource. For example, in the tag <code>Department:Sales</code>, the key is 'Department'.</p>"""
    value: "capo_transcribe.types.tag_value.TagValue"
    """<p>The second part of a key:value pair that forms a tag associated with a given resource. For example, in the tag <code>Department:Sales</code>, the value is 'Sales'.</p> <p>Note that you can set the value of a tag to an empty string, but you can't set the value of a tag to null. Omitting the tag value is the same as using an empty string.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
