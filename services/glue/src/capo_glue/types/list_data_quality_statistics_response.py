"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityStatisticsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.pagination_token
    import capo_glue.types.statistic_summary_list


class ListDataQualityStatisticsResponse(TypedDict, closed=True):
    statistics: NotRequired[
        "capo_glue.types.statistic_summary_list.StatisticSummaryList"
    ]
    """<p>A <code>StatisticSummaryList</code>.</p>"""
    next_token: NotRequired["capo_glue.types.pagination_token.PaginationToken"]
    """<p>A pagination token to request the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityStatisticsResponse) -> dict:
    out: dict = {}
    if "statistics" in value:
        import capo_glue.types.statistic_summary_list

        out["Statistics"] = (
            capo_glue.types.statistic_summary_list.serialize_aws_json_1_1(
                value["statistics"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataQualityStatisticsResponse:
    out: ListDataQualityStatisticsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Statistics") is not None:
        import capo_glue.types.statistic_summary_list

        out["statistics"] = (
            capo_glue.types.statistic_summary_list.deserialize_aws_json_1_1(
                data["Statistics"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListDataQualityStatisticsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "statistics" in value:
        import capo_glue.types.statistic_summary_list

        out["statistics"] = capo_glue.types.statistic_summary_list.redact_sensitive(
            value["statistics"]
        )
    return out
