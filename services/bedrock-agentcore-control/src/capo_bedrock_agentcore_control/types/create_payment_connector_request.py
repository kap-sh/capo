"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreatePaymentConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.credentials_provider_configurations
    import capo_bedrock_agentcore_control.types.payment_connector_name
    import capo_bedrock_agentcore_control.types.payment_connector_provision_mode
    import capo_bedrock_agentcore_control.types.payment_connector_type
    import capo_bedrock_agentcore_control.types.payment_manager_id
    import capo_bedrock_agentcore_control.types.payments_description


class CreatePaymentConnectorRequest(TypedDict, closed=True):
    payment_manager_id: (
        "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId"
    )
    """<p>The unique identifier of the payment manager to create the connector for.</p>"""
    name: "capo_bedrock_agentcore_control.types.payment_connector_name.PaymentConnectorName"
    """<p>The name of the payment connector.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
    ]
    """<p>A description of the payment connector.</p>"""
    type: "capo_bedrock_agentcore_control.types.payment_connector_type.PaymentConnectorType"
    """<p>The type of payment connector, which determines the payment provider integration.</p>"""
    credential_provider_configurations: "capo_bedrock_agentcore_control.types.credentials_provider_configurations.CredentialsProviderConfigurations"
    """<p>The credential provider configurations for the payment connector. These configurations specify how the connector authenticates with the payment provider.</p>"""
    provision_mode: NotRequired[
        "capo_bedrock_agentcore_control.types.payment_connector_provision_mode.PaymentConnectorProvisionMode"
    ]
    """<p>The provision mode for creating the payment connector. If you don't specify a value, the default is <code>MANUAL</code>.</p> <ul> <li> <p> <code>MANUAL</code> - You provide the credential provider configurations directly.</p> </li> <li> <p> <code>QUICK_CREATE</code> - The service orchestrates OAuth consent and provisions the credential provider for you.</p> </li> </ul>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePaymentConnectorRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.payment_connector_type

    out["type"] = (
        capo_bedrock_agentcore_control.types.payment_connector_type.serialize_json(
            value["type"]
        )
    )
    import capo_bedrock_agentcore_control.types.credentials_provider_configurations

    out["credentialProviderConfigurations"] = (
        capo_bedrock_agentcore_control.types.credentials_provider_configurations.serialize_json(
            value["credential_provider_configurations"]
        )
    )
    if "provision_mode" in value:
        import capo_bedrock_agentcore_control.types.payment_connector_provision_mode

        out["provisionMode"] = (
            capo_bedrock_agentcore_control.types.payment_connector_provision_mode.serialize_json(
                value["provision_mode"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreatePaymentConnectorRequest:
    out: CreatePaymentConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreatePaymentConnectorRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        import capo_bedrock_agentcore_control.types.payment_connector_type

        out["type"] = (
            capo_bedrock_agentcore_control.types.payment_connector_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("CreatePaymentConnectorRequest.type required")
    if data.get("credentialProviderConfigurations") is not None:
        import capo_bedrock_agentcore_control.types.credentials_provider_configurations

        out["credential_provider_configurations"] = (
            capo_bedrock_agentcore_control.types.credentials_provider_configurations.deserialize_json(
                data["credentialProviderConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePaymentConnectorRequest.credential_provider_configurations required"
        )
    if data.get("provisionMode") is not None:
        import capo_bedrock_agentcore_control.types.payment_connector_provision_mode

        out["provision_mode"] = (
            capo_bedrock_agentcore_control.types.payment_connector_provision_mode.deserialize_json(
                data["provisionMode"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
