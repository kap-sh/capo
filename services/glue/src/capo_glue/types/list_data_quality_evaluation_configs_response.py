"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityEvaluationConfigsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_evaluation_config_list
    import capo_glue.types.pagination_token


class ListDataQualityEvaluationConfigsResponse(TypedDict, closed=True):
    data_quality_evaluation_configs: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_list.DataQualityEvaluationConfigList"
    ]
    """<p>A list of <code>DataQualityEvaluationConfigListDetails</code> objects.</p>"""
    next_token: NotRequired["capo_glue.types.pagination_token.PaginationToken"]
    """<p>A pagination token, if more results are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityEvaluationConfigsResponse) -> dict:
    out: dict = {}
    if "data_quality_evaluation_configs" in value:
        import capo_glue.types.data_quality_evaluation_config_list

        out["DataQualityEvaluationConfigs"] = (
            capo_glue.types.data_quality_evaluation_config_list.serialize_aws_json_1_1(
                value["data_quality_evaluation_configs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataQualityEvaluationConfigsResponse:
    out: ListDataQualityEvaluationConfigsResponse = {}  # type: ignore[typeddict-item]
    if data.get("DataQualityEvaluationConfigs") is not None:
        import capo_glue.types.data_quality_evaluation_config_list

        out["data_quality_evaluation_configs"] = (
            capo_glue.types.data_quality_evaluation_config_list.deserialize_aws_json_1_1(
                data["DataQualityEvaluationConfigs"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
