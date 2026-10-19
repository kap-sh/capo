"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateCloudConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.cloud_connector_configuration
    import capo_ssm.types.cloud_connector_description
    import capo_ssm.types.cloud_connector_id
    import capo_ssm.types.display_name


class UpdateCloudConnectorRequest(TypedDict, closed=True):
    cloud_connector_id: "capo_ssm.types.cloud_connector_id.CloudConnectorId"
    """<p>The ID of the cloud connector to update.</p>"""
    display_name: NotRequired["capo_ssm.types.display_name.DisplayName"]
    """<p>A new friendly name for the cloud connector.</p>"""
    configuration: NotRequired[
        "capo_ssm.types.cloud_connector_configuration.CloudConnectorConfiguration"
    ]
    """<p>The updated configuration details for connecting to the third-party cloud environment.</p>"""
    description: NotRequired[
        "capo_ssm.types.cloud_connector_description.CloudConnectorDescription"
    ]
    """<p>A new description for the cloud connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCloudConnectorRequest) -> dict:
    out: dict = {}
    out["CloudConnectorId"] = value["cloud_connector_id"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "configuration" in value:
        import capo_ssm.types.cloud_connector_configuration

        out["Configuration"] = (
            capo_ssm.types.cloud_connector_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCloudConnectorRequest:
    out: UpdateCloudConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("CloudConnectorId") is not None:
        out["cloud_connector_id"] = data["CloudConnectorId"]
    else:
        out["cloud_connector_id"] = ""
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Configuration") is not None:
        import capo_ssm.types.cloud_connector_configuration

        out["configuration"] = (
            capo_ssm.types.cloud_connector_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
