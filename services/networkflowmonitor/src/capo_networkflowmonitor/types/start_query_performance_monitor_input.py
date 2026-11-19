"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#StartQueryPerformanceMonitorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_networkflowmonitor.types.filter_parameters
    import capo_networkflowmonitor.types.performance_monitor_query_type
    import capo_networkflowmonitor.types.query_limit
    import capo_networkflowmonitor.types.resource_name


class StartQueryPerformanceMonitorInput(TypedDict, closed=True):
    monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the performance monitor.</p>"""
    start_time: "datetime.datetime"
    """<p>The timestamp that is the date and time that is the beginning of the period that you want to retrieve results for with your query.</p>"""
    end_time: "datetime.datetime"
    """<p>The timestamp that is the date and time end of the period that you want to retrieve results for with your query.</p>"""
    query_type: "capo_networkflowmonitor.types.performance_monitor_query_type.PerformanceMonitorQueryType"
    """<p>The type of query that you want to create. Specify <code>TOP_PATHS</code> to return the top paths for the performance monitor.</p>"""
    filter_parameters: NotRequired[
        "capo_networkflowmonitor.types.filter_parameters.FilterParameters"
    ]
    """<p>The filters for the query, to return a subset of the top paths. For a <code>TOP_PATHS</code> query, you can filter on the following fields:</p> <ul> <li> <p> <code>local_az_id</code>: The Availability Zone ID of the local end of a path</p> </li> <li> <p> <code>remote_az_id</code>: The Availability Zone ID of the remote end of a path</p> </li> <li> <p> <code>impact_level</code>: The impact level of a path</p> </li> </ul> <p>When you filter on <code>impact_level</code>, Network Flow Monitor compares the filter with the most severe impact level for the path over the time period of the query, and the traffic and round-trip time that Network Flow Monitor returns for each path still cover the full time period. Paths that have no impact data don't match an <code>impact_level</code> filter, including a <code>NOT_EQUALS</code> filter. Network Flow Monitor doesn't filter the subnet pairs within a path by impact level.</p>"""
    limit: NotRequired["capo_networkflowmonitor.types.query_limit.QueryLimit"]
    """<p>The maximum number of top paths that you want the query to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQueryPerformanceMonitorInput) -> dict:
    out: dict = {}
    import capo_networkflowmonitor._protocol.serialize

    out["startTime"] = capo_networkflowmonitor._protocol.serialize.fmt_date_time(
        value["start_time"]
    )
    import capo_networkflowmonitor._protocol.serialize

    out["endTime"] = capo_networkflowmonitor._protocol.serialize.fmt_date_time(
        value["end_time"]
    )
    import capo_networkflowmonitor.types.performance_monitor_query_type

    out["queryType"] = (
        capo_networkflowmonitor.types.performance_monitor_query_type.serialize_json(
            value["query_type"]
        )
    )
    if "filter_parameters" in value:
        import capo_networkflowmonitor.types.filter_parameters

        out["filterParameters"] = (
            capo_networkflowmonitor.types.filter_parameters.serialize_json(
                value["filter_parameters"]
            )
        )
    if "limit" in value:
        out["limit"] = value["limit"]
    return out


def deserialize_json(data: dict) -> StartQueryPerformanceMonitorInput:
    out: StartQueryPerformanceMonitorInput = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import datetime

        out["start_time"] = datetime.datetime.fromisoformat(
            data["startTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import datetime

        out["end_time"] = datetime.datetime.fromisoformat(
            data["endTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("queryType") is not None:
        import capo_networkflowmonitor.types.performance_monitor_query_type

        out["query_type"] = (
            capo_networkflowmonitor.types.performance_monitor_query_type.deserialize_json(
                data["queryType"]
            )
        )
    else:
        import typing

        out["query_type"] = typing.cast(
            "capo_networkflowmonitor.types.performance_monitor_query_type.PerformanceMonitorQueryType",
            "",
        )
    if data.get("filterParameters") is not None:
        import capo_networkflowmonitor.types.filter_parameters

        out["filter_parameters"] = (
            capo_networkflowmonitor.types.filter_parameters.deserialize_json(
                data["filterParameters"]
            )
        )
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    return out
