"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MppPaymentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.mpp_payment_credential
    import capo_bedrock_agentcore.types.version


class MppPaymentOutput(TypedDict, closed=True):
    version: "capo_bedrock_agentcore.types.version.Version"
    """<p>The MPP protocol version, for example "1" or "2".</p>"""
    selected_payment_id: "str"
    """<p>The id of the challenge that was paid, echoed from the input challenge so you can correlate the result without decoding the credential.</p>"""
    payment_credential: (
        "capo_bedrock_agentcore.types.mpp_payment_credential.MppPaymentCredential"
    )
    """<p>Ready-to-send value for the <code>Authorization</code> header, in the form "Payment &lt;base64url-token&gt;". Attach this header and retry the original request. To inspect the full credential, base64url-decode the token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MppPaymentOutput) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    out["selectedPaymentId"] = value["selected_payment_id"]
    out["paymentCredential"] = value["payment_credential"]
    return out


def deserialize_json(data: dict) -> MppPaymentOutput:
    out: MppPaymentOutput = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("MppPaymentOutput.version required")
    if data.get("selectedPaymentId") is not None:
        out["selected_payment_id"] = data["selectedPaymentId"]
    else:
        raise DeserializationError("MppPaymentOutput.selected_payment_id required")
    if data.get("paymentCredential") is not None:
        out["payment_credential"] = data["paymentCredential"]
    else:
        raise DeserializationError("MppPaymentOutput.payment_credential required")
    return out
