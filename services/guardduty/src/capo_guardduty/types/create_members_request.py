"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateMembersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_details
    import capo_guardduty.types.detector_id


class CreateMembersRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector of the GuardDuty account for which you want to associate member accounts.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    account_details: NotRequired["capo_guardduty.types.account_details.AccountDetails"]
    """<p>A list of account ID and email address pairs of the accounts that you want to associate with the GuardDuty administrator account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMembersRequest) -> dict:
    out: dict = {}
    if "account_details" in value:
        import capo_guardduty.types.account_details

        out["accountDetails"] = capo_guardduty.types.account_details.serialize_json(
            value["account_details"]
        )
    return out


def deserialize_json(data: dict) -> CreateMembersRequest:
    out: CreateMembersRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountDetails") is not None:
        import capo_guardduty.types.account_details

        out["account_details"] = capo_guardduty.types.account_details.deserialize_json(
            data["accountDetails"]
        )
    return out
