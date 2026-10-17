"""Generated from Smithy shape ``com.amazonaws.lambdacore#UpdateNetworkConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.client_token_string
    import capo_lambda_core.types.network_connector_configuration
    import capo_lambda_core.types.network_connector_identifier
    import capo_lambda_core.types.network_connector_role_arn


class UpdateNetworkConnectorRequest(TypedDict, closed=True):
    identifier: (
        "capo_lambda_core.types.network_connector_identifier.NetworkConnectorIdentifier"
    )
    configuration: NotRequired[
        "capo_lambda_core.types.network_connector_configuration.NetworkConnectorConfiguration"
    ]
    """<p>The updated network configuration for the connector. Provide the full <code>VpcEgressConfiguration</code> including all subnet IDs and security group IDs — this replaces the existing configuration.</p>"""
    operator_role: NotRequired[
        "capo_lambda_core.types.network_connector_role_arn.NetworkConnectorRoleArn"
    ]
    """<p>The updated ARN of the IAM role that Lambda assumes to manage ENIs. Use this to change the operator role without recreating the connector.</p>"""
    client_token: NotRequired[
        "capo_lambda_core.types.client_token_string.ClientTokenString"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the update request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNetworkConnectorRequest) -> dict:
    out: dict = {}
    if "configuration" in value:
        import capo_lambda_core.types.network_connector_configuration

        out["Configuration"] = (
            capo_lambda_core.types.network_connector_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "operator_role" in value:
        out["OperatorRole"] = value["operator_role"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateNetworkConnectorRequest:
    out: UpdateNetworkConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("Configuration") is not None:
        import capo_lambda_core.types.network_connector_configuration

        out["configuration"] = (
            capo_lambda_core.types.network_connector_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    if data.get("OperatorRole") is not None:
        out["operator_role"] = data["OperatorRole"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
