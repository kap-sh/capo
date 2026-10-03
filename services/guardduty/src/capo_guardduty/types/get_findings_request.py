"""Generated from Smithy shape ``com.amazonaws.guardduty#GetFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.finding_ids
    import capo_guardduty.types.sort_criteria


class GetFindingsRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The ID of the detector that specifies the GuardDuty service whose findings you want to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    finding_ids: NotRequired["capo_guardduty.types.finding_ids.FindingIds"]
    """<p>The IDs of the findings that you want to retrieve.</p>"""
    sort_criteria: NotRequired["capo_guardduty.types.sort_criteria.SortCriteria"]
    """<p>Represents the criteria used for sorting findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsRequest) -> dict:
    out: dict = {}
    if "finding_ids" in value:
        import capo_guardduty.types.finding_ids

        out["findingIds"] = capo_guardduty.types.finding_ids.serialize_json(
            value["finding_ids"]
        )
    if "sort_criteria" in value:
        import capo_guardduty.types.sort_criteria

        out["sortCriteria"] = capo_guardduty.types.sort_criteria.serialize_json(
            value["sort_criteria"]
        )
    return out


def deserialize_json(data: dict) -> GetFindingsRequest:
    out: GetFindingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("findingIds") is not None:
        import capo_guardduty.types.finding_ids

        out["finding_ids"] = capo_guardduty.types.finding_ids.deserialize_json(
            data["findingIds"]
        )
    if data.get("sortCriteria") is not None:
        import capo_guardduty.types.sort_criteria

        out["sort_criteria"] = capo_guardduty.types.sort_criteria.deserialize_json(
            data["sortCriteria"]
        )
    return out
