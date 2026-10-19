"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListInsightsDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.date
    import capo_cloudtrail.types.list_insights_data_dimensions
    import capo_cloudtrail.types.list_insights_data_max_results_count
    import capo_cloudtrail.types.list_insights_data_type
    import capo_cloudtrail.types.pagination_token
    import capo_cloudtrail.types.resource_arn


class ListInsightsDataRequest(TypedDict, closed=True):
    insight_source: "capo_cloudtrail.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name(ARN) of the trail for which you want to retrieve Insights events.</p>"""
    data_type: "capo_cloudtrail.types.list_insights_data_type.ListInsightsDataType"
    """<p>Specifies the category of events returned. To fetch Insights events, specify <code>InsightsEvents</code> as the value of <code>DataType</code> </p>"""
    dimensions: NotRequired[
        "capo_cloudtrail.types.list_insights_data_dimensions.ListInsightsDataDimensions"
    ]
    """<p>Contains a map of dimensions. Currently the map can contain only one item.</p>"""
    start_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>Specifies that only events that occur after or at the specified time are returned. If the specified start time is after the specified end time, an error is returned.</p>"""
    end_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>Specifies that only events that occur before or at the specified time are returned. If the specified end time is before the specified start time, an error is returned.</p>"""
    max_results: NotRequired[
        "capo_cloudtrail.types.list_insights_data_max_results_count.ListInsightsDataMaxResultsCount"
    ]
    """<p>The number of events to return. Possible values are 1 through 50. The default is 50.</p>"""
    next_token: NotRequired["capo_cloudtrail.types.pagination_token.PaginationToken"]
    """<p>The token to use to get the next page of results after a previous API call. This token must be passed in with the same parameters that were specified in the original call. For example, if the original call specified a EventName as a dimension with <code>PutObject</code> as a value, the call with NextToken should include those same parameters. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInsightsDataRequest) -> dict:
    out: dict = {}
    out["InsightSource"] = value["insight_source"]
    import capo_cloudtrail.types.list_insights_data_type

    out["DataType"] = (
        capo_cloudtrail.types.list_insights_data_type.serialize_aws_json_1_1(
            value["data_type"]
        )
    )
    if "dimensions" in value:
        import capo_cloudtrail.types.list_insights_data_dimensions

        out["Dimensions"] = (
            capo_cloudtrail.types.list_insights_data_dimensions.serialize_aws_json_1_1(
                value["dimensions"]
            )
        )
    if "start_time" in value:
        import capo_cloudtrail.types.date

        out["StartTime"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_cloudtrail.types.date

        out["EndTime"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInsightsDataRequest:
    out: ListInsightsDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("InsightSource") is not None:
        out["insight_source"] = data["InsightSource"]
    else:
        out["insight_source"] = ""
    if data.get("DataType") is not None:
        import capo_cloudtrail.types.list_insights_data_type

        out["data_type"] = (
            capo_cloudtrail.types.list_insights_data_type.deserialize_aws_json_1_1(
                data["DataType"]
            )
        )
    else:
        import typing

        out["data_type"] = typing.cast(
            "capo_cloudtrail.types.list_insights_data_type.ListInsightsDataType", ""
        )
    if data.get("Dimensions") is not None:
        import capo_cloudtrail.types.list_insights_data_dimensions

        out["dimensions"] = (
            capo_cloudtrail.types.list_insights_data_dimensions.deserialize_aws_json_1_1(
                data["Dimensions"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_cloudtrail.types.date

        out["start_time"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_cloudtrail.types.date

        out["end_time"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
