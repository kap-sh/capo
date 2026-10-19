"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListPaymentInstrumentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_instrument_summary_list


class ListPaymentInstrumentsResponse(TypedDict, closed=True):
    payment_instruments: "capo_bedrock_agentcore.types.payment_instrument_summary_list.PaymentInstrumentSummaryList"
    """<p>List of payment instrument summaries matching the request criteria.</p>"""
    next_token: NotRequired["str"]
    """<p>Token for pagination to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPaymentInstrumentsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.payment_instrument_summary_list

    out["paymentInstruments"] = (
        capo_bedrock_agentcore.types.payment_instrument_summary_list.serialize_json(
            value["payment_instruments"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPaymentInstrumentsResponse:
    out: ListPaymentInstrumentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("paymentInstruments") is not None:
        import capo_bedrock_agentcore.types.payment_instrument_summary_list

        out["payment_instruments"] = (
            capo_bedrock_agentcore.types.payment_instrument_summary_list.deserialize_json(
                data["paymentInstruments"]
            )
        )
    else:
        out["payment_instruments"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
