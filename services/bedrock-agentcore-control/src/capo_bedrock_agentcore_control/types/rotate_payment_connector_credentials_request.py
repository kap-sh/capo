"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RotatePaymentConnectorCredentialsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.credential_rotation_config
    import capo_bedrock_agentcore_control.types.payment_connector_id
    import capo_bedrock_agentcore_control.types.payment_manager_id


class RotatePaymentConnectorCredentialsRequest(TypedDict, closed=True):
    payment_manager_id: (
        "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId"
    )
    """<p>The unique identifier of the parent payment manager.</p>"""
    payment_connector_id: (
        "capo_bedrock_agentcore_control.types.payment_connector_id.PaymentConnectorId"
    )
    """<p>The unique identifier of the payment connector whose credentials you want to rotate.</p>"""
    credentials_to_rotate: "capo_bedrock_agentcore_control.types.credential_rotation_config.CredentialRotationConfig"
    """<p>The credentials to rotate. Specify the member that matches the payment connector's <code>type</code>. Each credential that you select is rotated independently.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RotatePaymentConnectorCredentialsRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.credential_rotation_config

    out["credentialsToRotate"] = (
        capo_bedrock_agentcore_control.types.credential_rotation_config.serialize_json(
            value["credentials_to_rotate"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> RotatePaymentConnectorCredentialsRequest:
    out: RotatePaymentConnectorCredentialsRequest = {}  # type: ignore[typeddict-item]
    if data.get("credentialsToRotate") is not None:
        import capo_bedrock_agentcore_control.types.credential_rotation_config

        out["credentials_to_rotate"] = (
            capo_bedrock_agentcore_control.types.credential_rotation_config.deserialize_json(
                data["credentialsToRotate"]
            )
        )
    else:
        raise DeserializationError(
            "RotatePaymentConnectorCredentialsRequest.credentials_to_rotate required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
