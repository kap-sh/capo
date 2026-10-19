"""Generated from Smithy shape ``com.amazonaws.costexplorer#ResourceTag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.resource_tag_key
    import capo_cost_explorer.types.resource_tag_value


class ResourceTag(TypedDict, closed=True):
    key: "capo_cost_explorer.types.resource_tag_key.ResourceTagKey"
    """<p>The key that's associated with the tag. </p>"""
    value: "capo_cost_explorer.types.resource_tag_value.ResourceTagValue"
    """<p>The value that's associated with the tag. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceTag:
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
