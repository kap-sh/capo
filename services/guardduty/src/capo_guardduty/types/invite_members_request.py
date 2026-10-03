"""Generated from Smithy shape ``com.amazonaws.guardduty#InviteMembersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_ids
    import capo_guardduty.types.boolean
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.string


class InviteMembersRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector of the GuardDuty account with which you want to invite members.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    account_ids: NotRequired["capo_guardduty.types.account_ids.AccountIds"]
    """<p>A list of account IDs of the accounts that you want to invite to GuardDuty as members.</p>"""
    disable_email_notification: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>A Boolean value that specifies whether you want to disable email notification to the accounts that you are inviting to GuardDuty as members.</p>"""
    message: NotRequired["capo_guardduty.types.string.String"]
    """<p>The invitation message that you want to send to the accounts that you're inviting to GuardDuty as members.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InviteMembersRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_guardduty.types.account_ids

        out["accountIds"] = capo_guardduty.types.account_ids.serialize_json(
            value["account_ids"]
        )
    if "disable_email_notification" in value:
        out["disableEmailNotification"] = value["disable_email_notification"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InviteMembersRequest:
    out: InviteMembersRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_guardduty.types.account_ids

        out["account_ids"] = capo_guardduty.types.account_ids.deserialize_json(
            data["accountIds"]
        )
    if data.get("disableEmailNotification") is not None:
        out["disable_email_notification"] = data["disableEmailNotification"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
