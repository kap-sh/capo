"""Generated from Smithy shape ``com.amazonaws.lambdacore#GetNetworkConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.core_timestamp
    import capo_lambda_core.types.network_connector_arn
    import capo_lambda_core.types.network_connector_configuration
    import capo_lambda_core.types.network_connector_id
    import capo_lambda_core.types.network_connector_last_update_status
    import capo_lambda_core.types.network_connector_last_update_status_reason
    import capo_lambda_core.types.network_connector_last_update_status_reason_code
    import capo_lambda_core.types.network_connector_name
    import capo_lambda_core.types.network_connector_role_arn
    import capo_lambda_core.types.network_connector_state
    import capo_lambda_core.types.network_connector_state_reason_code
    import capo_lambda_core.types.network_connector_version
    import capo_lambda_core.types.string


class GetNetworkConnectorResponse(TypedDict, closed=True):
    arn: "capo_lambda_core.types.network_connector_arn.NetworkConnectorArn"
    """<p>The Amazon Resource Name (ARN) of the network connector.</p>"""
    name: "capo_lambda_core.types.network_connector_name.NetworkConnectorName"
    """<p>The name of the network connector.</p>"""
    id: "capo_lambda_core.types.network_connector_id.NetworkConnectorId"
    """<p>The unique identifier of the network connector.</p>"""
    version_arn: NotRequired[
        "capo_lambda_core.types.network_connector_arn.NetworkConnectorArn"
    ]
    """<p>The qualified ARN of the specific connector version returned by this request, including the immutable version suffix. This is populated only when you supply a version-qualified identifier. On a standard (unqualified) request, this field is not populated; the connector's latest active version is returned instead through the <code>LatestVersionArn</code> and <code>LatestVersion</code> fields described below.</p>"""
    version: NotRequired[
        "capo_lambda_core.types.network_connector_version.NetworkConnectorVersion"
    ]
    """<p>The version number of the network connector. On a standard (unqualified) request, this is the connector's current version; each configuration update increments it. When you supply a version-qualified identifier, this is the specific version you requested.</p>"""
    latest_version_arn: NotRequired[
        "capo_lambda_core.types.network_connector_arn.NetworkConnectorArn"
    ]
    """<p>The qualified ARN of the connector's latest active version, including the immutable version suffix. This field is returned only on a standard (unqualified) request; when you supply a version-qualified identifier it is not returned, and <code>VersionArn</code> is returned instead.</p>"""
    latest_version: NotRequired[
        "capo_lambda_core.types.network_connector_version.NetworkConnectorVersion"
    ]
    """<p>The version number of the connector's latest active version. Each configuration update creates a new immutable version; this attribute exposes the most recent one. This field is returned only on a standard (unqualified) request.</p>"""
    configuration: NotRequired[
        "capo_lambda_core.types.network_connector_configuration.NetworkConnectorConfiguration"
    ]
    """<p>The network configuration of the connector, including VPC subnets and security groups.</p>"""
    operator_role: NotRequired[
        "capo_lambda_core.types.network_connector_role_arn.NetworkConnectorRoleArn"
    ]
    """<p>The ARN of the IAM role that Lambda uses to manage the underlying ENI resources for this connector.</p>"""
    state: NotRequired[
        "capo_lambda_core.types.network_connector_state.NetworkConnectorState"
    ]
    """<p>The current state of the network connector.</p>"""
    state_reason: NotRequired["capo_lambda_core.types.string.String"]
    """<p>A human-readable explanation of the current state, populated when the state is <code>FAILED</code> or <code>DELETE_FAILED</code>.</p>"""
    state_reason_code: NotRequired[
        "capo_lambda_core.types.network_connector_state_reason_code.NetworkConnectorStateReasonCode"
    ]
    """<p>A machine-readable code indicating the reason for the current state. Use this for programmatic error handling.</p>"""
    last_update_status: NotRequired[
        "capo_lambda_core.types.network_connector_last_update_status.NetworkConnectorLastUpdateStatus"
    ]
    """<p>The status of the most recent update operation (<code>Successful</code>, <code>Failed</code>, or <code>InProgress</code>).</p>"""
    last_update_status_reason: NotRequired[
        "capo_lambda_core.types.network_connector_last_update_status_reason.NetworkConnectorLastUpdateStatusReason"
    ]
    """<p>A human-readable explanation of the last update status.</p>"""
    last_update_status_reason_code: NotRequired[
        "capo_lambda_core.types.network_connector_last_update_status_reason_code.NetworkConnectorLastUpdateStatusReasonCode"
    ]
    """<p>A machine-readable code indicating the reason for the last update status. Use this for programmatic error handling.</p>"""
    last_modified: NotRequired["capo_lambda_core.types.core_timestamp.CoreTimestamp"]
    """<p>The date and time when the connector configuration was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkConnectorResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    out["Id"] = value["id"]
    if "version_arn" in value:
        out["VersionArn"] = value["version_arn"]
    if "version" in value:
        out["Version"] = value["version"]
    if "latest_version_arn" in value:
        out["LatestVersionArn"] = value["latest_version_arn"]
    if "latest_version" in value:
        out["LatestVersion"] = value["latest_version"]
    if "configuration" in value:
        import capo_lambda_core.types.network_connector_configuration

        out["Configuration"] = (
            capo_lambda_core.types.network_connector_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "operator_role" in value:
        out["OperatorRole"] = value["operator_role"]
    if "state" in value:
        import capo_lambda_core.types.network_connector_state

        out["State"] = capo_lambda_core.types.network_connector_state.serialize_json(
            value["state"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "state_reason_code" in value:
        import capo_lambda_core.types.network_connector_state_reason_code

        out["StateReasonCode"] = (
            capo_lambda_core.types.network_connector_state_reason_code.serialize_json(
                value["state_reason_code"]
            )
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
    if "last_update_status_reason_code" in value:
        import capo_lambda_core.types.network_connector_last_update_status_reason_code

        out["LastUpdateStatusReasonCode"] = (
            capo_lambda_core.types.network_connector_last_update_status_reason_code.serialize_json(
                value["last_update_status_reason_code"]
            )
        )
    if "last_modified" in value:
        import capo_lambda_core.types.core_timestamp

        out["LastModified"] = capo_lambda_core.types.core_timestamp.serialize_json(
            value["last_modified"]
        )
    return out


def deserialize_json(data: dict) -> GetNetworkConnectorResponse:
    out: GetNetworkConnectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("VersionArn") is not None:
        out["version_arn"] = data["VersionArn"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("LatestVersionArn") is not None:
        out["latest_version_arn"] = data["LatestVersionArn"]
    if data.get("LatestVersion") is not None:
        out["latest_version"] = data["LatestVersion"]
    if data.get("Configuration") is not None:
        import capo_lambda_core.types.network_connector_configuration

        out["configuration"] = (
            capo_lambda_core.types.network_connector_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    if data.get("OperatorRole") is not None:
        out["operator_role"] = data["OperatorRole"]
    if data.get("State") is not None:
        import capo_lambda_core.types.network_connector_state

        out["state"] = capo_lambda_core.types.network_connector_state.deserialize_json(
            data["State"]
        )
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("StateReasonCode") is not None:
        import capo_lambda_core.types.network_connector_state_reason_code

        out["state_reason_code"] = (
            capo_lambda_core.types.network_connector_state_reason_code.deserialize_json(
                data["StateReasonCode"]
            )
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
    if data.get("LastUpdateStatusReasonCode") is not None:
        import capo_lambda_core.types.network_connector_last_update_status_reason_code

        out["last_update_status_reason_code"] = (
            capo_lambda_core.types.network_connector_last_update_status_reason_code.deserialize_json(
                data["LastUpdateStatusReasonCode"]
            )
        )
    if data.get("LastModified") is not None:
        import capo_lambda_core.types.core_timestamp

        out["last_modified"] = capo_lambda_core.types.core_timestamp.deserialize_json(
            data["LastModified"]
        )
    return out
