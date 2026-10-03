"""Generated from Smithy shape ``com.amazonaws.guardduty#DeleteIPSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.string


class DeleteIPSetRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector associated with the IPSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    ip_set_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique ID of the IPSet to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIPSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIPSetRequest:
    out: DeleteIPSetRequest = {}  # type: ignore[typeddict-item]
    return out
