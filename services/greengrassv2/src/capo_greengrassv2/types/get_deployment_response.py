"""Generated from Smithy shape ``com.amazonaws.greengrassv2#GetDeploymentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_deployment_specifications
    import capo_greengrassv2.types.deployment_io_t_job_configuration
    import capo_greengrassv2.types.deployment_policies
    import capo_greengrassv2.types.deployment_status
    import capo_greengrassv2.types.io_t_job_arn
    import capo_greengrassv2.types.is_latest_for_target
    import capo_greengrassv2.types.non_empty_string
    import capo_greengrassv2.types.nullable_string
    import capo_greengrassv2.types.tag_map
    import capo_greengrassv2.types.target_arn
    import capo_greengrassv2.types.thing_group_arn
    import capo_greengrassv2.types.timestamp


class GetDeploymentResponse(TypedDict, closed=True):
    target_arn: NotRequired["capo_greengrassv2.types.target_arn.TargetARN"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the target IoT thing or thing group.</p>"""
    revision_id: NotRequired["capo_greengrassv2.types.non_empty_string.NonEmptyString"]
    """<p>The revision number of the deployment.</p>"""
    deployment_id: NotRequired[
        "capo_greengrassv2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the deployment.</p>"""
    deployment_name: NotRequired[
        "capo_greengrassv2.types.nullable_string.NullableString"
    ]
    """<p>The name of the deployment.</p>"""
    deployment_status: NotRequired[
        "capo_greengrassv2.types.deployment_status.DeploymentStatus"
    ]
    """<p>The status of the deployment.</p>"""
    iot_job_id: NotRequired["capo_greengrassv2.types.nullable_string.NullableString"]
    """<p>The ID of the IoT job that applies the deployment to target devices.</p>"""
    iot_job_arn: NotRequired["capo_greengrassv2.types.io_t_job_arn.IoTJobARN"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the IoT job that applies the deployment to target devices.</p>"""
    components: NotRequired[
        "capo_greengrassv2.types.component_deployment_specifications.ComponentDeploymentSpecifications"
    ]
    """<p>The components to deploy. This is a dictionary, where each key is the name of a component, and each key's value is the version and configuration to deploy for that component.</p>"""
    deployment_policies: NotRequired[
        "capo_greengrassv2.types.deployment_policies.DeploymentPolicies"
    ]
    """<p>The deployment policies for the deployment. These policies define how the deployment updates components and handles failure.</p>"""
    iot_job_configuration: NotRequired[
        "capo_greengrassv2.types.deployment_io_t_job_configuration.DeploymentIoTJobConfiguration"
    ]
    """<p>The job configuration for the deployment configuration. The job configuration specifies the rollout, timeout, and stop configurations for the deployment configuration.</p>"""
    creation_timestamp: NotRequired["capo_greengrassv2.types.timestamp.Timestamp"]
    """<p>The time at which the deployment was created, expressed in ISO 8601 format.</p>"""
    is_latest_for_target: (
        "capo_greengrassv2.types.is_latest_for_target.IsLatestForTarget"
    )
    """<p>Whether or not the deployment is the latest revision for its target.</p>"""
    parent_target_arn: NotRequired[
        "capo_greengrassv2.types.thing_group_arn.ThingGroupARN"
    ]
    """<p>The parent deployment's target <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> within a subdeployment.</p>"""
    tags: NotRequired["capo_greengrassv2.types.tag_map.TagMap"]
    """<p>A list of key-value pairs that contain metadata for the resource. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html">Tag your resources</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentResponse) -> dict:
    out: dict = {}
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "deployment_name" in value:
        out["deploymentName"] = value["deployment_name"]
    if "deployment_status" in value:
        import capo_greengrassv2.types.deployment_status

        out["deploymentStatus"] = (
            capo_greengrassv2.types.deployment_status.serialize_json(
                value["deployment_status"]
            )
        )
    if "iot_job_id" in value:
        out["iotJobId"] = value["iot_job_id"]
    if "iot_job_arn" in value:
        out["iotJobArn"] = value["iot_job_arn"]
    if "components" in value:
        import capo_greengrassv2.types.component_deployment_specifications

        out["components"] = (
            capo_greengrassv2.types.component_deployment_specifications.serialize_json(
                value["components"]
            )
        )
    if "deployment_policies" in value:
        import capo_greengrassv2.types.deployment_policies

        out["deploymentPolicies"] = (
            capo_greengrassv2.types.deployment_policies.serialize_json(
                value["deployment_policies"]
            )
        )
    if "iot_job_configuration" in value:
        import capo_greengrassv2.types.deployment_io_t_job_configuration

        out["iotJobConfiguration"] = (
            capo_greengrassv2.types.deployment_io_t_job_configuration.serialize_json(
                value["iot_job_configuration"]
            )
        )
    if "creation_timestamp" in value:
        import capo_greengrassv2.types.timestamp

        out["creationTimestamp"] = capo_greengrassv2.types.timestamp.serialize_json(
            value["creation_timestamp"]
        )
    out["isLatestForTarget"] = value.get("is_latest_for_target", False)
    if "parent_target_arn" in value:
        out["parentTargetArn"] = value["parent_target_arn"]
    if "tags" in value:
        import capo_greengrassv2.types.tag_map

        out["tags"] = capo_greengrassv2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetDeploymentResponse:
    out: GetDeploymentResponse = {}  # type: ignore[typeddict-item]
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    if data.get("deploymentName") is not None:
        out["deployment_name"] = data["deploymentName"]
    if data.get("deploymentStatus") is not None:
        import capo_greengrassv2.types.deployment_status

        out["deployment_status"] = (
            capo_greengrassv2.types.deployment_status.deserialize_json(
                data["deploymentStatus"]
            )
        )
    if data.get("iotJobId") is not None:
        out["iot_job_id"] = data["iotJobId"]
    if data.get("iotJobArn") is not None:
        out["iot_job_arn"] = data["iotJobArn"]
    if data.get("components") is not None:
        import capo_greengrassv2.types.component_deployment_specifications

        out["components"] = (
            capo_greengrassv2.types.component_deployment_specifications.deserialize_json(
                data["components"]
            )
        )
    if data.get("deploymentPolicies") is not None:
        import capo_greengrassv2.types.deployment_policies

        out["deployment_policies"] = (
            capo_greengrassv2.types.deployment_policies.deserialize_json(
                data["deploymentPolicies"]
            )
        )
    if data.get("iotJobConfiguration") is not None:
        import capo_greengrassv2.types.deployment_io_t_job_configuration

        out["iot_job_configuration"] = (
            capo_greengrassv2.types.deployment_io_t_job_configuration.deserialize_json(
                data["iotJobConfiguration"]
            )
        )
    if data.get("creationTimestamp") is not None:
        import capo_greengrassv2.types.timestamp

        out["creation_timestamp"] = capo_greengrassv2.types.timestamp.deserialize_json(
            data["creationTimestamp"]
        )
    if data.get("isLatestForTarget") is not None:
        out["is_latest_for_target"] = data["isLatestForTarget"]
    else:
        out["is_latest_for_target"] = False
    if data.get("parentTargetArn") is not None:
        out["parent_target_arn"] = data["parentTargetArn"]
    if data.get("tags") is not None:
        import capo_greengrassv2.types.tag_map

        out["tags"] = capo_greengrassv2.types.tag_map.deserialize_json(data["tags"])
    return out
