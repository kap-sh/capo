"""Generated from Smithy shape ``com.amazonaws.quicksight#FailedKeyRegistrationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean
    import capo_quicksight.types.non_empty_string
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class FailedKeyRegistrationEntry(TypedDict, closed=True):
    key_arn: NotRequired["capo_quicksight.types.string.String"]
    """<p>The ARN of the KMS key that failed to update.</p>"""
    message: "capo_quicksight.types.non_empty_string.NonEmptyString"
    """<p>A message that provides information about why a <code>FailedKeyRegistrationEntry</code> error occurred.</p>"""
    status_code: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of a <code>FailedKeyRegistrationEntry</code> error.</p>"""
    sender_fault: "capo_quicksight.types.boolean.Boolean"
    """<p>A boolean that indicates whether a <code>FailedKeyRegistrationEntry</code> resulted from user error. If the value of this property is <code>True</code>, the error was caused by user error. If the value of this property is <code>False</code>, the error occurred on the backend. If your job continues fail and with a <code>False</code> <code>SenderFault</code> value, contact Amazon Web Services Support.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedKeyRegistrationEntry) -> dict:
    out: dict = {}
    if "key_arn" in value:
        out["KeyArn"] = value["key_arn"]
    out["Message"] = value["message"]
    out["StatusCode"] = value.get("status_code", 0)
    out["SenderFault"] = value.get("sender_fault", False)
    return out


def deserialize_json(data: dict) -> FailedKeyRegistrationEntry:
    out: FailedKeyRegistrationEntry = {}  # type: ignore[typeddict-item]
    if data.get("KeyArn") is not None:
        out["key_arn"] = data["KeyArn"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("StatusCode") is not None:
        out["status_code"] = data["StatusCode"]
    else:
        out["status_code"] = 0
    if data.get("SenderFault") is not None:
        out["sender_fault"] = data["SenderFault"]
    else:
        out["sender_fault"] = False
    return out
