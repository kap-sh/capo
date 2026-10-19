"""Generated from Smithy shape ``com.amazonaws.invoicing#ResourceTag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.resource_tag_key
    import capo_invoicing.types.resource_tag_value


class ResourceTag(TypedDict, closed=True):
    key: "capo_invoicing.types.resource_tag_key.ResourceTagKey"
    """<p>The object key of your of your resource tag. </p>"""
    value: "capo_invoicing.types.resource_tag_value.ResourceTagValue"
    """<p> The specific value of the resource tag. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceTag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceTag:
    out: ResourceTag = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
