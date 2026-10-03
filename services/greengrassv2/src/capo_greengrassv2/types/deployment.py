"""Generated from Smithy shape ``com.amazonaws.greengrassv2#Deployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.deployment_status
    import capo_greengrassv2.types.is_latest_for_target
    import capo_greengrassv2.types.non_empty_string
    import capo_greengrassv2.types.target_arn
    import capo_greengrassv2.types.thing_group_arn
    import capo_greengrassv2.types.timestamp


class Deployment(TypedDict, closed=True):
    target_arn: NotRequired["capo_greengrassv2.types.target_arn.TargetARN"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the target IoT thing or thing group. When creating a subdeployment, the targetARN can only be a thing group.</p>"""
    revision_id: NotRequired["capo_greengrassv2.types.non_empty_string.NonEmptyString"]
    """<p>The revision number of the deployment.</p>"""
    deployment_id: NotRequired[
        "capo_greengrassv2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the deployment.</p>"""
    deployment_name: NotRequired[
        "capo_greengrassv2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the deployment.</p>"""
    creation_timestamp: NotRequired["capo_greengrassv2.types.timestamp.Timestamp"]
    """<p>The time at which the deployment was created, expressed in ISO 8601 format.</p>"""
    deployment_status: NotRequired[
        "capo_greengrassv2.types.deployment_status.DeploymentStatus"
    ]
    """<p>The status of the deployment.</p>"""
    is_latest_for_target: (
        "capo_greengrassv2.types.is_latest_for_target.IsLatestForTarget"
    )
    """<p>Whether or not the deployment is the latest revision for its target.</p>"""
    parent_target_arn: NotRequired[
        "capo_greengrassv2.types.thing_group_arn.ThingGroupARN"
    ]
    """<p>The parent deployment's target <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> within a subdeployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Deployment) -> dict:
    out: dict = {}
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "deployment_name" in value:
        out["deploymentName"] = value["deployment_name"]
    if "creation_timestamp" in value:
        import capo_greengrassv2.types.timestamp

        out["creationTimestamp"] = capo_greengrassv2.types.timestamp.serialize_json(
            value["creation_timestamp"]
        )
    if "deployment_status" in value:
        import capo_greengrassv2.types.deployment_status

        out["deploymentStatus"] = (
            capo_greengrassv2.types.deployment_status.serialize_json(
                value["deployment_status"]
            )
        )
    out["isLatestForTarget"] = value.get("is_latest_for_target", False)
    if "parent_target_arn" in value:
        out["parentTargetArn"] = value["parent_target_arn"]
    return out


def deserialize_json(data: dict) -> Deployment:
    out: Deployment = {}  # type: ignore[typeddict-item]
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    if data.get("deploymentName") is not None:
        out["deployment_name"] = data["deploymentName"]
    if data.get("creationTimestamp") is not None:
        import capo_greengrassv2.types.timestamp

        out["creation_timestamp"] = capo_greengrassv2.types.timestamp.deserialize_json(
            data["creationTimestamp"]
        )
    if data.get("deploymentStatus") is not None:
        import capo_greengrassv2.types.deployment_status

        out["deployment_status"] = (
            capo_greengrassv2.types.deployment_status.deserialize_json(
                data["deploymentStatus"]
            )
        )
    if data.get("isLatestForTarget") is not None:
        out["is_latest_for_target"] = data["isLatestForTarget"]
    else:
        out["is_latest_for_target"] = False
    if data.get("parentTargetArn") is not None:
        out["parent_target_arn"] = data["parentTargetArn"]
    return out
