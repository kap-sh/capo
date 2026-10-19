"""Generated from Smithy shape ``com.amazonaws.sustainability#GetEstimatedWaterAllocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sustainability.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sustainability.types.dimension_list
    import capo_sustainability.types.filter_expression
    import capo_sustainability.types.max_results
    import capo_sustainability.types.next_token
    import capo_sustainability.types.time_granularity
    import capo_sustainability.types.time_period
    import capo_sustainability.types.water_allocation_type_list


class GetEstimatedWaterAllocationRequest(TypedDict, closed=True):
    time_period: "capo_sustainability.types.time_period.TimePeriod"
    """<p> The date range for fetching estimated water allocation. The range must include the start date of a year for that year's data to be included in the response. </p>"""
    group_by: NotRequired["capo_sustainability.types.dimension_list.DimensionList"]
    """<p>The dimensions available for grouping estimated water allocation.</p>"""
    filter_by: NotRequired[
        "capo_sustainability.types.filter_expression.FilterExpression"
    ]
    """<p> The criteria for filtering estimated water allocation. To determine which dimensions are available to be filtered by, you can first call <a>GetEstimatedWaterAllocationDimensionValues</a> </p>"""
    allocation_types: NotRequired[
        "capo_sustainability.types.water_allocation_type_list.WaterAllocationTypeList"
    ]
    """<p>The allocation types to include in the results. If absent, returns <code>TOTAL_WATER_WITHDRAWALS</code> allocation types. </p>"""
    granularity: NotRequired[
        "capo_sustainability.types.time_granularity.TimeGranularity"
    ]
    """<p>The time granularity for the results. Only <code>YEARLY_CALENDAR</code> time granularity is currently supported for water allocation. Defaults to <code>YEARLY_CALENDAR</code> if absent.</p> <p> If requesting partial time periods, data will be returned based on the smallest supported granularity. For example, requesting <code>2025-04-01T00:00:00Z</code> to <code>2026-04-01T00:00:00Z</code> with <code>YEARLY_CALENDAR</code> will return all the data for 2026 only. </p>"""
    max_results: NotRequired["capo_sustainability.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. Default is 1000.</p>"""
    next_token: NotRequired["capo_sustainability.types.next_token.NextToken"]
    """<p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEstimatedWaterAllocationRequest) -> dict:
    out: dict = {}
    import capo_sustainability.types.time_period

    out["TimePeriod"] = capo_sustainability.types.time_period.serialize_json(
        value["time_period"]
    )
    if "group_by" in value:
        import capo_sustainability.types.dimension_list

        out["GroupBy"] = capo_sustainability.types.dimension_list.serialize_json(
            value["group_by"]
        )
    if "filter_by" in value:
        import capo_sustainability.types.filter_expression

        out["FilterBy"] = capo_sustainability.types.filter_expression.serialize_json(
            value["filter_by"]
        )
    if "allocation_types" in value:
        import capo_sustainability.types.water_allocation_type_list

        out["AllocationTypes"] = (
            capo_sustainability.types.water_allocation_type_list.serialize_json(
                value["allocation_types"]
            )
        )
    if "granularity" in value:
        import capo_sustainability.types.time_granularity

        out["Granularity"] = capo_sustainability.types.time_granularity.serialize_json(
            value["granularity"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetEstimatedWaterAllocationRequest:
    out: GetEstimatedWaterAllocationRequest = {}  # type: ignore[typeddict-item]
    if data.get("TimePeriod") is not None:
        import capo_sustainability.types.time_period

        out["time_period"] = capo_sustainability.types.time_period.deserialize_json(
            data["TimePeriod"]
        )
    else:
        raise DeserializationError(
            "GetEstimatedWaterAllocationRequest.time_period required"
        )
    if data.get("GroupBy") is not None:
        import capo_sustainability.types.dimension_list

        out["group_by"] = capo_sustainability.types.dimension_list.deserialize_json(
            data["GroupBy"]
        )
    if data.get("FilterBy") is not None:
        import capo_sustainability.types.filter_expression

        out["filter_by"] = capo_sustainability.types.filter_expression.deserialize_json(
            data["FilterBy"]
        )
    if data.get("AllocationTypes") is not None:
        import capo_sustainability.types.water_allocation_type_list

        out["allocation_types"] = (
            capo_sustainability.types.water_allocation_type_list.deserialize_json(
                data["AllocationTypes"]
            )
        )
    if data.get("Granularity") is not None:
        import capo_sustainability.types.time_granularity

        out["granularity"] = (
            capo_sustainability.types.time_granularity.deserialize_json(
                data["Granularity"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
