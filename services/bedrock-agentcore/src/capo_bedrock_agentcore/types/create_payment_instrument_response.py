"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CreatePaymentInstrumentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_instrument


class CreatePaymentInstrumentResponse(TypedDict, closed=True):
    payment_instrument: (
        "capo_bedrock_agentcore.types.payment_instrument.PaymentInstrument"
    )
    """<p>The created payment instrument.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePaymentInstrumentResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.payment_instrument

    out["paymentInstrument"] = (
        capo_bedrock_agentcore.types.payment_instrument.serialize_json(
            value["payment_instrument"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreatePaymentInstrumentResponse:
    out: CreatePaymentInstrumentResponse = {}  # type: ignore[typeddict-item]
    if data.get("paymentInstrument") is not None:
        import capo_bedrock_agentcore.types.payment_instrument

        out["payment_instrument"] = (
            capo_bedrock_agentcore.types.payment_instrument.deserialize_json(
                data["paymentInstrument"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePaymentInstrumentResponse.payment_instrument required"
        )
    return out


def redact_sensitive(value: CreatePaymentInstrumentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payment_instrument" in value:
        import capo_bedrock_agentcore.types.payment_instrument

        out["payment_instrument"] = (
            capo_bedrock_agentcore.types.payment_instrument.redact_sensitive(
                value["payment_instrument"]
            )
        )
    return out
