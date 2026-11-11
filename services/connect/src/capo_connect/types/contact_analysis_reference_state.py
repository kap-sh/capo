"""Generated from Smithy shape ``com.amazonaws.connect#ContactAnalysisReferenceState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.string


class ContactAnalysisReferenceState(TypedDict, closed=True):
    status: NotRequired["capo_connect.types.string.String"]
    """<p>The status of conversational analytics processing for the contact. Valid values:</p> <ul> <li> <p> <code>REQUESTED</code> – Analysis has been requested for the contact and has not finished.</p> </li> <li> <p> <code>COMPLETED</code> – Analysis finished successfully.</p> </li> <li> <p> <code>FAILED</code> – Analysis did not finish successfully. See <code>StatusReason</code> for the cause.</p> </li> </ul>"""
    status_reason: NotRequired["capo_connect.types.string.String"]
    """<p>The reason for the current analysis status. This value is populated only when the status is <code>FAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactAnalysisReferenceState) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> ContactAnalysisReferenceState:
    out: ContactAnalysisReferenceState = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    return out
