"""Generated from Smithy shape ``com.amazonaws.b2bi#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.tag_key
    import capo_b2bi.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_b2bi.types.tag_key.TagKey"
    """<p>Specifies the name assigned to the tag that you create.</p>"""
    value: "capo_b2bi.types.tag_value.TagValue"
    """<p>Contains one or more values that you assigned to the key name that you create.</p>"""


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
