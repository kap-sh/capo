"""Generated from Smithy shape ``com.amazonaws.guardduty#GetRemainingFreeTrialDaysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_guardduty.errors import DeserializationError

if TYPE_CHECKING:
    import capo_guardduty.types.account_ids
    import capo_guardduty.types.detector_id


class GetRemainingFreeTrialDaysRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector of the GuardDuty member account.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    account_ids: "capo_guardduty.types.account_ids.AccountIds"
    """<p>A list of account identifiers of the GuardDuty member account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRemainingFreeTrialDaysRequest) -> dict:
    out: dict = {}
    import capo_guardduty.types.account_ids

    out["accountIds"] = capo_guardduty.types.account_ids.serialize_json(
        value["account_ids"]
    )
    return out


def deserialize_json(data: dict) -> GetRemainingFreeTrialDaysRequest:
    out: GetRemainingFreeTrialDaysRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_guardduty.types.account_ids

        out["account_ids"] = capo_guardduty.types.account_ids.deserialize_json(
            data["accountIds"]
        )
    else:
        raise DeserializationError(
            "GetRemainingFreeTrialDaysRequest.account_ids required"
        )
    return out
