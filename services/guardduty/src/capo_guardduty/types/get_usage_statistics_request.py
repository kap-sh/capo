"""Generated from Smithy shape ``com.amazonaws.guardduty#GetUsageStatisticsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.max_results
    import capo_guardduty.types.string
    import capo_guardduty.types.usage_criteria
    import capo_guardduty.types.usage_statistic_type


class GetUsageStatisticsRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The ID of the detector that specifies the GuardDuty service whose usage statistics you want to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    usage_statistic_type: NotRequired[
        "capo_guardduty.types.usage_statistic_type.UsageStatisticType"
    ]
    """<p>The type of usage statistics to retrieve.</p>"""
    usage_criteria: NotRequired["capo_guardduty.types.usage_criteria.UsageCriteria"]
    """<p>Represents the criteria used for querying usage.</p>"""
    unit: NotRequired["capo_guardduty.types.string.String"]
    """<p>The currency unit you would like to view your usage statistics in. Current valid values are USD.</p>"""
    max_results: NotRequired["capo_guardduty.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUsageStatisticsRequest) -> dict:
    out: dict = {}
    if "usage_statistic_type" in value:
        import capo_guardduty.types.usage_statistic_type

        out["usageStatisticsType"] = (
            capo_guardduty.types.usage_statistic_type.serialize_json(
                value["usage_statistic_type"]
            )
        )
    if "usage_criteria" in value:
        import capo_guardduty.types.usage_criteria

        out["usageCriteria"] = capo_guardduty.types.usage_criteria.serialize_json(
            value["usage_criteria"]
        )
    if "unit" in value:
        out["unit"] = value["unit"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetUsageStatisticsRequest:
    out: GetUsageStatisticsRequest = {}  # type: ignore[typeddict-item]
    if data.get("usageStatisticsType") is not None:
        import capo_guardduty.types.usage_statistic_type

        out["usage_statistic_type"] = (
            capo_guardduty.types.usage_statistic_type.deserialize_json(
                data["usageStatisticsType"]
            )
        )
    if data.get("usageCriteria") is not None:
        import capo_guardduty.types.usage_criteria

        out["usage_criteria"] = capo_guardduty.types.usage_criteria.deserialize_json(
            data["usageCriteria"]
        )
    if data.get("unit") is not None:
        out["unit"] = data["unit"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
