"""Generated from Smithy shape ``com.amazonaws.lambdacore#UpdateNetworkConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_core.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_core.types.core_timestamp
    import capo_lambda_core.types.network_connector_arn
    import capo_lambda_core.types.network_connector_configuration
    import capo_lambda_core.types.network_connector_id
    import capo_lambda_core.types.network_connector_last_update_status
    import capo_lambda_core.types.network_connector_last_update_status_reason
    import capo_lambda_core.types.network_connector_name
    import capo_lambda_core.types.network_connector_role_arn
    import capo_lambda_core.types.network_connector_state
    import capo_lambda_core.types.network_connector_version


class UpdateNetworkConnectorResponse(TypedDict, closed=True):
    arn: "capo_lambda_core.types.network_connector_arn.NetworkConnectorArn"
    """<p>The Amazon Resource Name (ARN) of the network connector.</p>"""
    name: "capo_lambda_core.types.network_connector_name.NetworkConnectorName"
    """<p>The name of the network connector.</p>"""
    id: "capo_lambda_core.types.network_connector_id.NetworkConnectorId"
    """<p>The unique identifier of the network connector.</p>"""
    version_arn: NotRequired[
        "capo_lambda_core.types.network_connector_arn.NetworkConnectorArn"
    ]
    """<p>The qualified ARN of the connector version resulting from this update, including the immutable version suffix.</p>"""
    version: NotRequired[
        "capo_lambda_core.types.network_connector_version.NetworkConnectorVersion"
    ]
    """<p>The version number of the connector version resulting from this update. A configuration change creates a new, incremented version; a no-op update returns the current version number.</p>"""
    operator_role: NotRequired[
        "capo_lambda_core.types.network_connector_role_arn.NetworkConnectorRoleArn"
    ]
    """<p>The ARN of the IAM role that Lambda uses to manage the underlying ENI resources for this connector.</p>"""
    configuration: NotRequired[
        "capo_lambda_core.types.network_connector_configuration.NetworkConnectorConfiguration"
    ]
    """<p>The network configuration of the connector, including VPC subnets and security groups.</p>"""
    state: NotRequired[
        "capo_lambda_core.types.network_connector_state.NetworkConnectorState"
    ]
    """<p>The current state of the network connector.</p>"""
    last_update_status: NotRequired[
        "capo_lambda_core.types.network_connector_last_update_status.NetworkConnectorLastUpdateStatus"
    ]
    """<p>The status of this update operation (typically <code>InProgress</code> immediately after the call).</p>"""
    last_update_status_reason: NotRequired[
        "capo_lambda_core.types.network_connector_last_update_status_reason.NetworkConnectorLastUpdateStatusReason"
    ]
    """<p>A human-readable explanation of the update status.</p>"""
    last_modified: NotRequired["capo_lambda_core.types.core_timestamp.CoreTimestamp"]
    """<p>The timestamp of this update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNetworkConnectorResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    out["Id"] = value["id"]
    if "version_arn" in value:
        out["VersionArn"] = value["version_arn"]
    if "version" in value:
        out["Version"] = value["version"]
    if "operator_role" in value:
        out["OperatorRole"] = value["operator_role"]
    if "configuration" in value:
        import capo_lambda_core.types.network_connector_configuration

        out["Configuration"] = (
            capo_lambda_core.types.network_connector_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "state" in value:
        import capo_lambda_core.types.network_connector_state

        out["State"] = capo_lambda_core.types.network_connector_state.serialize_json(
            value["state"]
        )
    if "last_update_status" in value:
        import capo_lambda_core.types.network_connector_last_update_status

        out["LastUpdateStatus"] = (
            capo_lambda_core.types.network_connector_last_update_status.serialize_json(
                value["last_update_status"]
            )
        )
    if "last_update_status_reason" in value:
        out["LastUpdateStatusReason"] = value["last_update_status_reason"]
    if "last_modified" in value:
        import capo_lambda_core.types.core_timestamp

        out["LastModified"] = capo_lambda_core.types.core_timestamp.serialize_json(
            value["last_modified"]
        )
    return out


def deserialize_json(data: dict) -> UpdateNetworkConnectorResponse:
    out: UpdateNetworkConnectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdateNetworkConnectorResponse.arn required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateNetworkConnectorResponse.name required")
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateNetworkConnectorResponse.id required")
    if data.get("VersionArn") is not None:
        out["version_arn"] = data["VersionArn"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("OperatorRole") is not None:
        out["operator_role"] = data["OperatorRole"]
    if data.get("Configuration") is not None:
        import capo_lambda_core.types.network_connector_configuration

        out["configuration"] = (
            capo_lambda_core.types.network_connector_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    if data.get("State") is not None:
        import capo_lambda_core.types.network_connector_state

        out["state"] = capo_lambda_core.types.network_connector_state.deserialize_json(
            data["State"]
        )
    if data.get("LastUpdateStatus") is not None:
        import capo_lambda_core.types.network_connector_last_update_status

        out["last_update_status"] = (
            capo_lambda_core.types.network_connector_last_update_status.deserialize_json(
                data["LastUpdateStatus"]
            )
        )
    if data.get("LastUpdateStatusReason") is not None:
        out["last_update_status_reason"] = data["LastUpdateStatusReason"]
    if data.get("LastModified") is not None:
        import capo_lambda_core.types.core_timestamp

        out["last_modified"] = capo_lambda_core.types.core_timestamp.deserialize_json(
            data["LastModified"]
        )
    return out
