"""Generated from Smithy shape ``com.amazonaws.guardduty#ArchiveFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.finding_ids


class ArchiveFindingsRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The ID of the detector that specifies the GuardDuty service whose findings you want to archive.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    finding_ids: NotRequired["capo_guardduty.types.finding_ids.FindingIds"]
    """<p>The IDs of the findings that you want to archive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveFindingsRequest) -> dict:
    out: dict = {}
    if "finding_ids" in value:
        import capo_guardduty.types.finding_ids

        out["findingIds"] = capo_guardduty.types.finding_ids.serialize_json(
            value["finding_ids"]
        )
    return out


def deserialize_json(data: dict) -> ArchiveFindingsRequest:
    out: ArchiveFindingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("findingIds") is not None:
        import capo_guardduty.types.finding_ids

        out["finding_ids"] = capo_guardduty.types.finding_ids.deserialize_json(
            data["findingIds"]
        )
    return out
