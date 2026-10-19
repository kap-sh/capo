"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ProcessPaymentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.date_timestamp
    import capo_bedrock_agentcore.types.payment_instrument_id
    import capo_bedrock_agentcore.types.payment_manager_arn
    import capo_bedrock_agentcore.types.payment_output
    import capo_bedrock_agentcore.types.payment_session_id
    import capo_bedrock_agentcore.types.payment_status
    import capo_bedrock_agentcore.types.payment_type
    import capo_bedrock_agentcore.types.process_payment_id


class ProcessPaymentResponse(TypedDict, closed=True):
    process_payment_id: (
        "capo_bedrock_agentcore.types.process_payment_id.ProcessPaymentId"
    )
    """<p>The unique identifier of the processed payment.</p>"""
    payment_manager_arn: (
        "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The ARN of the payment manager.</p>"""
    payment_session_id: (
        "capo_bedrock_agentcore.types.payment_session_id.PaymentSessionId"
    )
    """<p>The ID of the payment session used.</p>"""
    payment_instrument_id: (
        "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId"
    )
    """<p>The ID of the payment instrument used.</p>"""
    payment_type: "capo_bedrock_agentcore.types.payment_type.PaymentType"
    """<p>The type of payment processed.</p>"""
    status: "capo_bedrock_agentcore.types.payment_status.PaymentStatus"
    """<p>The status of the payment.</p>"""
    payment_output: "capo_bedrock_agentcore.types.payment_output.PaymentOutput"
    """<p>The payment output details specific to the payment type.</p>"""
    created_at: "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment was created.</p>"""
    updated_at: "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProcessPaymentResponse) -> dict:
    out: dict = {}
    out["processPaymentId"] = value["process_payment_id"]
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentSessionId"] = value["payment_session_id"]
    out["paymentInstrumentId"] = value["payment_instrument_id"]
    import capo_bedrock_agentcore.types.payment_type

    out["paymentType"] = capo_bedrock_agentcore.types.payment_type.serialize_json(
        value["payment_type"]
    )
    import capo_bedrock_agentcore.types.payment_status

    out["status"] = capo_bedrock_agentcore.types.payment_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agentcore.types.payment_output

    out["paymentOutput"] = capo_bedrock_agentcore.types.payment_output.serialize_json(
        value["payment_output"]
    )
    import capo_bedrock_agentcore.types.date_timestamp

    out["createdAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agentcore.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> ProcessPaymentResponse:
    out: ProcessPaymentResponse = {}  # type: ignore[typeddict-item]
    if data.get("processPaymentId") is not None:
        out["process_payment_id"] = data["processPaymentId"]
    else:
        out["process_payment_id"] = ""
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
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.payment_status

        out["status"] = capo_bedrock_agentcore.types.payment_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore.types.payment_status.PaymentStatus", ""
        )
    if data.get("paymentOutput") is not None:
        import capo_bedrock_agentcore.types.payment_output

        out["payment_output"] = (
            capo_bedrock_agentcore.types.payment_output.deserialize_json(
                data["paymentOutput"]
            )
        )
    else:
        import capo_bedrock_agentcore.types._unknown

        out["payment_output"] = (
            capo_bedrock_agentcore.types._unknown.UnknownUnionMember("")
        )
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


def redact_sensitive(value: ProcessPaymentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payment_output" in value:
        import capo_bedrock_agentcore.types.payment_output

        out["payment_output"] = (
            capo_bedrock_agentcore.types.payment_output.redact_sensitive(
                value["payment_output"]
            )
        )
    return out
