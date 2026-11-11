"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityEvaluationConfigsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_evaluation_config_level
    import capo_glue.types.data_quality_evaluation_config_page_size
    import capo_glue.types.pagination_token


class ListDataQualityEvaluationConfigsRequest(TypedDict, closed=True):
    level: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_level.DataQualityEvaluationConfigLevel"
    ]
    """<p>Lists only the configurations that apply to this level.</p>"""
    max_results: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_page_size.DataQualityEvaluationConfigPageSize"
    ]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_glue.types.pagination_token.PaginationToken"]
    """<p>A paginated token to offset the results. If you don't specify a token, the operation returns results starting from the beginning of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityEvaluationConfigsRequest) -> dict:
    out: dict = {}
    if "level" in value:
        import capo_glue.types.data_quality_evaluation_config_level

        out["Level"] = (
            capo_glue.types.data_quality_evaluation_config_level.serialize_aws_json_1_1(
                value["level"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataQualityEvaluationConfigsRequest:
    out: ListDataQualityEvaluationConfigsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Level") is not None:
        import capo_glue.types.data_quality_evaluation_config_level

        out["level"] = (
            capo_glue.types.data_quality_evaluation_config_level.deserialize_aws_json_1_1(
                data["Level"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
