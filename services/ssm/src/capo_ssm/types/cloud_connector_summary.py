"""Generated from Smithy shape ``com.amazonaws.ssm#CloudConnectorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.cloud_connector_description
    import capo_ssm.types.cloud_connector_iam_role_arn
    import capo_ssm.types.cloud_connector_id
    import capo_ssm.types.config_connector_arn
    import capo_ssm.types.date_time
    import capo_ssm.types.display_name
    import capo_ssm.types.provider


class CloudConnectorSummary(TypedDict, closed=True):
    cloud_connector_id: NotRequired[
        "capo_ssm.types.cloud_connector_id.CloudConnectorId"
    ]
    """<p>The ID of the cloud connector.</p>"""
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
    created_at: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time the cloud connector was created.</p>"""
    updated_at: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time the cloud connector was last updated.</p>"""
    provider: NotRequired["capo_ssm.types.provider.Provider"]
    """<p>The third-party cloud provider that the cloud connector connects to. Valid values: <code>Azure</code> | <code>GCP</code>.</p>"""
    config_connector_arn: NotRequired[
        "capo_ssm.types.config_connector_arn.ConfigConnectorArn"
    ]
    """<p>The ARN of the Amazon Web Services Config connector associated with this cloud connector. This value is returned only if the cloud connector was created with an Amazon Web Services Config connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudConnectorSummary) -> dict:
    out: dict = {}
    if "cloud_connector_id" in value:
        out["CloudConnectorId"] = value["cloud_connector_id"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
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
    if "provider" in value:
        import capo_ssm.types.provider

        out["Provider"] = capo_ssm.types.provider.serialize_aws_json_1_1(
            value["provider"]
        )
    if "config_connector_arn" in value:
        out["ConfigConnectorArn"] = value["config_connector_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudConnectorSummary:
    out: CloudConnectorSummary = {}  # type: ignore[typeddict-item]
    if data.get("CloudConnectorId") is not None:
        out["cloud_connector_id"] = data["CloudConnectorId"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
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
    if data.get("Provider") is not None:
        import capo_ssm.types.provider

        out["provider"] = capo_ssm.types.provider.deserialize_aws_json_1_1(
            data["Provider"]
        )
    if data.get("ConfigConnectorArn") is not None:
        out["config_connector_arn"] = data["ConfigConnectorArn"]
    return out
