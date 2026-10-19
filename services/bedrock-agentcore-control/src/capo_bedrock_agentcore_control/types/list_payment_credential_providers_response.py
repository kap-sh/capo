"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPaymentCredentialProvidersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.payment_credential_providers


class ListPaymentCredentialProvidersResponse(TypedDict, closed=True):
    credential_providers: "capo_bedrock_agentcore_control.types.payment_credential_providers.PaymentCredentialProviders"
    """<p>The list of payment credential providers.</p>"""
    next_token: NotRequired["str"]
    """<p>Pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPaymentCredentialProvidersResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.payment_credential_providers

    out["credentialProviders"] = (
        capo_bedrock_agentcore_control.types.payment_credential_providers.serialize_json(
            value["credential_providers"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPaymentCredentialProvidersResponse:
    out: ListPaymentCredentialProvidersResponse = {}  # type: ignore[typeddict-item]
    if data.get("credentialProviders") is not None:
        import capo_bedrock_agentcore_control.types.payment_credential_providers

        out["credential_providers"] = (
            capo_bedrock_agentcore_control.types.payment_credential_providers.deserialize_json(
                data["credentialProviders"]
            )
        )
    else:
        out["credential_providers"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
