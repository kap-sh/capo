"""Generated from Smithy shape ``com.amazonaws.greengrassv2#CreateDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_greengrassv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_greengrassv2.types.client_token_string
    import capo_greengrassv2.types.component_deployment_specifications
    import capo_greengrassv2.types.deployment_io_t_job_configuration
    import capo_greengrassv2.types.deployment_name_string
    import capo_greengrassv2.types.deployment_policies
    import capo_greengrassv2.types.tag_map
    import capo_greengrassv2.types.target_arn
    import capo_greengrassv2.types.thing_group_arn


class CreateDeploymentRequest(TypedDict, closed=True):
    target_arn: "capo_greengrassv2.types.target_arn.TargetARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the target IoT thing or thing group. When creating a subdeployment, the targetARN can only be a thing group.</p>"""
    deployment_name: NotRequired[
        "capo_greengrassv2.types.deployment_name_string.DeploymentNameString"
    ]
    """<p>The name of the deployment.</p>"""
    components: NotRequired[
        "capo_greengrassv2.types.component_deployment_specifications.ComponentDeploymentSpecifications"
    ]
    """<p>The components to deploy. This is a dictionary, where each key is the name of a component, and each key's value is the version and configuration to deploy for that component.</p>"""
    iot_job_configuration: NotRequired[
        "capo_greengrassv2.types.deployment_io_t_job_configuration.DeploymentIoTJobConfiguration"
    ]
    """<p>The job configuration for the deployment configuration. The job configuration specifies the rollout, timeout, and stop configurations for the deployment configuration.</p>"""
    deployment_policies: NotRequired[
        "capo_greengrassv2.types.deployment_policies.DeploymentPolicies"
    ]
    """<p>The deployment policies for the deployment. These policies define how the deployment updates components and handles failure.</p>"""
    parent_target_arn: NotRequired[
        "capo_greengrassv2.types.thing_group_arn.ThingGroupARN"
    ]
    """<p>The parent deployment's target <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> within a subdeployment.</p>"""
    tags: NotRequired["capo_greengrassv2.types.tag_map.TagMap"]
    """<p>A list of key-value pairs that contain metadata for the resource. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html">Tag your resources</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>"""
    client_token: NotRequired[
        "capo_greengrassv2.types.client_token_string.ClientTokenString"
    ]
    """<p>A unique, case-sensitive identifier that you can provide to ensure that the request is idempotent. Idempotency means that the request is successfully processed only once, even if you send the request multiple times. When a request succeeds, and you specify the same client token for subsequent successful requests, the IoT Greengrass V2 service returns the successful response that it caches from the previous request. IoT Greengrass V2 caches successful responses for idempotent requests for up to 8 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeploymentRequest) -> dict:
    out: dict = {}
    out["targetArn"] = value["target_arn"]
    if "deployment_name" in value:
        out["deploymentName"] = value["deployment_name"]
    if "components" in value:
        import capo_greengrassv2.types.component_deployment_specifications

        out["components"] = (
            capo_greengrassv2.types.component_deployment_specifications.serialize_json(
                value["components"]
            )
        )
    if "iot_job_configuration" in value:
        import capo_greengrassv2.types.deployment_io_t_job_configuration

        out["iotJobConfiguration"] = (
            capo_greengrassv2.types.deployment_io_t_job_configuration.serialize_json(
                value["iot_job_configuration"]
            )
        )
    if "deployment_policies" in value:
        import capo_greengrassv2.types.deployment_policies

        out["deploymentPolicies"] = (
            capo_greengrassv2.types.deployment_policies.serialize_json(
                value["deployment_policies"]
            )
        )
    if "parent_target_arn" in value:
        out["parentTargetArn"] = value["parent_target_arn"]
    if "tags" in value:
        import capo_greengrassv2.types.tag_map

        out["tags"] = capo_greengrassv2.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateDeploymentRequest:
    out: CreateDeploymentRequest = {}  # type: ignore[typeddict-item]
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    else:
        raise DeserializationError("CreateDeploymentRequest.target_arn required")
    if data.get("deploymentName") is not None:
        out["deployment_name"] = data["deploymentName"]
    if data.get("components") is not None:
        import capo_greengrassv2.types.component_deployment_specifications

        out["components"] = (
            capo_greengrassv2.types.component_deployment_specifications.deserialize_json(
                data["components"]
            )
        )
    if data.get("iotJobConfiguration") is not None:
        import capo_greengrassv2.types.deployment_io_t_job_configuration

        out["iot_job_configuration"] = (
            capo_greengrassv2.types.deployment_io_t_job_configuration.deserialize_json(
                data["iotJobConfiguration"]
            )
        )
    if data.get("deploymentPolicies") is not None:
        import capo_greengrassv2.types.deployment_policies

        out["deployment_policies"] = (
            capo_greengrassv2.types.deployment_policies.deserialize_json(
                data["deploymentPolicies"]
            )
        )
    if data.get("parentTargetArn") is not None:
        out["parent_target_arn"] = data["parentTargetArn"]
    if data.get("tags") is not None:
        import capo_greengrassv2.types.tag_map

        out["tags"] = capo_greengrassv2.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
