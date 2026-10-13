"""Generated from Smithy shape ``com.amazonaws.pi#ListPerformanceAnalysisReportRecommendationsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.next_token
    import capo_pi.types.recommendation_list


class ListPerformanceAnalysisReportRecommendationsResponse(TypedDict, closed=True):
    recommendations: NotRequired["capo_pi.types.recommendation_list.RecommendationList"]
    """<p>The list of recommendations for the analysis report.</p>"""
    next_token: NotRequired["capo_pi.types.next_token.NextToken"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxResults</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListPerformanceAnalysisReportRecommendationsResponse,
) -> dict:
    out: dict = {}
    if "recommendations" in value:
        import capo_pi.types.recommendation_list

        out["Recommendations"] = (
            capo_pi.types.recommendation_list.serialize_aws_json_1_1(
                value["recommendations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListPerformanceAnalysisReportRecommendationsResponse:
    out: ListPerformanceAnalysisReportRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Recommendations") is not None:
        import capo_pi.types.recommendation_list

        out["recommendations"] = (
            capo_pi.types.recommendation_list.deserialize_aws_json_1_1(
                data["Recommendations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(
    value: ListPerformanceAnalysisReportRecommendationsResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recommendations" in value:
        import capo_pi.types.recommendation_list

        out["recommendations"] = capo_pi.types.recommendation_list.redact_sensitive(
            value["recommendations"]
        )
    return out
