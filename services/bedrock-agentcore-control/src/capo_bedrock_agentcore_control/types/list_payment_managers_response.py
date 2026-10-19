"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPaymentManagersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.payment_manager_summaries


class ListPaymentManagersResponse(TypedDict, closed=True):
    payment_managers: "capo_bedrock_agentcore_control.types.payment_manager_summaries.PaymentManagerSummaries"
    """<p>The list of payment manager summaries. For details about the fields in each summary, see the <code>PaymentManagerSummary</code> data type.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPaymentManagersResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.payment_manager_summaries

    out["paymentManagers"] = (
        capo_bedrock_agentcore_control.types.payment_manager_summaries.serialize_json(
            value["payment_managers"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPaymentManagersResponse:
    out: ListPaymentManagersResponse = {}  # type: ignore[typeddict-item]
    if data.get("paymentManagers") is not None:
        import capo_bedrock_agentcore_control.types.payment_manager_summaries

        out["payment_managers"] = (
            capo_bedrock_agentcore_control.types.payment_manager_summaries.deserialize_json(
                data["paymentManagers"]
            )
        )
    else:
        out["payment_managers"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
