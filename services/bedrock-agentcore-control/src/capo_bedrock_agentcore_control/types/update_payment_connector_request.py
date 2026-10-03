"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatePaymentConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.credentials_provider_configurations
    import capo_bedrock_agentcore_control.types.payment_connector_id
    import capo_bedrock_agentcore_control.types.payment_connector_type
    import capo_bedrock_agentcore_control.types.payment_manager_id
    import capo_bedrock_agentcore_control.types.payments_description


class UpdatePaymentConnectorRequest(TypedDict, closed=True):
    payment_manager_id: (
        "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId"
    )
    """<p>The unique identifier of the parent payment manager.</p>"""
    payment_connector_id: (
        "capo_bedrock_agentcore_control.types.payment_connector_id.PaymentConnectorId"
    )
    """<p>The unique identifier of the payment connector to update.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
    ]
    """<p>The updated description of the payment connector.</p>"""
    type: NotRequired[
        "capo_bedrock_agentcore_control.types.payment_connector_type.PaymentConnectorType"
    ]
    """<p>The updated type of the payment connector.</p>"""
    credential_provider_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.credentials_provider_configurations.CredentialsProviderConfigurations"
    ]
    """<p>The updated credential provider configurations for the payment connector.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePaymentConnectorRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "type" in value:
        import capo_bedrock_agentcore_control.types.payment_connector_type

        out["type"] = (
            capo_bedrock_agentcore_control.types.payment_connector_type.serialize_json(
                value["type"]
            )
        )
    if "credential_provider_configurations" in value:
        import capo_bedrock_agentcore_control.types.credentials_provider_configurations

        out["credentialProviderConfigurations"] = (
            capo_bedrock_agentcore_control.types.credentials_provider_configurations.serialize_json(
                value["credential_provider_configurations"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdatePaymentConnectorRequest:
    out: UpdatePaymentConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        import capo_bedrock_agentcore_control.types.payment_connector_type

        out["type"] = (
            capo_bedrock_agentcore_control.types.payment_connector_type.deserialize_json(
                data["type"]
            )
        )
    if data.get("credentialProviderConfigurations") is not None:
        import capo_bedrock_agentcore_control.types.credentials_provider_configurations

        out["credential_provider_configurations"] = (
            capo_bedrock_agentcore_control.types.credentials_provider_configurations.deserialize_json(
                data["credentialProviderConfigurations"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
