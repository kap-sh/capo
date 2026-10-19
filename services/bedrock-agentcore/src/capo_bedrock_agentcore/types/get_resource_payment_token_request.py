"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetResourcePaymentTokenRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.credential_provider_name
    import capo_bedrock_agentcore.types.payment_token_request_input
    import capo_bedrock_agentcore.types.workload_identity_token_type


class GetResourcePaymentTokenRequest(TypedDict, closed=True):
    workload_identity_token: "capo_bedrock_agentcore.types.workload_identity_token_type.WorkloadIdentityTokenType"
    """<p>Workload access token for authorization.</p>"""
    resource_credential_provider_name: (
        "capo_bedrock_agentcore.types.credential_provider_name.CredentialProviderName"
    )
    """<p>Name of the payment credential provider to use.</p>"""
    payment_token_request: "capo_bedrock_agentcore.types.payment_token_request_input.PaymentTokenRequestInput"
    """<p>Vendor-specific token request input. Contains all request parameters in a type-safe, vendor-specific structure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePaymentTokenRequest) -> dict:
    out: dict = {}
    out["workloadIdentityToken"] = value["workload_identity_token"]
    out["resourceCredentialProviderName"] = value["resource_credential_provider_name"]
    import capo_bedrock_agentcore.types.payment_token_request_input

    out["paymentTokenRequest"] = (
        capo_bedrock_agentcore.types.payment_token_request_input.serialize_json(
            value["payment_token_request"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetResourcePaymentTokenRequest:
    out: GetResourcePaymentTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("workloadIdentityToken") is not None:
        out["workload_identity_token"] = data["workloadIdentityToken"]
    else:
        out["workload_identity_token"] = ""
    if data.get("resourceCredentialProviderName") is not None:
        out["resource_credential_provider_name"] = data[
            "resourceCredentialProviderName"
        ]
    else:
        out["resource_credential_provider_name"] = ""
    if data.get("paymentTokenRequest") is not None:
        import capo_bedrock_agentcore.types.payment_token_request_input

        out["payment_token_request"] = (
            capo_bedrock_agentcore.types.payment_token_request_input.deserialize_json(
                data["paymentTokenRequest"]
            )
        )
    else:
        import capo_bedrock_agentcore.types._unknown

        out["payment_token_request"] = (
            capo_bedrock_agentcore.types._unknown.UnknownUnionMember("")
        )
    return out


def redact_sensitive(value: GetResourcePaymentTokenRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "workload_identity_token" in value:
        out["workload_identity_token"] = "*** Sensitive Data Redacted ***"
    if "payment_token_request" in value:
        import capo_bedrock_agentcore.types.payment_token_request_input

        out["payment_token_request"] = (
            capo_bedrock_agentcore.types.payment_token_request_input.redact_sensitive(
                value["payment_token_request"]
            )
        )
    return out
