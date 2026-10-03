"""Generated from Smithy shape ``com.amazonaws.eks#FargateProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.fargate_profile_health
    import capo_eks.types.fargate_profile_selectors
    import capo_eks.types.fargate_profile_status
    import capo_eks.types.string
    import capo_eks.types.string_list
    import capo_eks.types.tag_map
    import capo_eks.types.timestamp


class FargateProfile(TypedDict, closed=True):
    fargate_profile_name: NotRequired["capo_eks.types.string.String"]
    """<p>The name of the Fargate profile.</p>"""
    fargate_profile_arn: NotRequired["capo_eks.types.string.String"]
    """<p>The full Amazon Resource Name (ARN) of the Fargate profile.</p>"""
    cluster_name: NotRequired["capo_eks.types.string.String"]
    """<p>The name of your cluster.</p>"""
    created_at: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp at object creation.</p>"""
    pod_execution_role_arn: NotRequired["capo_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the <code>Pod</code> execution role to use for any <code>Pod</code> that matches the selectors in the Fargate profile. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html"> <code>Pod</code> execution role</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    subnets: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>The IDs of subnets to launch a <code>Pod</code> into.</p>"""
    selectors: NotRequired[
        "capo_eks.types.fargate_profile_selectors.FargateProfileSelectors"
    ]
    """<p>The selectors to match for a <code>Pod</code> to use this Fargate profile.</p>"""
    status: NotRequired["capo_eks.types.fargate_profile_status.FargateProfileStatus"]
    """<p>The current status of the Fargate profile.</p>"""
    tags: NotRequired["capo_eks.types.tag_map.TagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""
    health: NotRequired["capo_eks.types.fargate_profile_health.FargateProfileHealth"]
    """<p>The health status of the Fargate profile. If there are issues with your Fargate profile's health, they are listed here.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FargateProfile) -> dict:
    out: dict = {}
    if "fargate_profile_name" in value:
        out["fargateProfileName"] = value["fargate_profile_name"]
    if "fargate_profile_arn" in value:
        out["fargateProfileArn"] = value["fargate_profile_arn"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "created_at" in value:
        import capo_eks.types.timestamp

        out["createdAt"] = capo_eks.types.timestamp.serialize_json(value["created_at"])
    if "pod_execution_role_arn" in value:
        out["podExecutionRoleArn"] = value["pod_execution_role_arn"]
    if "subnets" in value:
        import capo_eks.types.string_list

        out["subnets"] = capo_eks.types.string_list.serialize_json(value["subnets"])
    if "selectors" in value:
        import capo_eks.types.fargate_profile_selectors

        out["selectors"] = capo_eks.types.fargate_profile_selectors.serialize_json(
            value["selectors"]
        )
    if "status" in value:
        import capo_eks.types.fargate_profile_status

        out["status"] = capo_eks.types.fargate_profile_status.serialize_json(
            value["status"]
        )
    if "tags" in value:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.serialize_json(value["tags"])
    if "health" in value:
        import capo_eks.types.fargate_profile_health

        out["health"] = capo_eks.types.fargate_profile_health.serialize_json(
            value["health"]
        )
    return out


def deserialize_json(data: dict) -> FargateProfile:
    out: FargateProfile = {}  # type: ignore[typeddict-item]
    if data.get("fargateProfileName") is not None:
        out["fargate_profile_name"] = data["fargateProfileName"]
    if data.get("fargateProfileArn") is not None:
        out["fargate_profile_arn"] = data["fargateProfileArn"]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    if data.get("createdAt") is not None:
        import capo_eks.types.timestamp

        out["created_at"] = capo_eks.types.timestamp.deserialize_json(data["createdAt"])
    if data.get("podExecutionRoleArn") is not None:
        out["pod_execution_role_arn"] = data["podExecutionRoleArn"]
    if data.get("subnets") is not None:
        import capo_eks.types.string_list

        out["subnets"] = capo_eks.types.string_list.deserialize_json(data["subnets"])
    if data.get("selectors") is not None:
        import capo_eks.types.fargate_profile_selectors

        out["selectors"] = capo_eks.types.fargate_profile_selectors.deserialize_json(
            data["selectors"]
        )
    if data.get("status") is not None:
        import capo_eks.types.fargate_profile_status

        out["status"] = capo_eks.types.fargate_profile_status.deserialize_json(
            data["status"]
        )
    if data.get("tags") is not None:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.deserialize_json(data["tags"])
    if data.get("health") is not None:
        import capo_eks.types.fargate_profile_health

        out["health"] = capo_eks.types.fargate_profile_health.deserialize_json(
            data["health"]
        )
    return out
