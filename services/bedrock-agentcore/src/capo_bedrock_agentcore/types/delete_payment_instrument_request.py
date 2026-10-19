"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeletePaymentInstrumentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_connector_id
    import capo_bedrock_agentcore.types.payment_instrument_id
    import capo_bedrock_agentcore.types.payment_manager_arn
    import capo_bedrock_agentcore.types.user_id


class DeletePaymentInstrumentRequest(TypedDict, closed=True):
    user_id: NotRequired["capo_bedrock_agentcore.types.user_id.UserId"]
    """<p>The user ID making the delete request. Must match the instrument's userId.</p>"""
    payment_manager_arn: (
        "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The payment manager ARN. Must match the instrument's paymentManagerArn.</p>"""
    payment_connector_id: (
        "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
    )
    """<p>The payment connector ID. Must match the instrument's paymentConnectorId.</p>"""
    payment_instrument_id: (
        "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId"
    )
    """<p>The payment instrument ID to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePaymentInstrumentRequest) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentConnectorId"] = value["payment_connector_id"]
    out["paymentInstrumentId"] = value["payment_instrument_id"]
    return out


def deserialize_json(data: dict) -> DeletePaymentInstrumentRequest:
    out: DeletePaymentInstrumentRequest = {}  # type: ignore[typeddict-item]
    if data.get("paymentManagerArn") is not None:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        out["payment_manager_arn"] = ""
    if data.get("paymentConnectorId") is not None:
        out["payment_connector_id"] = data["paymentConnectorId"]
    else:
        out["payment_connector_id"] = ""
    if data.get("paymentInstrumentId") is not None:
        out["payment_instrument_id"] = data["paymentInstrumentId"]
    else:
        out["payment_instrument_id"] = ""
    return out
