"""Generated from Smithy shape ``com.amazonaws.organizations#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.tag_key
    import capo_organizations.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_organizations.types.tag_key.TagKey"
    """<p>The key identifier, or name, of the tag.</p>"""
    value: "capo_organizations.types.tag_value.TagValue"
    """<p>The string value that's associated with the key of the tag. You can set the value of a tag to an empty string, but you can't set the value of a tag to null.</p>"""


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
