"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetPaymentSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_agent_name
    import capo_bedrock_agentcore.types.payment_manager_arn
    import capo_bedrock_agentcore.types.payment_session_id
    import capo_bedrock_agentcore.types.user_id


class GetPaymentSessionRequest(TypedDict, closed=True):
    user_id: NotRequired["capo_bedrock_agentcore.types.user_id.UserId"]
    """<p>The user ID associated with this payment session.</p>"""
    agent_name: NotRequired[
        "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
    ]
    """<p>The agent name associated with this request, used for observability.</p>"""
    payment_manager_arn: (
        "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The ARN of the payment manager that owns this session.</p>"""
    payment_session_id: (
        "capo_bedrock_agentcore.types.payment_session_id.PaymentSessionId"
    )
    """<p>The ID of the payment session to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPaymentSessionRequest) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentSessionId"] = value["payment_session_id"]
    return out


def deserialize_json(data: dict) -> GetPaymentSessionRequest:
    out: GetPaymentSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("paymentManagerArn") is not None:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        out["payment_manager_arn"] = ""
    if data.get("paymentSessionId") is not None:
        out["payment_session_id"] = data["paymentSessionId"]
    else:
        out["payment_session_id"] = ""
    return out
