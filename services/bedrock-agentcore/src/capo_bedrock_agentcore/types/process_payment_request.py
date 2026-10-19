"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ProcessPaymentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.payment_agent_name
    import capo_bedrock_agentcore.types.payment_input
    import capo_bedrock_agentcore.types.payment_instrument_id
    import capo_bedrock_agentcore.types.payment_manager_arn
    import capo_bedrock_agentcore.types.payment_session_id
    import capo_bedrock_agentcore.types.payment_type
    import capo_bedrock_agentcore.types.user_id


class ProcessPaymentRequest(TypedDict, closed=True):
    user_id: NotRequired["capo_bedrock_agentcore.types.user_id.UserId"]
    """<p>The user ID associated with this payment.</p>"""
    agent_name: NotRequired[
        "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
    ]
    """<p>The agent name associated with this request, used for observability.</p>"""
    payment_manager_arn: (
        "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The ARN of the payment manager.</p>"""
    payment_session_id: (
        "capo_bedrock_agentcore.types.payment_session_id.PaymentSessionId"
    )
    """<p>The ID of the payment session.</p>"""
    payment_instrument_id: (
        "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId"
    )
    """<p>The ID of the payment instrument to use.</p>"""
    payment_type: "capo_bedrock_agentcore.types.payment_type.PaymentType"
    """<p>The type of payment to process.</p>"""
    payment_input: "capo_bedrock_agentcore.types.payment_input.PaymentInput"
    """<p>The payment input details specific to the payment type.</p>"""
    client_token: NotRequired["capo_bedrock_agentcore.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProcessPaymentRequest) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentSessionId"] = value["payment_session_id"]
    out["paymentInstrumentId"] = value["payment_instrument_id"]
    import capo_bedrock_agentcore.types.payment_type

    out["paymentType"] = capo_bedrock_agentcore.types.payment_type.serialize_json(
        value["payment_type"]
    )
    import capo_bedrock_agentcore.types.payment_input

    out["paymentInput"] = capo_bedrock_agentcore.types.payment_input.serialize_json(
        value["payment_input"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ProcessPaymentRequest:
    out: ProcessPaymentRequest = {}  # type: ignore[typeddict-item]
    if data.get("paymentManagerArn") is not None:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        out["payment_manager_arn"] = ""
    if data.get("paymentSessionId") is not None:
        out["payment_session_id"] = data["paymentSessionId"]
    else:
        out["payment_session_id"] = ""
    if data.get("paymentInstrumentId") is not None:
        out["payment_instrument_id"] = data["paymentInstrumentId"]
    else:
        out["payment_instrument_id"] = ""
    if data.get("paymentType") is not None:
        import capo_bedrock_agentcore.types.payment_type

        out["payment_type"] = (
            capo_bedrock_agentcore.types.payment_type.deserialize_json(
                data["paymentType"]
            )
        )
    else:
        import typing

        out["payment_type"] = typing.cast(
            "capo_bedrock_agentcore.types.payment_type.PaymentType", ""
        )
    if data.get("paymentInput") is not None:
        import capo_bedrock_agentcore.types.payment_input

        out["payment_input"] = (
            capo_bedrock_agentcore.types.payment_input.deserialize_json(
                data["paymentInput"]
            )
        )
    else:
        import capo_bedrock_agentcore.types._unknown

        out["payment_input"] = capo_bedrock_agentcore.types._unknown.UnknownUnionMember(
            ""
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: ProcessPaymentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payment_input" in value:
        import capo_bedrock_agentcore.types.payment_input

        out["payment_input"] = (
            capo_bedrock_agentcore.types.payment_input.redact_sensitive(
                value["payment_input"]
            )
        )
    return out
