"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPaymentConnectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.payment_connector_summaries


class ListPaymentConnectorsResponse(TypedDict, closed=True):
    payment_connectors: "capo_bedrock_agentcore_control.types.payment_connector_summaries.PaymentConnectorSummaries"
    """<p>The list of payment connector summaries. For details about the fields in each summary, see the <code>PaymentConnectorSummary</code> data type.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPaymentConnectorsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.payment_connector_summaries

    out["paymentConnectors"] = (
        capo_bedrock_agentcore_control.types.payment_connector_summaries.serialize_json(
            value["payment_connectors"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPaymentConnectorsResponse:
    out: ListPaymentConnectorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("paymentConnectors") is not None:
        import capo_bedrock_agentcore_control.types.payment_connector_summaries

        out["payment_connectors"] = (
            capo_bedrock_agentcore_control.types.payment_connector_summaries.deserialize_json(
                data["paymentConnectors"]
            )
        )
    else:
        out["payment_connectors"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
