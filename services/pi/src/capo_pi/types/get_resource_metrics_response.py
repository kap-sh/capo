"""Generated from Smithy shape ``com.amazonaws.pi#GetResourceMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.iso_timestamp
    import capo_pi.types.metric_key_data_points_list
    import capo_pi.types.next_token
    import capo_pi.types.string


class GetResourceMetricsResponse(TypedDict, closed=True):
    aligned_start_time: NotRequired["capo_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The start time for the returned metrics, after alignment to a granular boundary (as specified by <code>PeriodInSeconds</code>). <code>AlignedStartTime</code> will be less than or equal to the value of the user-specified <code>StartTime</code>.</p>"""
    aligned_end_time: NotRequired["capo_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The end time for the returned metrics, after alignment to a granular boundary (as specified by <code>PeriodInSeconds</code>). <code>AlignedEndTime</code> will be greater than or equal to the value of the user-specified <code>Endtime</code>.</p>"""
    identifier: NotRequired["capo_pi.types.string.String"]
    """<p>An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as <i>ResourceID</i>. When you call <code>DescribeDBInstances</code>, the identifier is returned as <code>DbiResourceId</code>.</p>"""
    metric_list: NotRequired[
        "capo_pi.types.metric_key_data_points_list.MetricKeyDataPointsList"
    ]
    """<p>An array of metric results, where each array element contains all of the data points for a particular dimension.</p>"""
    next_token: NotRequired["capo_pi.types.next_token.NextToken"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxRecords</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourceMetricsResponse) -> dict:
    out: dict = {}
    if "aligned_start_time" in value:
        import capo_pi.types.iso_timestamp

        out["AlignedStartTime"] = capo_pi.types.iso_timestamp.serialize_aws_json_1_1(
            value["aligned_start_time"]
        )
    if "aligned_end_time" in value:
        import capo_pi.types.iso_timestamp

        out["AlignedEndTime"] = capo_pi.types.iso_timestamp.serialize_aws_json_1_1(
            value["aligned_end_time"]
        )
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "metric_list" in value:
        import capo_pi.types.metric_key_data_points_list

        out["MetricList"] = (
            capo_pi.types.metric_key_data_points_list.serialize_aws_json_1_1(
                value["metric_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourceMetricsResponse:
    out: GetResourceMetricsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AlignedStartTime") is not None:
        import capo_pi.types.iso_timestamp

        out["aligned_start_time"] = (
            capo_pi.types.iso_timestamp.deserialize_aws_json_1_1(
                data["AlignedStartTime"]
            )
        )
    if data.get("AlignedEndTime") is not None:
        import capo_pi.types.iso_timestamp

        out["aligned_end_time"] = capo_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["AlignedEndTime"]
        )
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    if data.get("MetricList") is not None:
        import capo_pi.types.metric_key_data_points_list

        out["metric_list"] = (
            capo_pi.types.metric_key_data_points_list.deserialize_aws_json_1_1(
                data["MetricList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetResourceMetricsResponse) -> dict:
    out: dict = {}
    if "aligned_start_time" in value:
        import capo_pi.types.iso_timestamp

        out["AlignedStartTime"] = capo_pi.types.iso_timestamp.serialize_cbor(
            value["aligned_start_time"]
        )
    if "aligned_end_time" in value:
        import capo_pi.types.iso_timestamp

        out["AlignedEndTime"] = capo_pi.types.iso_timestamp.serialize_cbor(
            value["aligned_end_time"]
        )
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "metric_list" in value:
        import capo_pi.types.metric_key_data_points_list

        out["MetricList"] = capo_pi.types.metric_key_data_points_list.serialize_cbor(
            value["metric_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> GetResourceMetricsResponse:
    out: GetResourceMetricsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AlignedStartTime") is not None:
        import capo_pi.types.iso_timestamp

        out["aligned_start_time"] = capo_pi.types.iso_timestamp.deserialize_cbor(
            data["AlignedStartTime"]
        )
    if data.get("AlignedEndTime") is not None:
        import capo_pi.types.iso_timestamp

        out["aligned_end_time"] = capo_pi.types.iso_timestamp.deserialize_cbor(
            data["AlignedEndTime"]
        )
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    if data.get("MetricList") is not None:
        import capo_pi.types.metric_key_data_points_list

        out["metric_list"] = capo_pi.types.metric_key_data_points_list.deserialize_cbor(
            data["MetricList"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
