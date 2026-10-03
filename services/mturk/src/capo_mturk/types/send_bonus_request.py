"""Generated from Smithy shape ``com.amazonaws.mturk#SendBonusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mturk.types.currency_amount
    import capo_mturk.types.customer_id
    import capo_mturk.types.entity_id
    import capo_mturk.types.idempotency_token
    import capo_mturk.types.string


class SendBonusRequest(TypedDict, closed=True):
    worker_id: "capo_mturk.types.customer_id.CustomerId"
    """<p>The ID of the Worker being paid the bonus.</p>"""
    bonus_amount: "capo_mturk.types.currency_amount.CurrencyAmount"
    """<p> The Bonus amount is a US Dollar amount specified using a string (for example, "5" represents $5.00 USD and "101.42" represents $101.42 USD). Do not include currency symbols or currency codes. </p>"""
    assignment_id: "capo_mturk.types.entity_id.EntityId"
    """<p>The ID of the assignment for which this bonus is paid.</p>"""
    reason: "capo_mturk.types.string.String"
    """<p>A message that explains the reason for the bonus payment. The Worker receiving the bonus can see this message.</p>"""
    unique_request_token: NotRequired[
        "capo_mturk.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique identifier for this request, which allows you to retry the call on error without granting multiple bonuses. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the bonus already exists in the system from a previous call using the same UniqueRequestToken, subsequent calls will return an error with a message containing the request ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendBonusRequest) -> dict:
    out: dict = {}
    out["WorkerId"] = value["worker_id"]
    out["BonusAmount"] = value["bonus_amount"]
    out["AssignmentId"] = value["assignment_id"]
    out["Reason"] = value["reason"]
    if "unique_request_token" in value:
        out["UniqueRequestToken"] = value["unique_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SendBonusRequest:
    out: SendBonusRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkerId") is not None:
        out["worker_id"] = data["WorkerId"]
    else:
        raise DeserializationError("SendBonusRequest.worker_id required")
    if data.get("BonusAmount") is not None:
        out["bonus_amount"] = data["BonusAmount"]
    else:
        raise DeserializationError("SendBonusRequest.bonus_amount required")
    if data.get("AssignmentId") is not None:
        out["assignment_id"] = data["AssignmentId"]
    else:
        raise DeserializationError("SendBonusRequest.assignment_id required")
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    else:
        raise DeserializationError("SendBonusRequest.reason required")
    if data.get("UniqueRequestToken") is not None:
        out["unique_request_token"] = data["UniqueRequestToken"]
    return out
