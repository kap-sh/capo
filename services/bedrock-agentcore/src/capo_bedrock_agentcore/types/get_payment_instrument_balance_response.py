"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetPaymentInstrumentBalanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_instrument_id
    import capo_bedrock_agentcore.types.token_balance


class GetPaymentInstrumentBalanceResponse(TypedDict, closed=True):
    payment_instrument_id: (
        "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId"
    )
    """<p>The ID of the payment instrument.</p>"""
    token_balance: "capo_bedrock_agentcore.types.token_balance.TokenBalance"
    """<p>The balance of the supported token on the requested chain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPaymentInstrumentBalanceResponse) -> dict:
    out: dict = {}
    out["paymentInstrumentId"] = value["payment_instrument_id"]
    import capo_bedrock_agentcore.types.token_balance

    out["tokenBalance"] = capo_bedrock_agentcore.types.token_balance.serialize_json(
        value["token_balance"]
    )
    return out


def deserialize_json(data: dict) -> GetPaymentInstrumentBalanceResponse:
    out: GetPaymentInstrumentBalanceResponse = {}  # type: ignore[typeddict-item]
    if data.get("paymentInstrumentId") is not None:
        out["payment_instrument_id"] = data["paymentInstrumentId"]
    else:
        out["payment_instrument_id"] = ""
    if data.get("tokenBalance") is not None:
        import capo_bedrock_agentcore.types.token_balance

        out["token_balance"] = (
            capo_bedrock_agentcore.types.token_balance.deserialize_json(
                data["tokenBalance"]
            )
        )
    else:
        raise DeserializationError(
            "GetPaymentInstrumentBalanceResponse.token_balance required"
        )
    return out
