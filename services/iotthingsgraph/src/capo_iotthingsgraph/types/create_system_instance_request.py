"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#CreateSystemInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.definition_document
    import capo_iotthingsgraph.types.deployment_target
    import capo_iotthingsgraph.types.group_name
    import capo_iotthingsgraph.types.metrics_configuration
    import capo_iotthingsgraph.types.role_arn
    import capo_iotthingsgraph.types.s3_bucket_name
    import capo_iotthingsgraph.types.tag_list


class CreateSystemInstanceRequest(TypedDict, closed=True):
    tags: NotRequired["capo_iotthingsgraph.types.tag_list.TagList"]
    """<p>Metadata, consisting of key-value pairs, that can be used to categorize your system instances.</p>"""
    definition: "capo_iotthingsgraph.types.definition_document.DefinitionDocument"
    target: "capo_iotthingsgraph.types.deployment_target.DeploymentTarget"
    """<p>The target type of the deployment. Valid values are <code>GREENGRASS</code> and <code>CLOUD</code>.</p>"""
    greengrass_group_name: NotRequired["capo_iotthingsgraph.types.group_name.GroupName"]
    """<p>The name of the Greengrass group where the system instance will be deployed. This value is required if the value of the <code>target</code> parameter is <code>GREENGRASS</code>.</p>"""
    s3_bucket_name: NotRequired["capo_iotthingsgraph.types.s3_bucket_name.S3BucketName"]
    """<p>The name of the Amazon Simple Storage Service bucket that will be used to store and deploy the system instance's resource file. This value is required if the value of the <code>target</code> parameter is <code>GREENGRASS</code>.</p>"""
    metrics_configuration: NotRequired[
        "capo_iotthingsgraph.types.metrics_configuration.MetricsConfiguration"
    ]
    flow_actions_role_arn: NotRequired["capo_iotthingsgraph.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role that AWS IoT Things Graph will assume when it executes the flow. This role must have read and write access to AWS Lambda and AWS IoT and any other AWS services that the flow uses when it executes. This value is required if the value of the <code>target</code> parameter is <code>CLOUD</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSystemInstanceRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_iotthingsgraph.types.tag_list

        out["tags"] = capo_iotthingsgraph.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    import capo_iotthingsgraph.types.definition_document

    out["definition"] = (
        capo_iotthingsgraph.types.definition_document.serialize_aws_json_1_1(
            value["definition"]
        )
    )
    import capo_iotthingsgraph.types.deployment_target

    out["target"] = capo_iotthingsgraph.types.deployment_target.serialize_aws_json_1_1(
        value["target"]
    )
    if "greengrass_group_name" in value:
        out["greengrassGroupName"] = value["greengrass_group_name"]
    if "s3_bucket_name" in value:
        out["s3BucketName"] = value["s3_bucket_name"]
    if "metrics_configuration" in value:
        import capo_iotthingsgraph.types.metrics_configuration

        out["metricsConfiguration"] = (
            capo_iotthingsgraph.types.metrics_configuration.serialize_aws_json_1_1(
                value["metrics_configuration"]
            )
        )
    if "flow_actions_role_arn" in value:
        out["flowActionsRoleArn"] = value["flow_actions_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSystemInstanceRequest:
    out: CreateSystemInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_iotthingsgraph.types.tag_list

        out["tags"] = capo_iotthingsgraph.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("definition") is not None:
        import capo_iotthingsgraph.types.definition_document

        out["definition"] = (
            capo_iotthingsgraph.types.definition_document.deserialize_aws_json_1_1(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("CreateSystemInstanceRequest.definition required")
    if data.get("target") is not None:
        import capo_iotthingsgraph.types.deployment_target

        out["target"] = (
            capo_iotthingsgraph.types.deployment_target.deserialize_aws_json_1_1(
                data["target"]
            )
        )
    else:
        import typing

        out["target"] = typing.cast(
            "capo_iotthingsgraph.types.deployment_target.DeploymentTarget", ""
        )
    if data.get("greengrassGroupName") is not None:
        out["greengrass_group_name"] = data["greengrassGroupName"]
    if data.get("s3BucketName") is not None:
        out["s3_bucket_name"] = data["s3BucketName"]
    if data.get("metricsConfiguration") is not None:
        import capo_iotthingsgraph.types.metrics_configuration

        out["metrics_configuration"] = (
            capo_iotthingsgraph.types.metrics_configuration.deserialize_aws_json_1_1(
                data["metricsConfiguration"]
            )
        )
    if data.get("flowActionsRoleArn") is not None:
        out["flow_actions_role_arn"] = data["flowActionsRoleArn"]
    return out
