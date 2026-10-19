"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.tag_key
    import capo_partnercentral_selling.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_partnercentral_selling.types.tag_key.TagKey"
    """<p>The key in the tag.</p>"""
    value: "capo_partnercentral_selling.types.tag_value.TagValue"
    """<p>The value in the tag.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Tag:
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
