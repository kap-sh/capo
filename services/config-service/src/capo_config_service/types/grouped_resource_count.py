"""Generated from Smithy shape ``com.amazonaws.configservice#GroupedResourceCount``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.long
    import capo_config_service.types.string_with_char_limit256


class GroupedResourceCount(TypedDict, closed=True):
    group_name: (
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    )
    """<p>The name of the group that can be region, account ID, or resource type. For example, region1, region2 if the region was chosen as <code>GroupByKey</code>.</p>"""
    resource_count: "capo_config_service.types.long.Long"
    """<p>The number of resources in the group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupedResourceCount) -> dict:
    out: dict = {}
    out["GroupName"] = value["group_name"]
    out["ResourceCount"] = value.get("resource_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> GroupedResourceCount:
    out: GroupedResourceCount = {}  # type: ignore[typeddict-item]
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
    else:
        out["group_name"] = ""
    if data.get("ResourceCount") is not None:
        out["resource_count"] = data["ResourceCount"]
    else:
        out["resource_count"] = 0
    return out
