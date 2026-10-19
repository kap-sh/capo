"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentInstrument``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.date_timestamp
    import capo_bedrock_agentcore.types.payment_connector_id
    import capo_bedrock_agentcore.types.payment_instrument_details
    import capo_bedrock_agentcore.types.payment_instrument_id
    import capo_bedrock_agentcore.types.payment_instrument_status
    import capo_bedrock_agentcore.types.payment_instrument_type
    import capo_bedrock_agentcore.types.payment_manager_arn
    import capo_bedrock_agentcore.types.user_id


class PaymentInstrument(TypedDict, closed=True):
    payment_instrument_id: (
        "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId"
    )
    """<p>The unique identifier for this payment instrument.</p>"""
    payment_manager_arn: (
        "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The ARN of the payment manager that owns this payment instrument.</p>"""
    payment_connector_id: (
        "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
    )
    """<p>The ID of the payment connector associated with this instrument.</p>"""
    user_id: "capo_bedrock_agentcore.types.user_id.UserId"
    """<p>The user ID associated with this payment instrument.</p>"""
    payment_instrument_type: (
        "capo_bedrock_agentcore.types.payment_instrument_type.PaymentInstrumentType"
    )
    """<p>The type of payment instrument (e.g., EMBEDDED_CRYPTO_WALLET).</p>"""
    payment_instrument_details: "capo_bedrock_agentcore.types.payment_instrument_details.PaymentInstrumentDetails"
    """<p>The details specific to the payment instrument type.</p>"""
    created_at: "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when this payment instrument was created.</p>"""
    status: (
        "capo_bedrock_agentcore.types.payment_instrument_status.PaymentInstrumentStatus"
    )
    """<p>The current status of this payment instrument.</p>"""
    updated_at: "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when this payment instrument was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaymentInstrument) -> dict:
    out: dict = {}
    out["paymentInstrumentId"] = value["payment_instrument_id"]
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentConnectorId"] = value["payment_connector_id"]
    out["userId"] = value["user_id"]
    import capo_bedrock_agentcore.types.payment_instrument_type

    out["paymentInstrumentType"] = (
        capo_bedrock_agentcore.types.payment_instrument_type.serialize_json(
            value["payment_instrument_type"]
        )
    )
    import capo_bedrock_agentcore.types.payment_instrument_details

    out["paymentInstrumentDetails"] = (
        capo_bedrock_agentcore.types.payment_instrument_details.serialize_json(
            value["payment_instrument_details"]
        )
    )
    import capo_bedrock_agentcore.types.date_timestamp

    out["createdAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agentcore.types.payment_instrument_status

    out["status"] = (
        capo_bedrock_agentcore.types.payment_instrument_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock_agentcore.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> PaymentInstrument:
    out: PaymentInstrument = {}  # type: ignore[typeddict-item]
    if data.get("paymentInstrumentId") is not None:
        out["payment_instrument_id"] = data["paymentInstrumentId"]
    else:
        out["payment_instrument_id"] = ""
    if data.get("paymentManagerArn") is not None:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        out["payment_manager_arn"] = ""
    if data.get("paymentConnectorId") is not None:
        out["payment_connector_id"] = data["paymentConnectorId"]
    else:
        out["payment_connector_id"] = ""
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        out["user_id"] = ""
    if data.get("paymentInstrumentType") is not None:
        import capo_bedrock_agentcore.types.payment_instrument_type

        out["payment_instrument_type"] = (
            capo_bedrock_agentcore.types.payment_instrument_type.deserialize_json(
                data["paymentInstrumentType"]
            )
        )
    else:
        import typing

        out["payment_instrument_type"] = typing.cast(
            "capo_bedrock_agentcore.types.payment_instrument_type.PaymentInstrumentType",
            "",
        )
    if data.get("paymentInstrumentDetails") is not None:
        import capo_bedrock_agentcore.types.payment_instrument_details

        out["payment_instrument_details"] = (
            capo_bedrock_agentcore.types.payment_instrument_details.deserialize_json(
                data["paymentInstrumentDetails"]
            )
        )
    else:
        import capo_bedrock_agentcore.types._unknown

        out["payment_instrument_details"] = (
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
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.payment_instrument_status

        out["status"] = (
            capo_bedrock_agentcore.types.payment_instrument_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore.types.payment_instrument_status.PaymentInstrumentStatus",
            "",
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


def redact_sensitive(value: PaymentInstrument) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payment_instrument_details" in value:
        import capo_bedrock_agentcore.types.payment_instrument_details

        out["payment_instrument_details"] = (
            capo_bedrock_agentcore.types.payment_instrument_details.redact_sensitive(
                value["payment_instrument_details"]
            )
        )
    return out
