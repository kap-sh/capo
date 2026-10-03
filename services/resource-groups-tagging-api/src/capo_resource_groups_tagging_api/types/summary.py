"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#Summary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.amazon_resource_type
    import capo_resource_groups_tagging_api.types.last_updated
    import capo_resource_groups_tagging_api.types.non_compliant_resources
    import capo_resource_groups_tagging_api.types.region
    import capo_resource_groups_tagging_api.types.target_id
    import capo_resource_groups_tagging_api.types.target_id_type


class Summary(TypedDict, closed=True):
    last_updated: NotRequired[
        "capo_resource_groups_tagging_api.types.last_updated.LastUpdated"
    ]
    """<p>The timestamp that shows when this summary was generated in this Region. </p>"""
    target_id: NotRequired["capo_resource_groups_tagging_api.types.target_id.TargetId"]
    """<p>The account identifier or the root identifier of the organization. If you don't know the root ID, you can call the Organizations <a href="https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListRoots.html">ListRoots</a> API.</p>"""
    target_id_type: NotRequired[
        "capo_resource_groups_tagging_api.types.target_id_type.TargetIdType"
    ]
    """<p>Whether the target is an account, an OU, or the organization root.</p>"""
    region: NotRequired["capo_resource_groups_tagging_api.types.region.Region"]
    """<p>The Amazon Web Services Region that the summary applies to.</p>"""
    resource_type: NotRequired[
        "capo_resource_groups_tagging_api.types.amazon_resource_type.AmazonResourceType"
    ]
    """<p>The Amazon Web Services resource type.</p>"""
    non_compliant_resources: "capo_resource_groups_tagging_api.types.non_compliant_resources.NonCompliantResources"
    """<p>The count of noncompliant resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Summary) -> dict:
    out: dict = {}
    if "last_updated" in value:
        out["LastUpdated"] = value["last_updated"]
    if "target_id" in value:
        out["TargetId"] = value["target_id"]
    if "target_id_type" in value:
        import capo_resource_groups_tagging_api.types.target_id_type

        out["TargetIdType"] = (
            capo_resource_groups_tagging_api.types.target_id_type.serialize_aws_json_1_1(
                value["target_id_type"]
            )
        )
    if "region" in value:
        out["Region"] = value["region"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    out["NonCompliantResources"] = value.get("non_compliant_resources", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> Summary:
    out: Summary = {}  # type: ignore[typeddict-item]
    if data.get("LastUpdated") is not None:
        out["last_updated"] = data["LastUpdated"]
    if data.get("TargetId") is not None:
        out["target_id"] = data["TargetId"]
    if data.get("TargetIdType") is not None:
        import capo_resource_groups_tagging_api.types.target_id_type

        out["target_id_type"] = (
            capo_resource_groups_tagging_api.types.target_id_type.deserialize_aws_json_1_1(
                data["TargetIdType"]
            )
        )
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("NonCompliantResources") is not None:
        out["non_compliant_resources"] = data["NonCompliantResources"]
    else:
        out["non_compliant_resources"] = 0
    return out
