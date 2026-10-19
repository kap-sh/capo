"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeletePaymentSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_manager_arn
    import capo_bedrock_agentcore.types.payment_session_id
    import capo_bedrock_agentcore.types.user_id


class DeletePaymentSessionRequest(TypedDict, closed=True):
    user_id: NotRequired["capo_bedrock_agentcore.types.user_id.UserId"]
    """<p>The user ID making the delete request. Must match the session's userId.</p>"""
    payment_manager_arn: (
        "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The payment manager ARN. Must match the session's paymentManagerArn.</p>"""
    payment_session_id: (
        "capo_bedrock_agentcore.types.payment_session_id.PaymentSessionId"
    )
    """<p>The payment session ID to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePaymentSessionRequest) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentSessionId"] = value["payment_session_id"]
    return out


def deserialize_json(data: dict) -> DeletePaymentSessionRequest:
    out: DeletePaymentSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("paymentManagerArn") is not None:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        out["payment_manager_arn"] = ""
    if data.get("paymentSessionId") is not None:
        out["payment_session_id"] = data["paymentSessionId"]
    else:
        out["payment_session_id"] = ""
    return out
