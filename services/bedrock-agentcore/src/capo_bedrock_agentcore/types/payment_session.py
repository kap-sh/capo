"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentSession``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.available_limits
    import capo_bedrock_agentcore.types.date_timestamp
    import capo_bedrock_agentcore.types.payment_manager_arn
    import capo_bedrock_agentcore.types.payment_session_id
    import capo_bedrock_agentcore.types.session_limits
    import capo_bedrock_agentcore.types.user_id


class PaymentSession(TypedDict, closed=True):
    payment_session_id: (
        "capo_bedrock_agentcore.types.payment_session_id.PaymentSessionId"
    )
    """<p>The unique identifier of the payment session.</p>"""
    payment_manager_arn: (
        "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The ARN of the payment manager that owns this session.</p>"""
    limits: NotRequired["capo_bedrock_agentcore.types.session_limits.SessionLimits"]
    """<p>The spending limits for the payment session.</p>"""
    user_id: "capo_bedrock_agentcore.types.user_id.UserId"
    """<p>The user ID associated with this session.</p>"""
    expiry_time_in_minutes: "int"
    """<p>The session expiry time in minutes.</p>"""
    created_at: "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the session was created.</p>"""
    available_limits: NotRequired[
        "capo_bedrock_agentcore.types.available_limits.AvailableLimits"
    ]
    """<p>The current available spending limits.</p>"""
    updated_at: "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the session was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaymentSession) -> dict:
    out: dict = {}
    out["paymentSessionId"] = value["payment_session_id"]
    out["paymentManagerArn"] = value["payment_manager_arn"]
    if "limits" in value:
        import capo_bedrock_agentcore.types.session_limits

        out["limits"] = capo_bedrock_agentcore.types.session_limits.serialize_json(
            value["limits"]
        )
    out["userId"] = value["user_id"]
    out["expiryTimeInMinutes"] = value["expiry_time_in_minutes"]
    import capo_bedrock_agentcore.types.date_timestamp

    out["createdAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    if "available_limits" in value:
        import capo_bedrock_agentcore.types.available_limits

        out["availableLimits"] = (
            capo_bedrock_agentcore.types.available_limits.serialize_json(
                value["available_limits"]
            )
        )
    import capo_bedrock_agentcore.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> PaymentSession:
    out: PaymentSession = {}  # type: ignore[typeddict-item]
    if data.get("paymentSessionId") is not None:
        out["payment_session_id"] = data["paymentSessionId"]
    else:
        out["payment_session_id"] = ""
    if data.get("paymentManagerArn") is not None:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        out["payment_manager_arn"] = ""
    if data.get("limits") is not None:
        import capo_bedrock_agentcore.types.session_limits

        out["limits"] = capo_bedrock_agentcore.types.session_limits.deserialize_json(
            data["limits"]
        )
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        out["user_id"] = ""
    if data.get("expiryTimeInMinutes") is not None:
        out["expiry_time_in_minutes"] = data["expiryTimeInMinutes"]
    else:
        out["expiry_time_in_minutes"] = 0
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("availableLimits") is not None:
        import capo_bedrock_agentcore.types.available_limits

        out["available_limits"] = (
            capo_bedrock_agentcore.types.available_limits.deserialize_json(
                data["availableLimits"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
