"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityResultsV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_results_v2_filter_criteria
    import capo_glue.types.page_size
    import capo_glue.types.pagination_token


class ListDataQualityResultsV2Request(TypedDict, closed=True):
    filter: NotRequired[
        "capo_glue.types.data_quality_results_v2_filter_criteria.DataQualityResultsV2FilterCriteria"
    ]
    """<p>The filter criteria.</p>"""
    next_token: NotRequired["capo_glue.types.pagination_token.PaginationToken"]
    """<p>A pagination token to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum number of results to return. If you don't specify a value, the operation uses the default number of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityResultsV2Request) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_glue.types.data_quality_results_v2_filter_criteria

        out["Filter"] = (
            capo_glue.types.data_quality_results_v2_filter_criteria.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataQualityResultsV2Request:
    out: ListDataQualityResultsV2Request = {}  # type: ignore[typeddict-item]
    if data.get("Filter") is not None:
        import capo_glue.types.data_quality_results_v2_filter_criteria

        out["filter"] = (
            capo_glue.types.data_quality_results_v2_filter_criteria.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
