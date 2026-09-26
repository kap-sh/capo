"""Generated from Smithy shape ``com.amazonaws.lambdacore#DeleteNetworkConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_core.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_core.types.network_connector_arn
    import capo_lambda_core.types.network_connector_configuration
    import capo_lambda_core.types.network_connector_id
    import capo_lambda_core.types.network_connector_name
    import capo_lambda_core.types.network_connector_role_arn
    import capo_lambda_core.types.network_connector_state


class DeleteNetworkConnectorResponse(TypedDict, closed=True):
    arn: "capo_lambda_core.types.network_connector_arn.NetworkConnectorArn"
    """<p>The Amazon Resource Name (ARN) of the network connector.</p>"""
    name: "capo_lambda_core.types.network_connector_name.NetworkConnectorName"
    """<p>The name of the network connector.</p>"""
    id: "capo_lambda_core.types.network_connector_id.NetworkConnectorId"
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
    """<p>The current state of the network connector. The State field is typically <code>DELETING</code> after this call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNetworkConnectorResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    out["Id"] = value["id"]
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
    return out


def deserialize_json(data: dict) -> DeleteNetworkConnectorResponse:
    out: DeleteNetworkConnectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DeleteNetworkConnectorResponse.arn required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteNetworkConnectorResponse.name required")
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DeleteNetworkConnectorResponse.id required")
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
    return out
