"""Generated from Smithy shape ``com.amazonaws.guardduty#DeleteFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.string


class DeleteFilterRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector that is associated with the filter.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    filter_name: "capo_guardduty.types.string.String"
    """<p>The name of the filter that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFilterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFilterRequest:
    out: DeleteFilterRequest = {}  # type: ignore[typeddict-item]
    return out
