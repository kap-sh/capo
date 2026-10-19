"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.core_timestamp
    import capo_lambda_core.types.network_connector_arn
    import capo_lambda_core.types.network_connector_id
    import capo_lambda_core.types.network_connector_name
    import capo_lambda_core.types.network_connector_state
    import capo_lambda_core.types.network_connector_type
    import capo_lambda_core.types.network_connector_version


class NetworkConnectorSummary(TypedDict, closed=True):
    arn: "capo_lambda_core.types.network_connector_arn.NetworkConnectorArn"
    """<p>The ARN of the network connector.</p>"""
    name: "capo_lambda_core.types.network_connector_name.NetworkConnectorName"
    """<p>The name of the network connector.</p>"""
    id: "capo_lambda_core.types.network_connector_id.NetworkConnectorId"
    """<p>The unique identifier of the network connector.</p>"""
    type: "capo_lambda_core.types.network_connector_type.NetworkConnectorType"
    """<p>The type of the network connector (<code>VPC_EGRESS</code>).</p>"""
    state: NotRequired[
        "capo_lambda_core.types.network_connector_state.NetworkConnectorState"
    ]
    """<p>The current state of the network connector.</p>"""
    last_modified: NotRequired["capo_lambda_core.types.core_timestamp.CoreTimestamp"]
    """<p>The date and time when the connector was last modified.</p>"""
    latest_version_arn: NotRequired[
        "capo_lambda_core.types.network_connector_arn.NetworkConnectorArn"
    ]
    """<p>The qualified ARN of the connector's latest version, including the immutable version suffix.</p>"""
    latest_version: NotRequired[
        "capo_lambda_core.types.network_connector_version.NetworkConnectorVersion"
    ]
    """<p>The version number of the connector's latest version. Each configuration update creates a new immutable version; this attribute exposes the most recent one.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    out["Id"] = value["id"]
    import capo_lambda_core.types.network_connector_type

    out["Type"] = capo_lambda_core.types.network_connector_type.serialize_json(
        value["type"]
    )
    if "state" in value:
        import capo_lambda_core.types.network_connector_state

        out["State"] = capo_lambda_core.types.network_connector_state.serialize_json(
            value["state"]
        )
    if "last_modified" in value:
        import capo_lambda_core.types.core_timestamp

        out["LastModified"] = capo_lambda_core.types.core_timestamp.serialize_json(
            value["last_modified"]
        )
    if "latest_version_arn" in value:
        out["LatestVersionArn"] = value["latest_version_arn"]
    if "latest_version" in value:
        out["LatestVersion"] = value["latest_version"]
    return out


def deserialize_json(data: dict) -> NetworkConnectorSummary:
    out: NetworkConnectorSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("Type") is not None:
        import capo_lambda_core.types.network_connector_type

        out["type"] = capo_lambda_core.types.network_connector_type.deserialize_json(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_lambda_core.types.network_connector_type.NetworkConnectorType", ""
        )
    if data.get("State") is not None:
        import capo_lambda_core.types.network_connector_state

        out["state"] = capo_lambda_core.types.network_connector_state.deserialize_json(
            data["State"]
        )
    if data.get("LastModified") is not None:
        import capo_lambda_core.types.core_timestamp

        out["last_modified"] = capo_lambda_core.types.core_timestamp.deserialize_json(
            data["LastModified"]
        )
    if data.get("LatestVersionArn") is not None:
        out["latest_version_arn"] = data["LatestVersionArn"]
    if data.get("LatestVersion") is not None:
        out["latest_version"] = data["LatestVersion"]
    return out
