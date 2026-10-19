"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentCredentialProviderConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.payment_credential_provider_arn


class PaymentCredentialProviderConfiguration(TypedDict, closed=True):
    credential_provider_arn: "capo_bedrock_agentcore_control.types.payment_credential_provider_arn.PaymentCredentialProviderArn"
    """<p>The Amazon Resource Name (ARN) of the credential provider that stores the authentication credentials for the payment provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaymentCredentialProviderConfiguration) -> dict:
    out: dict = {}
    out["credentialProviderArn"] = value["credential_provider_arn"]
    return out


def deserialize_json(data: dict) -> PaymentCredentialProviderConfiguration:
    out: PaymentCredentialProviderConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("credentialProviderArn") is not None:
        out["credential_provider_arn"] = data["credentialProviderArn"]
    else:
        out["credential_provider_arn"] = ""
    return out
