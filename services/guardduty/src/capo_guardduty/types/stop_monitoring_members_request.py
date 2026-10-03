"""Generated from Smithy shape ``com.amazonaws.guardduty#StopMonitoringMembersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_ids
    import capo_guardduty.types.detector_id


class StopMonitoringMembersRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector associated with the GuardDuty administrator account that is monitoring member accounts.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    account_ids: NotRequired["capo_guardduty.types.account_ids.AccountIds"]
    """<p>A list of account IDs for the member accounts to stop monitoring.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopMonitoringMembersRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_guardduty.types.account_ids

        out["accountIds"] = capo_guardduty.types.account_ids.serialize_json(
            value["account_ids"]
        )
    return out


def deserialize_json(data: dict) -> StopMonitoringMembersRequest:
    out: StopMonitoringMembersRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_guardduty.types.account_ids

        out["account_ids"] = capo_guardduty.types.account_ids.deserialize_json(
            data["accountIds"]
        )
    return out
