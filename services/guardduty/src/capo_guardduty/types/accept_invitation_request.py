"""Generated from Smithy shape ``com.amazonaws.guardduty#AcceptInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.string


class AcceptInvitationRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector of the GuardDuty member account.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    master_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The account ID of the GuardDuty administrator account whose invitation you're accepting.</p>"""
    invitation_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The value that is used to validate the administrator account to the member account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptInvitationRequest) -> dict:
    out: dict = {}
    if "master_id" in value:
        out["masterId"] = value["master_id"]
    if "invitation_id" in value:
        out["invitationId"] = value["invitation_id"]
    return out


def deserialize_json(data: dict) -> AcceptInvitationRequest:
    out: AcceptInvitationRequest = {}  # type: ignore[typeddict-item]
    if data.get("masterId") is not None:
        out["master_id"] = data["masterId"]
    if data.get("invitationId") is not None:
        out["invitation_id"] = data["invitationId"]
    return out
