"""Generated from Smithy shape ``com.amazonaws.fms#ResourceTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.resource_tag_key
    import capo_fms.types.resource_tag_value


class ResourceTag(TypedDict, closed=True):
    key: "capo_fms.types.resource_tag_key.ResourceTagKey"
    """<p>The resource tag key.</p>"""
    value: NotRequired["capo_fms.types.resource_tag_value.ResourceTagValue"]
    """<p>The resource tag value. To specify an empty string value, either don't provide this or specify it as "". </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceTag:
    out: ResourceTag = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("ResourceTag.key required")
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
