"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#StartQueryMonitorTopContributorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_networkflowmonitor.types.destination_category
    import capo_networkflowmonitor.types.limit
    import capo_networkflowmonitor.types.monitor_metric
    import capo_networkflowmonitor.types.resource_name


class StartQueryMonitorTopContributorsInput(TypedDict, closed=True):
    monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    start_time: "datetime.datetime"
    """<p>The timestamp that is the date and time that is the beginning of the period that you want to retrieve results for with your query.</p>"""
    end_time: "datetime.datetime"
    """<p>The timestamp that is the date and time end of the period that you want to retrieve results for with your query.</p>"""
    metric_name: "capo_networkflowmonitor.types.monitor_metric.MonitorMetric"
    """<p>The metric that you want to query top contributors for. That is, you can specify a metric with this call and return the top contributor network flows, for that type of metric, for a monitor and (optionally) within a specific category, such as network flows between Availability Zones.</p>"""
    destination_category: (
        "capo_networkflowmonitor.types.destination_category.DestinationCategory"
    )
    """<p>The category that you want to query top contributors for, for a specific monitor. Destination categories can be one of the following: </p> <ul> <li> <p> <code>INTRA_AZ</code>: Top contributor network flows within a single Availability Zone</p> </li> <li> <p> <code>INTER_AZ</code>: Top contributor network flows between Availability Zones</p> </li> <li> <p> <code>INTER_REGION</code>: Top contributor network flows between Regions (to the edge of another Region)</p> </li> <li> <p> <code>INTER_VPC</code>: Top contributor network flows between VPCs</p> </li> <li> <p> <code>AMAZON_S3</code>: Top contributor network flows to or from Amazon S3</p> </li> <li> <p> <code>AMAZON_DYNAMODB</code>: Top contributor network flows to or from Amazon Dynamo DB</p> </li> <li> <p> <code>UNCLASSIFIED</code>: Top contributor network flows that do not have a bucket classification</p> </li> </ul>"""
    limit: NotRequired["capo_networkflowmonitor.types.limit.Limit"]
    """<p>The maximum number of top contributors to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQueryMonitorTopContributorsInput) -> dict:
    out: dict = {}
    import capo_networkflowmonitor._protocol.serialize

    out["startTime"] = capo_networkflowmonitor._protocol.serialize.fmt_date_time(
        value["start_time"]
    )
    import capo_networkflowmonitor._protocol.serialize

    out["endTime"] = capo_networkflowmonitor._protocol.serialize.fmt_date_time(
        value["end_time"]
    )
    import capo_networkflowmonitor.types.monitor_metric

    out["metricName"] = capo_networkflowmonitor.types.monitor_metric.serialize_json(
        value["metric_name"]
    )
    import capo_networkflowmonitor.types.destination_category

    out["destinationCategory"] = (
        capo_networkflowmonitor.types.destination_category.serialize_json(
            value["destination_category"]
        )
    )
    if "limit" in value:
        out["limit"] = value["limit"]
    return out


def deserialize_json(data: dict) -> StartQueryMonitorTopContributorsInput:
    out: StartQueryMonitorTopContributorsInput = {}  # type: ignore[typeddict-item]
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
    if data.get("metricName") is not None:
        import capo_networkflowmonitor.types.monitor_metric

        out["metric_name"] = (
            capo_networkflowmonitor.types.monitor_metric.deserialize_json(
                data["metricName"]
            )
        )
    else:
        import typing

        out["metric_name"] = typing.cast(
            "capo_networkflowmonitor.types.monitor_metric.MonitorMetric", ""
        )
    if data.get("destinationCategory") is not None:
        import capo_networkflowmonitor.types.destination_category

        out["destination_category"] = (
            capo_networkflowmonitor.types.destination_category.deserialize_json(
                data["destinationCategory"]
            )
        )
    else:
        import typing

        out["destination_category"] = typing.cast(
            "capo_networkflowmonitor.types.destination_category.DestinationCategory", ""
        )
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    return out
