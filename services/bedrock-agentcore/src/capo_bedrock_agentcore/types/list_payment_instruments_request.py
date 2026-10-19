"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListPaymentInstrumentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.next_token
    import capo_bedrock_agentcore.types.payment_agent_name
    import capo_bedrock_agentcore.types.payment_connector_id
    import capo_bedrock_agentcore.types.payment_manager_arn
    import capo_bedrock_agentcore.types.user_id


class ListPaymentInstrumentsRequest(TypedDict, closed=True):
    user_id: NotRequired["capo_bedrock_agentcore.types.user_id.UserId"]
    """<p>The user ID associated with the payment instruments.</p>"""
    agent_name: NotRequired[
        "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
    ]
    """<p>The agent name associated with this request, used for observability.</p>"""
    payment_manager_arn: (
        "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The ARN of the payment manager that owns the payment instruments.</p>"""
    payment_connector_id: NotRequired[
        "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
    ]
    """<p>The ID of the payment connector to filter by.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore.types.next_token.NextToken"]
    """<p>Token for pagination to retrieve the next set of results.</p>"""
    max_results: NotRequired["int"]
    """<p>Maximum number of results to return in a single response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPaymentInstrumentsRequest) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    if "payment_connector_id" in value:
        out["paymentConnectorId"] = value["payment_connector_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListPaymentInstrumentsRequest:
    out: ListPaymentInstrumentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("paymentManagerArn") is not None:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        out["payment_manager_arn"] = ""
    if data.get("paymentConnectorId") is not None:
        out["payment_connector_id"] = data["paymentConnectorId"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
