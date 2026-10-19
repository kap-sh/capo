"""Generated from Smithy shape ``com.amazonaws.sustainability#GetEstimatedWaterAllocationDimensionValuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sustainability.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sustainability.types.dimension_list
    import capo_sustainability.types.max_results
    import capo_sustainability.types.next_token
    import capo_sustainability.types.time_period


class GetEstimatedWaterAllocationDimensionValuesRequest(TypedDict, closed=True):
    time_period: "capo_sustainability.types.time_period.TimePeriod"
    """<p> The date range for fetching the dimension values. The range must include the start date of a year for that year's data to be included in the response. </p>"""
    dimensions: "capo_sustainability.types.dimension_list.DimensionList"
    """<p>The dimensions available for grouping estimated water allocation.</p>"""
    max_results: NotRequired["capo_sustainability.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. Default is 1000.</p>"""
    next_token: NotRequired["capo_sustainability.types.next_token.NextToken"]
    """<p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEstimatedWaterAllocationDimensionValuesRequest) -> dict:
    out: dict = {}
    import capo_sustainability.types.time_period

    out["TimePeriod"] = capo_sustainability.types.time_period.serialize_json(
        value["time_period"]
    )
    import capo_sustainability.types.dimension_list

    out["Dimensions"] = capo_sustainability.types.dimension_list.serialize_json(
        value["dimensions"]
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetEstimatedWaterAllocationDimensionValuesRequest:
    out: GetEstimatedWaterAllocationDimensionValuesRequest = {}  # type: ignore[typeddict-item]
    if data.get("TimePeriod") is not None:
        import capo_sustainability.types.time_period

        out["time_period"] = capo_sustainability.types.time_period.deserialize_json(
            data["TimePeriod"]
        )
    else:
        raise DeserializationError(
            "GetEstimatedWaterAllocationDimensionValuesRequest.time_period required"
        )
    if data.get("Dimensions") is not None:
        import capo_sustainability.types.dimension_list

        out["dimensions"] = capo_sustainability.types.dimension_list.deserialize_json(
            data["Dimensions"]
        )
    else:
        raise DeserializationError(
            "GetEstimatedWaterAllocationDimensionValuesRequest.dimensions required"
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
