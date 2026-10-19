"""Generated from Smithy shape ``com.amazonaws.pi#ListPerformanceAnalysisReportRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.analysis_report_id
    import capo_pi.types.identifier_string
    import capo_pi.types.max_results
    import capo_pi.types.next_token
    import capo_pi.types.recommendation_id_list
    import capo_pi.types.service_type


class ListPerformanceAnalysisReportRecommendationsRequest(TypedDict, closed=True):
    service_type: "capo_pi.types.service_type.ServiceType"
    """<p>The Amazon Web Services service for which Performance Insights returns metrics. Valid value is <code>RDS</code>.</p>"""
    identifier: "capo_pi.types.identifier_string.IdentifierString"
    """<p>An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as <i>ResourceID</i>. When you call <code>DescribeDBInstances</code>, the identifier is returned as <code>DbiResourceId</code>.</p> <p>To use a DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VW2X</code>.</p>"""
    analysis_report_id: "capo_pi.types.analysis_report_id.AnalysisReportId"
    """<p>A unique identifier of the created analysis report. For example, <code>report-12345678901234567</code> </p>"""
    recommendation_ids: NotRequired[
        "capo_pi.types.recommendation_id_list.RecommendationIdList"
    ]
    """<p>A list of recommendation identifiers to filter the results.</p>"""
    max_results: NotRequired["capo_pi.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response. If more items exist than the specified <code>MaxResults</code> value, a pagination token is included in the response so that the remaining results can be retrieved. </p>"""
    next_token: NotRequired["capo_pi.types.next_token.NextToken"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxResults</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListPerformanceAnalysisReportRecommendationsRequest,
) -> dict:
    out: dict = {}
    import capo_pi.types.service_type

    out["ServiceType"] = capo_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["Identifier"] = value["identifier"]
    out["AnalysisReportId"] = value["analysis_report_id"]
    if "recommendation_ids" in value:
        import capo_pi.types.recommendation_id_list

        out["RecommendationIds"] = (
            capo_pi.types.recommendation_id_list.serialize_aws_json_1_1(
                value["recommendation_ids"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListPerformanceAnalysisReportRecommendationsRequest:
    out: ListPerformanceAnalysisReportRecommendationsRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("AnalysisReportId") is not None:
        out["analysis_report_id"] = data["AnalysisReportId"]
    else:
        out["analysis_report_id"] = ""
    if data.get("RecommendationIds") is not None:
        import capo_pi.types.recommendation_id_list

        out["recommendation_ids"] = (
            capo_pi.types.recommendation_id_list.deserialize_aws_json_1_1(
                data["RecommendationIds"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
