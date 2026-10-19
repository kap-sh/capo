"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.tag_key
    import capo_partnercentral_benefits.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_partnercentral_benefits.types.tag_key.TagKey"
    """<p>The tag key, which acts as a category or label for the tag.</p>"""
    value: "capo_partnercentral_benefits.types.tag_value.TagValue"
    """<p>The tag value, which provides additional information or context for the tag key.</p>"""


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
