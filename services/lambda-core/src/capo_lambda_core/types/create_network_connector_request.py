"""Generated from Smithy shape ``com.amazonaws.lambdacore#CreateNetworkConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_core.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_core.types.client_token_string
    import capo_lambda_core.types.network_connector_configuration
    import capo_lambda_core.types.network_connector_name
    import capo_lambda_core.types.network_connector_role_arn
    import capo_lambda_core.types.network_connector_tags


class CreateNetworkConnectorRequest(TypedDict, closed=True):
    name: "capo_lambda_core.types.network_connector_name.NetworkConnectorName"
    """<p>A unique name for the network connector within your account and Region. You can use the name to identify the connector in subsequent API calls.</p>"""
    configuration: "capo_lambda_core.types.network_connector_configuration.NetworkConnectorConfiguration"
    """<p>The network configuration for the connector. Specify a <code>VpcEgressConfiguration</code> to enable outbound traffic routing through your VPC.</p>"""
    operator_role: NotRequired[
        "capo_lambda_core.types.network_connector_role_arn.NetworkConnectorRoleArn"
    ]
    """<p>The ARN of the IAM role that Lambda assumes to manage elastic network interfaces in your VPC. This role must have permissions for <code>ec2:CreateNetworkInterface</code>, <code>ec2:DeleteNetworkInterface</code>, and related describe operations.</p>"""
    client_token: NotRequired[
        "capo_lambda_core.types.client_token_string.ClientTokenString"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request with the same client token, the API returns the existing connector without creating a duplicate.</p>"""
    tags: NotRequired[
        "capo_lambda_core.types.network_connector_tags.NetworkConnectorTags"
    ]
    """<p>A map of key-value pairs to associate with the network connector for organization, cost allocation, or access control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNetworkConnectorRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
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
    if "tags" in value:
        import capo_lambda_core.types.network_connector_tags

        out["Tags"] = capo_lambda_core.types.network_connector_tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateNetworkConnectorRequest:
    out: CreateNetworkConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateNetworkConnectorRequest.name required")
    if data.get("Configuration") is not None:
        import capo_lambda_core.types.network_connector_configuration

        out["configuration"] = (
            capo_lambda_core.types.network_connector_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateNetworkConnectorRequest.configuration required"
        )
    if data.get("OperatorRole") is not None:
        out["operator_role"] = data["OperatorRole"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_lambda_core.types.network_connector_tags

        out["tags"] = capo_lambda_core.types.network_connector_tags.deserialize_json(
            data["Tags"]
        )
    return out
