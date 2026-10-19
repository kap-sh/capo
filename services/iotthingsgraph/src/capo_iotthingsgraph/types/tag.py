"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.tag_key
    import capo_iotthingsgraph.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_iotthingsgraph.types.tag_key.TagKey"
    """<p>The required name of the tag. The string value can be from 1 to 128 Unicode characters in length.</p>"""
    value: "capo_iotthingsgraph.types.tag_value.TagValue"
    """<p>The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
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
    else:
        out["value"] = ""
    return out
