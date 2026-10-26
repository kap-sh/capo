"""Generated from Smithy shape ``com.amazonaws.ssm#CreateCloudConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.cloud_connector_configuration
    import capo_ssm.types.cloud_connector_description
    import capo_ssm.types.cloud_connector_iam_role_arn
    import capo_ssm.types.config_connector_arn
    import capo_ssm.types.display_name
    import capo_ssm.types.tag_list


class CreateCloudConnectorRequest(TypedDict, closed=True):
    display_name: "capo_ssm.types.display_name.DisplayName"
    """<p>A friendly name for the cloud connector.</p>"""
    role_arn: "capo_ssm.types.cloud_connector_iam_role_arn.CloudConnectorIamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that the cloud connector uses to communicate with the third-party cloud environment.</p>"""
    description: NotRequired[
        "capo_ssm.types.cloud_connector_description.CloudConnectorDescription"
    ]
    """<p>A description for the cloud connector.</p>"""
    configuration: (
        "capo_ssm.types.cloud_connector_configuration.CloudConnectorConfiguration"
    )
    """<p>The configuration details for connecting to the third-party cloud environment.</p>"""
    config_connector_arn: "capo_ssm.types.config_connector_arn.ConfigConnectorArn"
    """<p>The ARN of the Amazon Web Services Config connector associated with this cloud connector.</p>"""
    tags: NotRequired["capo_ssm.types.tag_list.TagList"]
    """<p>Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCloudConnectorRequest) -> dict:
    out: dict = {}
    out["DisplayName"] = value["display_name"]
    out["RoleArn"] = value["role_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_ssm.types.cloud_connector_configuration

    out["Configuration"] = (
        capo_ssm.types.cloud_connector_configuration.serialize_aws_json_1_1(
            value["configuration"]
        )
    )
    out["ConfigConnectorArn"] = value["config_connector_arn"]
    if "tags" in value:
        import capo_ssm.types.tag_list

        out["Tags"] = capo_ssm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCloudConnectorRequest:
    out: CreateCloudConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    else:
        out["display_name"] = ""
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Configuration") is not None:
        import capo_ssm.types.cloud_connector_configuration

        out["configuration"] = (
            capo_ssm.types.cloud_connector_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    else:
        out["configuration"] = {"$unknown": {"name": ""}}
    if data.get("ConfigConnectorArn") is not None:
        out["config_connector_arn"] = data["ConfigConnectorArn"]
    else:
        out["config_connector_arn"] = ""
    if data.get("Tags") is not None:
        import capo_ssm.types.tag_list

        out["tags"] = capo_ssm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
