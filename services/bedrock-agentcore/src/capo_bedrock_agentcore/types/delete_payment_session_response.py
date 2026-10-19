"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeletePaymentSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_session_status


class DeletePaymentSessionResponse(TypedDict, closed=True):
    status: "capo_bedrock_agentcore.types.payment_session_status.PaymentSessionStatus"
    """<p>The status of the deletion. Always DELETED for successful hard delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePaymentSessionResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.payment_session_status

    out["status"] = capo_bedrock_agentcore.types.payment_session_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeletePaymentSessionResponse:
    out: DeletePaymentSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.payment_session_status

        out["status"] = (
            capo_bedrock_agentcore.types.payment_session_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore.types.payment_session_status.PaymentSessionStatus",
            "",
        )
    return out
