"""Generated from Smithy shape ``com.amazonaws.pi#ListPerformanceAnalysisReportsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.boolean
    import capo_pi.types.identifier_string
    import capo_pi.types.max_results
    import capo_pi.types.next_token
    import capo_pi.types.service_type


class ListPerformanceAnalysisReportsRequest(TypedDict, closed=True):
    service_type: "capo_pi.types.service_type.ServiceType"
    """<p>The Amazon Web Services service for which Performance Insights returns metrics. Valid value is <code>RDS</code>.</p>"""
    identifier: "capo_pi.types.identifier_string.IdentifierString"
    """<p>An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as <i>ResourceID</i>. When you call <code>DescribeDBInstances</code>, the identifier is returned as <code>DbiResourceId</code>.</p> <p>To use a DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VW2X</code>.</p>"""
    next_token: NotRequired["capo_pi.types.next_token.NextToken"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxResults</code>.</p>"""
    max_results: NotRequired["capo_pi.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response. If more items exist than the specified <code>MaxResults</code> value, a pagination token is included in the response so that the remaining results can be retrieved. </p>"""
    list_tags: NotRequired["capo_pi.types.boolean.Boolean"]
    """<p>Specifies whether or not to include the list of tags in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPerformanceAnalysisReportsRequest) -> dict:
    out: dict = {}
    import capo_pi.types.service_type

    out["ServiceType"] = capo_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["Identifier"] = value["identifier"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "list_tags" in value:
        out["ListTags"] = value["list_tags"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPerformanceAnalysisReportsRequest:
    out: ListPerformanceAnalysisReportsRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("ListTags") is not None:
        out["list_tags"] = data["ListTags"]
    return out
