"""Generated from Smithy shape ``com.amazonaws.pi#DescribeDimensionKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pi.types.additional_metrics_list
    import capo_pi.types.dimension_group
    import capo_pi.types.identifier_string
    import capo_pi.types.integer
    import capo_pi.types.iso_timestamp
    import capo_pi.types.max_results
    import capo_pi.types.metric_query_filter_map
    import capo_pi.types.next_token
    import capo_pi.types.request_string
    import capo_pi.types.service_type


class DescribeDimensionKeysRequest(TypedDict, closed=True):
    service_type: "capo_pi.types.service_type.ServiceType"
    """<p>The Amazon Web Services service for which Performance Insights will return metrics. Valid values are as follows:</p> <ul> <li> <p> <code>RDS</code> </p> </li> <li> <p> <code>DOCDB</code> </p> </li> </ul>"""
    identifier: "capo_pi.types.identifier_string.IdentifierString"
    """<p>An immutable, Amazon Web Services Region-unique identifier for a data source. Performance Insights gathers metrics from this data source.</p> <p>To use an Amazon RDS instance as a data source, you specify its <code>DbiResourceId</code> value. For example, specify <code>db-FAIHNTYBKTGAUSUZQYPDS2GW4A</code>. </p>"""
    start_time: "capo_pi.types.iso_timestamp.ISOTimestamp"
    """<p>The date and time specifying the beginning of the requested time series data. You must specify a <code>StartTime</code> within the past 7 days. The value specified is <i>inclusive</i>, which means that data points equal to or greater than <code>StartTime</code> are returned. </p> <p>The value for <code>StartTime</code> must be earlier than the value for <code>EndTime</code>. </p>"""
    end_time: "capo_pi.types.iso_timestamp.ISOTimestamp"
    """<p>The date and time specifying the end of the requested time series data. The value specified is <i>exclusive</i>, which means that data points less than (but not equal to) <code>EndTime</code> are returned.</p> <p>The value for <code>EndTime</code> must be later than the value for <code>StartTime</code>.</p>"""
    metric: "capo_pi.types.request_string.RequestString"
    """<p>The name of a Performance Insights metric to be measured.</p> <p>Valid values for <code>Metric</code> are:</p> <ul> <li> <p> <code>db.load.avg</code> - A scaled representation of the number of active sessions for the database engine. </p> </li> <li> <p> <code>db.sampledload.avg</code> - The raw number of active sessions for the database engine. </p> </li> </ul> <p>If the number of active sessions is less than an internal Performance Insights threshold, <code>db.load.avg</code> and <code>db.sampledload.avg</code> are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with <code>db.load.avg</code> showing the scaled values, <code>db.sampledload.avg</code> showing the raw values, and <code>db.sampledload.avg</code> less than <code>db.load.avg</code>. For most use cases, you can query <code>db.load.avg</code> only. </p>"""
    period_in_seconds: NotRequired["capo_pi.types.integer.Integer"]
    """<p>The granularity, in seconds, of the data points returned from Performance Insights. A period can be as short as one second, or as long as one day (86400 seconds). Valid values are: </p> <ul> <li> <p> <code>1</code> (one second)</p> </li> <li> <p> <code>60</code> (one minute)</p> </li> <li> <p> <code>300</code> (five minutes)</p> </li> <li> <p> <code>3600</code> (one hour)</p> </li> <li> <p> <code>86400</code> (twenty-four hours)</p> </li> </ul> <p>If you don't specify <code>PeriodInSeconds</code>, then Performance Insights chooses a value for you, with a goal of returning roughly 100-200 data points in the response. </p>"""
    group_by: "capo_pi.types.dimension_group.DimensionGroup"
    """<p>A specification for how to aggregate the data points from a query result. You must specify a valid dimension group. Performance Insights returns all dimensions within this group, unless you provide the names of specific dimensions within this group. You can also request that Performance Insights return a limited number of values for a dimension. </p>"""
    additional_metrics: NotRequired[
        "capo_pi.types.additional_metrics_list.AdditionalMetricsList"
    ]
    """<p>Additional metrics for the top <code>N</code> dimension keys. If the specified dimension group in the <code>GroupBy</code> parameter is <code>db.sql_tokenized</code>, you can specify per-SQL metrics to get the values for the top <code>N</code> SQL digests. The response syntax is as follows: <code>"AdditionalMetrics" : { "<i>string</i>" : "<i>string</i>" }</code>.</p> <p>The only supported statistic function is <code>.avg</code>.</p>"""
    partition_by: NotRequired["capo_pi.types.dimension_group.DimensionGroup"]
    """<p>For each dimension specified in <code>GroupBy</code>, specify a secondary dimension to further subdivide the partition keys in the response. </p>"""
    filter: NotRequired["capo_pi.types.metric_query_filter_map.MetricQueryFilterMap"]
    """<p>One or more filters to apply in the request. Restrictions:</p> <ul> <li> <p>Any number of filters by the same dimension, as specified in the <code>GroupBy</code> or <code>Partition</code> parameters.</p> </li> <li> <p>A single filter for any other dimension in this dimension group.</p> </li> </ul> <note> <p>The <code>db.sql.db_id</code> filter isn't available for RDS for SQL Server DB instances.</p> </note>"""
    max_results: NotRequired["capo_pi.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response. If more items exist than the specified <code>MaxRecords</code> value, a pagination token is included in the response so that the remaining results can be retrieved. </p>"""
    next_token: NotRequired["capo_pi.types.next_token.NextToken"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDimensionKeysRequest) -> dict:
    out: dict = {}
    import capo_pi.types.service_type

    out["ServiceType"] = capo_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["Identifier"] = value["identifier"]
    import capo_pi.types.iso_timestamp

    out["StartTime"] = capo_pi.types.iso_timestamp.serialize_aws_json_1_1(
        value["start_time"]
    )
    import capo_pi.types.iso_timestamp

    out["EndTime"] = capo_pi.types.iso_timestamp.serialize_aws_json_1_1(
        value["end_time"]
    )
    out["Metric"] = value["metric"]
    if "period_in_seconds" in value:
        out["PeriodInSeconds"] = value["period_in_seconds"]
    import capo_pi.types.dimension_group

    out["GroupBy"] = capo_pi.types.dimension_group.serialize_aws_json_1_1(
        value["group_by"]
    )
    if "additional_metrics" in value:
        import capo_pi.types.additional_metrics_list

        out["AdditionalMetrics"] = (
            capo_pi.types.additional_metrics_list.serialize_aws_json_1_1(
                value["additional_metrics"]
            )
        )
    if "partition_by" in value:
        import capo_pi.types.dimension_group

        out["PartitionBy"] = capo_pi.types.dimension_group.serialize_aws_json_1_1(
            value["partition_by"]
        )
    if "filter" in value:
        import capo_pi.types.metric_query_filter_map

        out["Filter"] = capo_pi.types.metric_query_filter_map.serialize_aws_json_1_1(
            value["filter"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDimensionKeysRequest:
    out: DescribeDimensionKeysRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceType") is not None:
        import capo_pi.types.service_type

        out["service_type"] = capo_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    else:
        raise DeserializationError("DescribeDimensionKeysRequest.service_type required")
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("DescribeDimensionKeysRequest.identifier required")
    if data.get("StartTime") is not None:
        import capo_pi.types.iso_timestamp

        out["start_time"] = capo_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    else:
        raise DeserializationError("DescribeDimensionKeysRequest.start_time required")
    if data.get("EndTime") is not None:
        import capo_pi.types.iso_timestamp

        out["end_time"] = capo_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    else:
        raise DeserializationError("DescribeDimensionKeysRequest.end_time required")
    if data.get("Metric") is not None:
        out["metric"] = data["Metric"]
    else:
        raise DeserializationError("DescribeDimensionKeysRequest.metric required")
    if data.get("PeriodInSeconds") is not None:
        out["period_in_seconds"] = data["PeriodInSeconds"]
    if data.get("GroupBy") is not None:
        import capo_pi.types.dimension_group

        out["group_by"] = capo_pi.types.dimension_group.deserialize_aws_json_1_1(
            data["GroupBy"]
        )
    else:
        raise DeserializationError("DescribeDimensionKeysRequest.group_by required")
    if data.get("AdditionalMetrics") is not None:
        import capo_pi.types.additional_metrics_list

        out["additional_metrics"] = (
            capo_pi.types.additional_metrics_list.deserialize_aws_json_1_1(
                data["AdditionalMetrics"]
            )
        )
    if data.get("PartitionBy") is not None:
        import capo_pi.types.dimension_group

        out["partition_by"] = capo_pi.types.dimension_group.deserialize_aws_json_1_1(
            data["PartitionBy"]
        )
    if data.get("Filter") is not None:
        import capo_pi.types.metric_query_filter_map

        out["filter"] = capo_pi.types.metric_query_filter_map.deserialize_aws_json_1_1(
            data["Filter"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
