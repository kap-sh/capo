"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListPaymentSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.next_token
    import capo_bedrock_agentcore.types.payment_session_summary_list


class ListPaymentSessionsResponse(TypedDict, closed=True):
    payment_sessions: "capo_bedrock_agentcore.types.payment_session_summary_list.PaymentSessionSummaryList"
    """<p>List of payment session summaries matching the request criteria.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore.types.next_token.NextToken"]
    """<p>Token for pagination to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPaymentSessionsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.payment_session_summary_list

    out["paymentSessions"] = (
        capo_bedrock_agentcore.types.payment_session_summary_list.serialize_json(
            value["payment_sessions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPaymentSessionsResponse:
    out: ListPaymentSessionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("paymentSessions") is not None:
        import capo_bedrock_agentcore.types.payment_session_summary_list

        out["payment_sessions"] = (
            capo_bedrock_agentcore.types.payment_session_summary_list.deserialize_json(
                data["paymentSessions"]
            )
        )
    else:
        out["payment_sessions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
