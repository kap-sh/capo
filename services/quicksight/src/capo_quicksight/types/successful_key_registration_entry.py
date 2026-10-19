"""Generated from Smithy shape ``com.amazonaws.quicksight#SuccessfulKeyRegistrationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class SuccessfulKeyRegistrationEntry(TypedDict, closed=True):
    key_arn: "capo_quicksight.types.string.String"
    """<p>The ARN of the KMS key that is associated with the <code>SuccessfulKeyRegistrationEntry</code> entry.</p>"""
    status_code: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of a <code>SuccessfulKeyRegistrationEntry</code> entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulKeyRegistrationEntry) -> dict:
    out: dict = {}
    out["KeyArn"] = value["key_arn"]
    out["StatusCode"] = value.get("status_code", 0)
    return out


def deserialize_json(data: dict) -> SuccessfulKeyRegistrationEntry:
    out: SuccessfulKeyRegistrationEntry = {}  # type: ignore[typeddict-item]
    if data.get("KeyArn") is not None:
        out["key_arn"] = data["KeyArn"]
    else:
        out["key_arn"] = ""
    if data.get("StatusCode") is not None:
        out["status_code"] = data["StatusCode"]
    else:
        out["status_code"] = 0
    return out
