"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_core.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_core.types.core_timestamp
    import capo_lambda_core.types.network_connector_arn
    import capo_lambda_core.types.network_connector_id
    import capo_lambda_core.types.network_connector_name
    import capo_lambda_core.types.network_connector_state
    import capo_lambda_core.types.network_connector_state_reason_code
    import capo_lambda_core.types.network_connector_version
    import capo_lambda_core.types.string


class NetworkConnectorVersionSummary(TypedDict, closed=True):
    arn: "capo_lambda_core.types.network_connector_arn.NetworkConnectorArn"
    """<p>The unqualified ARN of the network connector that this version belongs to.</p>"""
    version_arn: "capo_lambda_core.types.network_connector_arn.NetworkConnectorArn"
    """<p>The qualified ARN of this connector version, including the immutable version suffix.</p>"""
    name: "capo_lambda_core.types.network_connector_name.NetworkConnectorName"
    """<p>The name of the network connector.</p>"""
    id: "capo_lambda_core.types.network_connector_id.NetworkConnectorId"
    """<p>The unique identifier of the network connector.</p>"""
    version: "capo_lambda_core.types.network_connector_version.NetworkConnectorVersion"
    """<p>The version number of this connector version.</p>"""
    state: "capo_lambda_core.types.network_connector_state.NetworkConnectorState"
    """<p>The current state of this connector version.</p>"""
    state_reason: NotRequired["capo_lambda_core.types.string.String"]
    """<p>A human-readable explanation of the current state, populated when the state is <code>FAILED</code>.</p>"""
    state_reason_code: NotRequired[
        "capo_lambda_core.types.network_connector_state_reason_code.NetworkConnectorStateReasonCode"
    ]
    """<p>A machine-readable code indicating the reason for the current state. Use this for programmatic error handling.</p>"""
    last_modified: NotRequired["capo_lambda_core.types.core_timestamp.CoreTimestamp"]
    """<p>The date and time when this connector version was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorVersionSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["VersionArn"] = value["version_arn"]
    out["Name"] = value["name"]
    out["Id"] = value["id"]
    out["Version"] = value["version"]
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
    if "last_modified" in value:
        import capo_lambda_core.types.core_timestamp

        out["LastModified"] = capo_lambda_core.types.core_timestamp.serialize_json(
            value["last_modified"]
        )
    return out


def deserialize_json(data: dict) -> NetworkConnectorVersionSummary:
    out: NetworkConnectorVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("NetworkConnectorVersionSummary.arn required")
    if data.get("VersionArn") is not None:
        out["version_arn"] = data["VersionArn"]
    else:
        raise DeserializationError(
            "NetworkConnectorVersionSummary.version_arn required"
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("NetworkConnectorVersionSummary.name required")
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("NetworkConnectorVersionSummary.id required")
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        raise DeserializationError("NetworkConnectorVersionSummary.version required")
    if data.get("State") is not None:
        import capo_lambda_core.types.network_connector_state

        out["state"] = capo_lambda_core.types.network_connector_state.deserialize_json(
            data["State"]
        )
    else:
        raise DeserializationError("NetworkConnectorVersionSummary.state required")
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("StateReasonCode") is not None:
        import capo_lambda_core.types.network_connector_state_reason_code

        out["state_reason_code"] = (
            capo_lambda_core.types.network_connector_state_reason_code.deserialize_json(
                data["StateReasonCode"]
            )
        )
    if data.get("LastModified") is not None:
        import capo_lambda_core.types.core_timestamp

        out["last_modified"] = capo_lambda_core.types.core_timestamp.deserialize_json(
            data["LastModified"]
        )
    return out
