"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetPaymentInstrumentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_instrument


class GetPaymentInstrumentResponse(TypedDict, closed=True):
    payment_instrument: (
        "capo_bedrock_agentcore.types.payment_instrument.PaymentInstrument"
    )
    """<p>The payment instrument details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPaymentInstrumentResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.payment_instrument

    out["paymentInstrument"] = (
        capo_bedrock_agentcore.types.payment_instrument.serialize_json(
            value["payment_instrument"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetPaymentInstrumentResponse:
    out: GetPaymentInstrumentResponse = {}  # type: ignore[typeddict-item]
    if data.get("paymentInstrument") is not None:
        import capo_bedrock_agentcore.types.payment_instrument

        out["payment_instrument"] = (
            capo_bedrock_agentcore.types.payment_instrument.deserialize_json(
                data["paymentInstrument"]
            )
        )
    else:
        raise DeserializationError(
            "GetPaymentInstrumentResponse.payment_instrument required"
        )
    return out


def redact_sensitive(value: GetPaymentInstrumentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payment_instrument" in value:
        import capo_bedrock_agentcore.types.payment_instrument

        out["payment_instrument"] = (
            capo_bedrock_agentcore.types.payment_instrument.redact_sensitive(
                value["payment_instrument"]
            )
        )
    return out
