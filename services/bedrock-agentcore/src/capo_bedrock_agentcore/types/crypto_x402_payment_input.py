"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CryptoX402PaymentInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_document
    import capo_bedrock_agentcore.types.permit2_allowance_limit


class CryptoX402PaymentInput(TypedDict, closed=True):
    version: "str"
    """<p>The version of the X402 protocol.</p>"""
    payload: "capo_bedrock_agentcore.types.payment_document.PaymentDocument"
    """<p>The X402 payment payload.</p>"""
    permit2_allowance_limit: NotRequired[
        "capo_bedrock_agentcore.types.permit2_allowance_limit.Permit2AllowanceLimit"
    ]
    """<p>The maximum on-chain Permit2 allowance to grant before signing the payment authorization, in the asset's smallest denomination. This field is valid only for the <code>upto</code> (metered) scheme; supplying it for the <code>exact</code> scheme returns a validation error.</p> <p>When set, the service approves an ERC-20 allowance for this amount before processing the payment. The approval sets, rather than adds to, the wallet's allowance. Set this field only when the wallet needs approving, for example on its first <code>upto</code> payment, to avoid a redundant on-chain transaction. Omit the field to skip allowance handling. This is the default, and the only behavior for the <code>exact</code> scheme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CryptoX402PaymentInput) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    out["payload"] = value["payload"]
    if "permit2_allowance_limit" in value:
        out["permit2AllowanceLimit"] = value["permit2_allowance_limit"]
    return out


def deserialize_json(data: dict) -> CryptoX402PaymentInput:
    out: CryptoX402PaymentInput = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CryptoX402PaymentInput.version required")
    if data.get("payload") is not None:
        out["payload"] = data["payload"]
    else:
        raise DeserializationError("CryptoX402PaymentInput.payload required")
    if data.get("permit2AllowanceLimit") is not None:
        out["permit2_allowance_limit"] = data["permit2AllowanceLimit"]
    return out


def redact_sensitive(value: CryptoX402PaymentInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        out["payload"] = "*** Sensitive Data Redacted ***"
    return out
