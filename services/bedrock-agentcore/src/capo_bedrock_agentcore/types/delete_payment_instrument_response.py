"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeletePaymentInstrumentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_instrument_status


class DeletePaymentInstrumentResponse(TypedDict, closed=True):
    status: (
        "capo_bedrock_agentcore.types.payment_instrument_status.PaymentInstrumentStatus"
    )
    """<p>The status of the instrument after deletion. Always DELETED for successful soft delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePaymentInstrumentResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.payment_instrument_status

    out["status"] = (
        capo_bedrock_agentcore.types.payment_instrument_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeletePaymentInstrumentResponse:
    out: DeletePaymentInstrumentResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.payment_instrument_status

        out["status"] = (
            capo_bedrock_agentcore.types.payment_instrument_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore.types.payment_instrument_status.PaymentInstrumentStatus",
            "",
        )
    return out
