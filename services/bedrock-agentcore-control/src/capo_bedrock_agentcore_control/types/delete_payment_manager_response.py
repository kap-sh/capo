"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeletePaymentManagerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.payment_manager_id
    import capo_bedrock_agentcore_control.types.payment_manager_status


class DeletePaymentManagerResponse(TypedDict, closed=True):
    status: "capo_bedrock_agentcore_control.types.payment_manager_status.PaymentManagerStatus"
    """<p>The current status of the payment manager, set to <code>DELETING</code> when deletion is initiated. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, and <code>DELETE_FAILED</code>.</p>"""
    payment_manager_id: NotRequired[
        "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId"
    ]
    """<p>The unique identifier of the deleted payment manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePaymentManagerResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.payment_manager_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.payment_manager_status.serialize_json(
            value["status"]
        )
    )
    if "payment_manager_id" in value:
        out["paymentManagerId"] = value["payment_manager_id"]
    return out


def deserialize_json(data: dict) -> DeletePaymentManagerResponse:
    out: DeletePaymentManagerResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.payment_manager_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.payment_manager_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.payment_manager_status.PaymentManagerStatus",
            "",
        )
    if data.get("paymentManagerId") is not None:
        out["payment_manager_id"] = data["paymentManagerId"]
    return out
