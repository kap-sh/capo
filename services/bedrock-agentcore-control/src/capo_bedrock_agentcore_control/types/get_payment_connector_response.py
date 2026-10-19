"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetPaymentConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.credentials_provider_configurations
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.payment_connector_authorization_url
    import capo_bedrock_agentcore_control.types.payment_connector_id
    import capo_bedrock_agentcore_control.types.payment_connector_name
    import capo_bedrock_agentcore_control.types.payment_connector_provision_mode
    import capo_bedrock_agentcore_control.types.payment_connector_status
    import capo_bedrock_agentcore_control.types.payment_connector_type
    import capo_bedrock_agentcore_control.types.payments_description


class GetPaymentConnectorResponse(TypedDict, closed=True):
    payment_connector_id: (
        "capo_bedrock_agentcore_control.types.payment_connector_id.PaymentConnectorId"
    )
    """<p>The unique identifier of the payment connector.</p>"""
    name: "capo_bedrock_agentcore_control.types.payment_connector_name.PaymentConnectorName"
    """<p>The name of the payment connector.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
    ]
    """<p>The description of the payment connector.</p>"""
    type: "capo_bedrock_agentcore_control.types.payment_connector_type.PaymentConnectorType"
    """<p>The type of the payment connector, which determines the payment provider integration.</p>"""
    provision_mode: NotRequired[
        "capo_bedrock_agentcore_control.types.payment_connector_provision_mode.PaymentConnectorProvisionMode"
    ]
    """<p>Specifies how the payment connector was provisioned. Payment connectors that were created before this field was available return <code>MANUAL</code>.</p> <ul> <li> <p> <code>MANUAL</code> - You provided the credential provider configurations, so you own the credentials. Rotate them with the payment provider, then call <code>UpdatePaymentCredentialProvider</code>.</p> </li> <li> <p> <code>QUICK_CREATE</code> - AgentCore provisioned the credential provider for you, so the credentials are service-managed. You can rotate them with <code>RotatePaymentConnectorCredentials</code>.</p> </li> </ul>"""
    credential_provider_configurations: "capo_bedrock_agentcore_control.types.credentials_provider_configurations.CredentialsProviderConfigurations"
    """<p>The credential provider configurations for the payment connector.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment connector was created.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment connector was last updated.</p>"""
    status: "capo_bedrock_agentcore_control.types.payment_connector_status.PaymentConnectorStatus"
    """<p>The current status of the payment connector. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, and <code>DELETE_FAILED</code>.</p>"""
    authorization_url: NotRequired[
        "capo_bedrock_agentcore_control.types.payment_connector_authorization_url.PaymentConnectorAuthorizationUrl"
    ]
    """<p>The URL that the user must open to complete OAuth consent. This field is only present when the payment connector status is <code>PENDING_AUTHENTICATION</code>.</p>"""
    credentials_updated_at: NotRequired[
        "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    ]
    """<p>The timestamp when the payment connector's current service-managed credentials took effect. It is first set when the credentials are provisioned and is updated by each rotation. This field is present only for payment connectors with a <code>provisionMode</code> of <code>QUICK_CREATE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPaymentConnectorResponse) -> dict:
    out: dict = {}
    out["paymentConnectorId"] = value["payment_connector_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.payment_connector_type

    out["type"] = (
        capo_bedrock_agentcore_control.types.payment_connector_type.serialize_json(
            value["type"]
        )
    )
    if "provision_mode" in value:
        import capo_bedrock_agentcore_control.types.payment_connector_provision_mode

        out["provisionMode"] = (
            capo_bedrock_agentcore_control.types.payment_connector_provision_mode.serialize_json(
                value["provision_mode"]
            )
        )
    import capo_bedrock_agentcore_control.types.credentials_provider_configurations

    out["credentialProviderConfigurations"] = (
        capo_bedrock_agentcore_control.types.credentials_provider_configurations.serialize_json(
            value["credential_provider_configurations"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.payment_connector_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.payment_connector_status.serialize_json(
            value["status"]
        )
    )
    if "authorization_url" in value:
        out["authorizationUrl"] = value["authorization_url"]
    if "credentials_updated_at" in value:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["credentialsUpdatedAt"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
                value["credentials_updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPaymentConnectorResponse:
    out: GetPaymentConnectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("paymentConnectorId") is not None:
        out["payment_connector_id"] = data["paymentConnectorId"]
    else:
        out["payment_connector_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agentcore_control.types.payment_connector_type.PaymentConnectorType",
            "",
        )
    if data.get("provisionMode") is not None:
        import capo_bedrock_agentcore_control.types.payment_connector_provision_mode

        out["provision_mode"] = (
            capo_bedrock_agentcore_control.types.payment_connector_provision_mode.deserialize_json(
                data["provisionMode"]
            )
        )
    if data.get("credentialProviderConfigurations") is not None:
        import capo_bedrock_agentcore_control.types.credentials_provider_configurations

        out["credential_provider_configurations"] = (
            capo_bedrock_agentcore_control.types.credentials_provider_configurations.deserialize_json(
                data["credentialProviderConfigurations"]
            )
        )
    else:
        out["credential_provider_configurations"] = []
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.payment_connector_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.payment_connector_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.payment_connector_status.PaymentConnectorStatus",
            "",
        )
    if data.get("authorizationUrl") is not None:
        out["authorization_url"] = data["authorizationUrl"]
    if data.get("credentialsUpdatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["credentials_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["credentialsUpdatedAt"]
            )
        )
    return out
