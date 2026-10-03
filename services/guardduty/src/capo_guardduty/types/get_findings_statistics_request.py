"""Generated from Smithy shape ``com.amazonaws.guardduty#GetFindingsStatisticsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.finding_criteria
    import capo_guardduty.types.finding_statistic_types
    import capo_guardduty.types.group_by_type
    import capo_guardduty.types.max_results100
    import capo_guardduty.types.order_by


class GetFindingsStatisticsRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The ID of the detector whose findings statistics you want to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    finding_statistic_types: NotRequired[
        "capo_guardduty.types.finding_statistic_types.FindingStatisticTypes"
    ]
    """<p>The types of finding statistics to retrieve.</p>"""
    finding_criteria: NotRequired[
        "capo_guardduty.types.finding_criteria.FindingCriteria"
    ]
    """<p>Represents the criteria that is used for querying findings.</p>"""
    group_by: NotRequired["capo_guardduty.types.group_by_type.GroupByType"]
    """<p>Displays the findings statistics grouped by one of the listed valid values.</p>"""
    order_by: NotRequired["capo_guardduty.types.order_by.OrderBy"]
    """<p>Displays the sorted findings in the requested order. The default value of <code>orderBy</code> is <code>DESC</code>.</p> <p>You can use this parameter only with the <code>groupBy</code> parameter.</p>"""
    max_results: NotRequired["capo_guardduty.types.max_results100.MaxResults100"]
    """<p>The maximum number of results to be returned in the response. The default value is 25.</p> <p>You can use this parameter only with the <code>groupBy</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsStatisticsRequest) -> dict:
    out: dict = {}
    if "finding_statistic_types" in value:
        import capo_guardduty.types.finding_statistic_types

        out["findingStatisticTypes"] = (
            capo_guardduty.types.finding_statistic_types.serialize_json(
                value["finding_statistic_types"]
            )
        )
    if "finding_criteria" in value:
        import capo_guardduty.types.finding_criteria

        out["findingCriteria"] = capo_guardduty.types.finding_criteria.serialize_json(
            value["finding_criteria"]
        )
    if "group_by" in value:
        import capo_guardduty.types.group_by_type

        out["groupBy"] = capo_guardduty.types.group_by_type.serialize_json(
            value["group_by"]
        )
    if "order_by" in value:
        import capo_guardduty.types.order_by

        out["orderBy"] = capo_guardduty.types.order_by.serialize_json(value["order_by"])
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> GetFindingsStatisticsRequest:
    out: GetFindingsStatisticsRequest = {}  # type: ignore[typeddict-item]
    if data.get("findingStatisticTypes") is not None:
        import capo_guardduty.types.finding_statistic_types

        out["finding_statistic_types"] = (
            capo_guardduty.types.finding_statistic_types.deserialize_json(
                data["findingStatisticTypes"]
            )
        )
    if data.get("findingCriteria") is not None:
        import capo_guardduty.types.finding_criteria

        out["finding_criteria"] = (
            capo_guardduty.types.finding_criteria.deserialize_json(
                data["findingCriteria"]
            )
        )
    if data.get("groupBy") is not None:
        import capo_guardduty.types.group_by_type

        out["group_by"] = capo_guardduty.types.group_by_type.deserialize_json(
            data["groupBy"]
        )
    if data.get("orderBy") is not None:
        import capo_guardduty.types.order_by

        out["order_by"] = capo_guardduty.types.order_by.deserialize_json(
            data["orderBy"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
