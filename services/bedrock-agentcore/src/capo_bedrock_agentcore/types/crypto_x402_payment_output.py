"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CryptoX402PaymentOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_document


class CryptoX402PaymentOutput(TypedDict, closed=True):
    version: "str"
    """<p>The version of the X402 protocol.</p>"""
    payload: "capo_bedrock_agentcore.types.payment_document.PaymentDocument"
    """<p>The X402 payment response payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CryptoX402PaymentOutput) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    out["payload"] = value["payload"]
    return out


def deserialize_json(data: dict) -> CryptoX402PaymentOutput:
    out: CryptoX402PaymentOutput = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("payload") is not None:
        out["payload"] = data["payload"]
    else:
        out["payload"] = None
    return out


def redact_sensitive(value: CryptoX402PaymentOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        out["payload"] = "*** Sensitive Data Redacted ***"
    return out
