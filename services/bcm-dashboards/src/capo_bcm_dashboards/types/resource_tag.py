"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ResourceTag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.resource_tag_key
    import capo_bcm_dashboards.types.resource_tag_value


class ResourceTag(TypedDict, closed=True):
    key: "capo_bcm_dashboards.types.resource_tag_key.ResourceTagKey"
    """<p>The key of the tag to be attached to the dashboard resource.</p>"""
    value: "capo_bcm_dashboards.types.resource_tag_value.ResourceTagValue"
    """<p>The value of the tag to be attached to the dashboard resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceTag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
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
    else:
        out["value"] = ""
    return out
