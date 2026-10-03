"""Generated from Smithy shape ``com.amazonaws.guardduty#GetCoverageStatisticsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.coverage_filter_criteria
    import capo_guardduty.types.coverage_statistics_type_list
    import capo_guardduty.types.detector_id


class GetCoverageStatisticsRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the GuardDuty detector.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    filter_criteria: NotRequired[
        "capo_guardduty.types.coverage_filter_criteria.CoverageFilterCriteria"
    ]
    """<p>Represents the criteria used to filter the coverage statistics.</p>"""
    statistics_type: NotRequired[
        "capo_guardduty.types.coverage_statistics_type_list.CoverageStatisticsTypeList"
    ]
    """<p>Represents the statistics type used to aggregate the coverage details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCoverageStatisticsRequest) -> dict:
    out: dict = {}
    if "filter_criteria" in value:
        import capo_guardduty.types.coverage_filter_criteria

        out["filterCriteria"] = (
            capo_guardduty.types.coverage_filter_criteria.serialize_json(
                value["filter_criteria"]
            )
        )
    if "statistics_type" in value:
        import capo_guardduty.types.coverage_statistics_type_list

        out["statisticsType"] = (
            capo_guardduty.types.coverage_statistics_type_list.serialize_json(
                value["statistics_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCoverageStatisticsRequest:
    out: GetCoverageStatisticsRequest = {}  # type: ignore[typeddict-item]
    if data.get("filterCriteria") is not None:
        import capo_guardduty.types.coverage_filter_criteria

        out["filter_criteria"] = (
            capo_guardduty.types.coverage_filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    if data.get("statisticsType") is not None:
        import capo_guardduty.types.coverage_statistics_type_list

        out["statistics_type"] = (
            capo_guardduty.types.coverage_statistics_type_list.deserialize_json(
                data["statisticsType"]
            )
        )
    return out
