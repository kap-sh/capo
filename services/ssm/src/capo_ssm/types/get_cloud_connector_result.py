"""Generated from Smithy shape ``com.amazonaws.ssm#GetCloudConnectorResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.cloud_connector_arn
    import capo_ssm.types.cloud_connector_configuration
    import capo_ssm.types.cloud_connector_description
    import capo_ssm.types.cloud_connector_iam_role_arn
    import capo_ssm.types.config_connector_arn
    import capo_ssm.types.date_time
    import capo_ssm.types.display_name


class GetCloudConnectorResult(TypedDict, closed=True):
    cloud_connector_arn: NotRequired[
        "capo_ssm.types.cloud_connector_arn.CloudConnectorArn"
    ]
    """<p>The ARN of the cloud connector.</p>"""
    display_name: NotRequired["capo_ssm.types.display_name.DisplayName"]
    """<p>The friendly name of the cloud connector.</p>"""
    description: NotRequired[
        "capo_ssm.types.cloud_connector_description.CloudConnectorDescription"
    ]
    """<p>The description of the cloud connector.</p>"""
    role_arn: NotRequired[
        "capo_ssm.types.cloud_connector_iam_role_arn.CloudConnectorIamRoleArn"
    ]
    """<p>The ARN of the IAM role used by the cloud connector.</p>"""
    configuration: NotRequired[
        "capo_ssm.types.cloud_connector_configuration.CloudConnectorConfiguration"
    ]
    """<p>The configuration details for the third-party cloud environment connection.</p>"""
    config_connector_arn: NotRequired[
        "capo_ssm.types.config_connector_arn.ConfigConnectorArn"
    ]
    """<p>The ARN of the Amazon Web Services Config connector associated with this cloud connector. This value is returned only if the cloud connector was created with an Amazon Web Services Config connector.</p>"""
    created_at: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time the cloud connector was created.</p>"""
    updated_at: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time the cloud connector was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCloudConnectorResult) -> dict:
    out: dict = {}
    if "cloud_connector_arn" in value:
        out["CloudConnectorArn"] = value["cloud_connector_arn"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "configuration" in value:
        import capo_ssm.types.cloud_connector_configuration

        out["Configuration"] = (
            capo_ssm.types.cloud_connector_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "config_connector_arn" in value:
        out["ConfigConnectorArn"] = value["config_connector_arn"]
    if "created_at" in value:
        import capo_ssm.types.date_time

        out["CreatedAt"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_ssm.types.date_time

        out["UpdatedAt"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCloudConnectorResult:
    out: GetCloudConnectorResult = {}  # type: ignore[typeddict-item]
    if data.get("CloudConnectorArn") is not None:
        out["cloud_connector_arn"] = data["CloudConnectorArn"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("Configuration") is not None:
        import capo_ssm.types.cloud_connector_configuration

        out["configuration"] = (
            capo_ssm.types.cloud_connector_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    if data.get("ConfigConnectorArn") is not None:
        out["config_connector_arn"] = data["ConfigConnectorArn"]
    if data.get("CreatedAt") is not None:
        import capo_ssm.types.date_time

        out["created_at"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_ssm.types.date_time

        out["updated_at"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    return out
