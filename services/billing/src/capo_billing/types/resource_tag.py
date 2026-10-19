"""Generated from Smithy shape ``com.amazonaws.billing#ResourceTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.resource_tag_key
    import capo_billing.types.resource_tag_value


class ResourceTag(TypedDict, closed=True):
    key: "capo_billing.types.resource_tag_key.ResourceTagKey"
    """<p> The key that's associated with the tag. </p>"""
    value: NotRequired["capo_billing.types.resource_tag_value.ResourceTagValue"]
    """<p> The value that's associated with the tag. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceTag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceTag:
    out: ResourceTag = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
