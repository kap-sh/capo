"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CreatePaymentSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.payment_agent_name
    import capo_bedrock_agentcore.types.payment_manager_arn
    import capo_bedrock_agentcore.types.session_limits
    import capo_bedrock_agentcore.types.user_id


class CreatePaymentSessionRequest(TypedDict, closed=True):
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
    limits: NotRequired["capo_bedrock_agentcore.types.session_limits.SessionLimits"]
    """<p>The spending limits for this payment session.</p>"""
    expiry_time_in_minutes: "int"
    """<p>The session expiry time in minutes. Must be between 15 and 480 minutes.</p>"""
    client_token: NotRequired["capo_bedrock_agentcore.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePaymentSessionRequest) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    if "limits" in value:
        import capo_bedrock_agentcore.types.session_limits

        out["limits"] = capo_bedrock_agentcore.types.session_limits.serialize_json(
            value["limits"]
        )
    out["expiryTimeInMinutes"] = value["expiry_time_in_minutes"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreatePaymentSessionRequest:
    out: CreatePaymentSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("paymentManagerArn") is not None:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        out["payment_manager_arn"] = ""
    if data.get("limits") is not None:
        import capo_bedrock_agentcore.types.session_limits

        out["limits"] = capo_bedrock_agentcore.types.session_limits.deserialize_json(
            data["limits"]
        )
    if data.get("expiryTimeInMinutes") is not None:
        out["expiry_time_in_minutes"] = data["expiryTimeInMinutes"]
    else:
        out["expiry_time_in_minutes"] = 0
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
