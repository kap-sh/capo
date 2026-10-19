"""Generated from Smithy shape ``com.amazonaws.pi#ListAvailableResourceMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.identifier_string
    import capo_pi.types.max_results
    import capo_pi.types.metric_type_list
    import capo_pi.types.next_token
    import capo_pi.types.service_type


class ListAvailableResourceMetricsRequest(TypedDict, closed=True):
    service_type: "capo_pi.types.service_type.ServiceType"
    """<p>The Amazon Web Services service for which Performance Insights returns metrics.</p>"""
    identifier: "capo_pi.types.identifier_string.IdentifierString"
    """<p>An immutable identifier for a data source that is unique within an Amazon Web Services Region. Performance Insights gathers metrics from this data source. To use an Amazon RDS DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VWZ</code>. </p>"""
    metric_types: "capo_pi.types.metric_type_list.MetricTypeList"
    """<p>The types of metrics to return in the response. Valid values in the array include the following:</p> <ul> <li> <p> <code>os</code> (OS counter metrics) - All engines</p> </li> <li> <p> <code>db</code> (DB load metrics) - All engines except for Amazon DocumentDB</p> </li> <li> <p> <code>db.sql.stats</code> (per-SQL metrics) - All engines except for Amazon DocumentDB</p> </li> <li> <p> <code>db.sql_tokenized.stats</code> (per-SQL digest metrics) - All engines except for Amazon DocumentDB</p> </li> </ul>"""
    next_token: NotRequired["capo_pi.types.next_token.NextToken"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxRecords</code>. </p>"""
    max_results: NotRequired["capo_pi.types.max_results.MaxResults"]
    """<p>The maximum number of items to return. If the <code>MaxRecords</code> value is less than the number of existing items, the response includes a pagination token. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAvailableResourceMetricsRequest) -> dict:
    out: dict = {}
    import capo_pi.types.service_type

    out["ServiceType"] = capo_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["Identifier"] = value["identifier"]
    import capo_pi.types.metric_type_list

    out["MetricTypes"] = capo_pi.types.metric_type_list.serialize_aws_json_1_1(
        value["metric_types"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAvailableResourceMetricsRequest:
    out: ListAvailableResourceMetricsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceType") is not None:
        import capo_pi.types.service_type

        out["service_type"] = capo_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    else:
        import typing

        out["service_type"] = typing.cast("capo_pi.types.service_type.ServiceType", "")
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("MetricTypes") is not None:
        import capo_pi.types.metric_type_list

        out["metric_types"] = capo_pi.types.metric_type_list.deserialize_aws_json_1_1(
            data["MetricTypes"]
        )
    else:
        out["metric_types"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
