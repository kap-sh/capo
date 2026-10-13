"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CreatePaymentInstrumentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.payment_agent_name
    import capo_bedrock_agentcore.types.payment_connector_id
    import capo_bedrock_agentcore.types.payment_instrument_details
    import capo_bedrock_agentcore.types.payment_instrument_type
    import capo_bedrock_agentcore.types.payment_manager_arn
    import capo_bedrock_agentcore.types.user_id


class CreatePaymentInstrumentRequest(TypedDict, closed=True):
    user_id: NotRequired["capo_bedrock_agentcore.types.user_id.UserId"]
    """<p>The user ID associated with this payment instrument.</p>"""
    agent_name: NotRequired[
        "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
    ]
    """<p>The agent name associated with this request, used for observability.</p>"""
    payment_manager_arn: (
        "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The ARN of the payment manager that owns this payment instrument.</p>"""
    payment_connector_id: (
        "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
    )
    """<p>The ID of the payment connector to use for this instrument.</p>"""
    payment_instrument_type: (
        "capo_bedrock_agentcore.types.payment_instrument_type.PaymentInstrumentType"
    )
    """<p>The type of payment instrument being created.</p>"""
    payment_instrument_details: "capo_bedrock_agentcore.types.payment_instrument_details.PaymentInstrumentDetails"
    """<p>The details of the payment instrument.</p>"""
    client_token: NotRequired["capo_bedrock_agentcore.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePaymentInstrumentRequest) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentConnectorId"] = value["payment_connector_id"]
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreatePaymentInstrumentRequest:
    out: CreatePaymentInstrumentRequest = {}  # type: ignore[typeddict-item]
    if data.get("paymentManagerArn") is not None:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        raise DeserializationError(
            "CreatePaymentInstrumentRequest.payment_manager_arn required"
        )
    if data.get("paymentConnectorId") is not None:
        out["payment_connector_id"] = data["paymentConnectorId"]
    else:
        raise DeserializationError(
            "CreatePaymentInstrumentRequest.payment_connector_id required"
        )
    if data.get("paymentInstrumentType") is not None:
        import capo_bedrock_agentcore.types.payment_instrument_type

        out["payment_instrument_type"] = (
            capo_bedrock_agentcore.types.payment_instrument_type.deserialize_json(
                data["paymentInstrumentType"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePaymentInstrumentRequest.payment_instrument_type required"
        )
    if data.get("paymentInstrumentDetails") is not None:
        import capo_bedrock_agentcore.types.payment_instrument_details

        out["payment_instrument_details"] = (
            capo_bedrock_agentcore.types.payment_instrument_details.deserialize_json(
                data["paymentInstrumentDetails"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePaymentInstrumentRequest.payment_instrument_details required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreatePaymentInstrumentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payment_instrument_details" in value:
        import capo_bedrock_agentcore.types.payment_instrument_details

        out["payment_instrument_details"] = (
            capo_bedrock_agentcore.types.payment_instrument_details.redact_sensitive(
                value["payment_instrument_details"]
            )
        )
    return out
