"""Generated from Smithy shape ``com.amazonaws.translate#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_translate.types.tag_key
    import capo_translate.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_translate.types.tag_key.TagKey"
    """<p>The initial part of a key-value pair that forms a tag associated with a given resource. </p>"""
    value: "capo_translate.types.tag_value.TagValue"
    """<p> The second part of a key-value pair that forms a tag associated with a given resource.</p>"""


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
