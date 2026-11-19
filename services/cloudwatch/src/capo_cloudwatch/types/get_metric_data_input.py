"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetMetricDataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.get_metric_data_max_datapoints
    import capo_cloudwatch.types.label_options
    import capo_cloudwatch.types.metric_data_queries
    import capo_cloudwatch.types.next_token
    import capo_cloudwatch.types.scan_by
    import capo_cloudwatch.types.timestamp


class GetMetricDataInput(TypedDict, closed=True):
    metric_data_queries: NotRequired[
        "capo_cloudwatch.types.metric_data_queries.MetricDataQueries"
    ]
    """<p>The metric queries to be returned. A single <code>GetMetricData</code> call can include as many as 500 <code>MetricDataQuery</code> structures. Each of these structures can specify either a metric to retrieve, a Metrics Insights query, or a math expression to perform on retrieved data. </p>"""
    start_time: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The time stamp indicating the earliest data to be returned.</p> <p>The value specified is inclusive; results include data points with the specified time stamp. </p> <p>CloudWatch rounds the specified time stamp as follows:</p> <ul> <li> <p>Start time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00.</p> </li> <li> <p>Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00.</p> </li> <li> <p>Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00.</p> </li> </ul> <p>If you set <code>Period</code> to 5, 10, 20, or 30, the start time of your request is rounded down to the nearest time that corresponds to even 5-, 10-, 20-, or 30-second divisions of a minute. For example, if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of your request is rounded down and you receive data from 01:05:10 to 01:05:20. If you make a query at 15:07:17 for the previous 5 minutes of data, using a period of 5 seconds, you receive data timestamped between 15:02:15 and 15:07:15. </p> <p>For better performance, specify <code>StartTime</code> and <code>EndTime</code> values that align with the value of the metric's <code>Period</code> and sync up with the beginning and end of an hour. For example, if the <code>Period</code> of a metric is 5 minutes, specifying 12:05 or 12:30 as <code>StartTime</code> can get a faster response from CloudWatch than setting 12:07 or 12:29 as the <code>StartTime</code>.</p>"""
    end_time: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The time stamp indicating the latest data to be returned.</p> <p>The value specified is exclusive; results include data points up to the specified time stamp.</p> <p>For better performance, specify <code>StartTime</code> and <code>EndTime</code> values that align with the value of the metric's <code>Period</code> and sync up with the beginning and end of an hour. For example, if the <code>Period</code> of a metric is 5 minutes, specifying 12:05 or 12:30 as <code>EndTime</code> can get a faster response from CloudWatch than setting 12:07 or 12:29 as the <code>EndTime</code>.</p>"""
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p>Include this value, if it was returned by the previous <code>GetMetricData</code> operation, to get the next set of data points.</p>"""
    scan_by: NotRequired["capo_cloudwatch.types.scan_by.ScanBy"]
    """<p>The order in which data points should be returned. <code>TimestampDescending</code> returns the newest data first and paginates when the <code>MaxDatapoints</code> limit is reached. <code>TimestampAscending</code> returns the oldest data first and paginates when the <code>MaxDatapoints</code> limit is reached.</p> <p>If you omit this parameter, the default of <code>TimestampDescending</code> is used.</p>"""
    max_datapoints: NotRequired[
        "capo_cloudwatch.types.get_metric_data_max_datapoints.GetMetricDataMaxDatapoints"
    ]
    """<p>The maximum number of data points the request should return before paginating. If you omit this, the default of 100,800 is used.</p>"""
    label_options: NotRequired["capo_cloudwatch.types.label_options.LabelOptions"]
    """<p>This structure includes the <code>Timezone</code> parameter, which you can use to specify your time zone so that the labels of returned data display the correct time for your time zone. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetMetricDataInput) -> dict:
    out: dict = {}
    if "metric_data_queries" in value:
        import capo_cloudwatch.types.metric_data_queries

        out["MetricDataQueries"] = (
            capo_cloudwatch.types.metric_data_queries.serialize_aws_json_1_0(
                value["metric_data_queries"]
            )
        )
    if "start_time" in value:
        import capo_cloudwatch.types.timestamp

        out["StartTime"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_cloudwatch.types.timestamp

        out["EndTime"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["end_time"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "scan_by" in value:
        import capo_cloudwatch.types.scan_by

        out["ScanBy"] = capo_cloudwatch.types.scan_by.serialize_aws_json_1_0(
            value["scan_by"]
        )
    if "max_datapoints" in value:
        out["MaxDatapoints"] = value["max_datapoints"]
    if "label_options" in value:
        import capo_cloudwatch.types.label_options

        out["LabelOptions"] = (
            capo_cloudwatch.types.label_options.serialize_aws_json_1_0(
                value["label_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetMetricDataInput:
    out: GetMetricDataInput = {}  # type: ignore[typeddict-item]
    if data.get("MetricDataQueries") is not None:
        import capo_cloudwatch.types.metric_data_queries

        out["metric_data_queries"] = (
            capo_cloudwatch.types.metric_data_queries.deserialize_aws_json_1_0(
                data["MetricDataQueries"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_cloudwatch.types.timestamp

        out["start_time"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_cloudwatch.types.timestamp

        out["end_time"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["EndTime"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ScanBy") is not None:
        import capo_cloudwatch.types.scan_by

        out["scan_by"] = capo_cloudwatch.types.scan_by.deserialize_aws_json_1_0(
            data["ScanBy"]
        )
    if data.get("MaxDatapoints") is not None:
        out["max_datapoints"] = data["MaxDatapoints"]
    if data.get("LabelOptions") is not None:
        import capo_cloudwatch.types.label_options

        out["label_options"] = (
            capo_cloudwatch.types.label_options.deserialize_aws_json_1_0(
                data["LabelOptions"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetMetricDataInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_data_queries" in value:
        import capo_cloudwatch.types.metric_data_queries

        capo_cloudwatch.types.metric_data_queries.serialize_query(
            value["metric_data_queries"], pairs, f"{key_prefix}MetricDataQueries"
        )
    if "start_time" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "end_time" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["end_time"], pairs, f"{key_prefix}EndTime"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "scan_by" in value:
        import capo_cloudwatch.types.scan_by

        capo_cloudwatch.types.scan_by.serialize_query(
            value["scan_by"], pairs, f"{key_prefix}ScanBy"
        )
    if "max_datapoints" in value:
        pairs.append((f"{key_prefix}MaxDatapoints", str(value["max_datapoints"])))
    if "label_options" in value:
        import capo_cloudwatch.types.label_options

        capo_cloudwatch.types.label_options.serialize_query(
            value["label_options"], pairs, f"{key_prefix}LabelOptions"
        )


def deserialize_query(el: Element) -> GetMetricDataInput:
    out: GetMetricDataInput = {}  # type: ignore[typeddict-item]
    child_metric_data_queries = el.find("MetricDataQueries")
    if child_metric_data_queries is not None:
        import capo_cloudwatch.types.metric_data_queries

        out["metric_data_queries"] = (
            capo_cloudwatch.types.metric_data_queries.deserialize_query(
                child_metric_data_queries
            )
        )
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_cloudwatch.types.timestamp

        out["start_time"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_cloudwatch.types.timestamp

        out["end_time"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_end_time
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_scan_by = el.find("ScanBy")
    if child_scan_by is not None:
        import capo_cloudwatch.types.scan_by

        out["scan_by"] = capo_cloudwatch.types.scan_by.deserialize_query(child_scan_by)
    child_max_datapoints = el.find("MaxDatapoints")
    if child_max_datapoints is not None:
        out["max_datapoints"] = int(child_max_datapoints.text or "")
    child_label_options = el.find("LabelOptions")
    if child_label_options is not None:
        import capo_cloudwatch.types.label_options

        out["label_options"] = capo_cloudwatch.types.label_options.deserialize_query(
            child_label_options
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetMetricDataInput) -> dict:
    out: dict = {}
    if "metric_data_queries" in value:
        import capo_cloudwatch.types.metric_data_queries

        out["MetricDataQueries"] = (
            capo_cloudwatch.types.metric_data_queries.serialize_cbor(
                value["metric_data_queries"]
            )
        )
    if "start_time" in value:
        import capo_cloudwatch.types.timestamp

        out["StartTime"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_cloudwatch.types.timestamp

        out["EndTime"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["end_time"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "scan_by" in value:
        import capo_cloudwatch.types.scan_by

        out["ScanBy"] = capo_cloudwatch.types.scan_by.serialize_cbor(value["scan_by"])
    if "max_datapoints" in value:
        out["MaxDatapoints"] = value["max_datapoints"]
    if "label_options" in value:
        import capo_cloudwatch.types.label_options

        out["LabelOptions"] = capo_cloudwatch.types.label_options.serialize_cbor(
            value["label_options"]
        )
    return out


def deserialize_cbor(data: dict) -> GetMetricDataInput:
    out: GetMetricDataInput = {}  # type: ignore[typeddict-item]
    if data.get("MetricDataQueries") is not None:
        import capo_cloudwatch.types.metric_data_queries

        out["metric_data_queries"] = (
            capo_cloudwatch.types.metric_data_queries.deserialize_cbor(
                data["MetricDataQueries"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_cloudwatch.types.timestamp

        out["start_time"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_cloudwatch.types.timestamp

        out["end_time"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["EndTime"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ScanBy") is not None:
        import capo_cloudwatch.types.scan_by

        out["scan_by"] = capo_cloudwatch.types.scan_by.deserialize_cbor(data["ScanBy"])
    if data.get("MaxDatapoints") is not None:
        out["max_datapoints"] = data["MaxDatapoints"]
    if data.get("LabelOptions") is not None:
        import capo_cloudwatch.types.label_options

        out["label_options"] = capo_cloudwatch.types.label_options.deserialize_cbor(
            data["LabelOptions"]
        )
    return out
