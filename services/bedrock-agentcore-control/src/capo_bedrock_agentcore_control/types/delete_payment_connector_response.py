"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeletePaymentConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.payment_connector_id
    import capo_bedrock_agentcore_control.types.payment_connector_status


class DeletePaymentConnectorResponse(TypedDict, closed=True):
    status: "capo_bedrock_agentcore_control.types.payment_connector_status.PaymentConnectorStatus"
    """<p>The current status of the payment connector, set to <code>DELETING</code> when deletion is initiated. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, and <code>DELETE_FAILED</code>.</p>"""
    payment_connector_id: NotRequired[
        "capo_bedrock_agentcore_control.types.payment_connector_id.PaymentConnectorId"
    ]
    """<p>The unique identifier of the deleted payment connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePaymentConnectorResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.payment_connector_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.payment_connector_status.serialize_json(
            value["status"]
        )
    )
    if "payment_connector_id" in value:
        out["paymentConnectorId"] = value["payment_connector_id"]
    return out


def deserialize_json(data: dict) -> DeletePaymentConnectorResponse:
    out: DeletePaymentConnectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.payment_connector_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.payment_connector_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.payment_connector_status.PaymentConnectorStatus",
            "",
        )
    if data.get("paymentConnectorId") is not None:
        out["payment_connector_id"] = data["paymentConnectorId"]
    return out
