"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityResultsV2FilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_evaluation_run_mode
    import capo_glue.types.data_source
    import capo_glue.types.name_string
    import capo_glue.types.publish_data_quality_result_dimensions
    import capo_glue.types.timestamp


class DataQualityResultsV2FilterCriteria(TypedDict, closed=True):
    data_source: NotRequired["capo_glue.types.data_source.DataSource"]
    """<p>The data source used to filter the results. For example, you can retrieve all results for an Glue table. <code>DatabaseName</code> and <code>TableName</code> are required. If you omit <code>CatalogId</code>, the catalog of the calling account is used.</p> <p>When you filter by data source, a page of results can be empty but still include a <code>NextToken</code>. Keep requesting pages until <code>NextToken</code> is absent.</p>"""
    published_after: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time after which to include published results.</p>"""
    published_before: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time before which to include published results.</p>"""
    dimensions: NotRequired[
        "capo_glue.types.publish_data_quality_result_dimensions.PublishDataQualityResultDimensions"
    ]
    """<p>The platform dimensions to filter results by.</p>"""
    evaluation_context: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The evaluation context to filter results by.</p>"""
    evaluation_run_mode: NotRequired[
        "capo_glue.types.data_quality_evaluation_run_mode.DataQualityEvaluationRunMode"
    ]
    """<p>Filter results by how their evaluation run started: <code>ON_DEMAND</code> or <code>EVALUATION_CONFIG</code>. Results that no evaluation run produced match neither value.</p>"""
    data_quality_evaluation_config: NotRequired[
        "capo_glue.types.name_string.NameString"
    ]
    """<p>Filter results by the evaluation configuration name which started the evaluation run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityResultsV2FilterCriteria) -> dict:
    out: dict = {}
    if "data_source" in value:
        import capo_glue.types.data_source

        out["DataSource"] = capo_glue.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "published_after" in value:
        import capo_glue.types.timestamp

        out["PublishedAfter"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["published_after"]
        )
    if "published_before" in value:
        import capo_glue.types.timestamp

        out["PublishedBefore"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["published_before"]
        )
    if "dimensions" in value:
        import capo_glue.types.publish_data_quality_result_dimensions

        out["Dimensions"] = (
            capo_glue.types.publish_data_quality_result_dimensions.serialize_aws_json_1_1(
                value["dimensions"]
            )
        )
    if "evaluation_context" in value:
        out["EvaluationContext"] = value["evaluation_context"]
    if "evaluation_run_mode" in value:
        import capo_glue.types.data_quality_evaluation_run_mode

        out["EvaluationRunMode"] = (
            capo_glue.types.data_quality_evaluation_run_mode.serialize_aws_json_1_1(
                value["evaluation_run_mode"]
            )
        )
    if "data_quality_evaluation_config" in value:
        out["DataQualityEvaluationConfig"] = value["data_quality_evaluation_config"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityResultsV2FilterCriteria:
    out: DataQualityResultsV2FilterCriteria = {}  # type: ignore[typeddict-item]
    if data.get("DataSource") is not None:
        import capo_glue.types.data_source

        out["data_source"] = capo_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    if data.get("PublishedAfter") is not None:
        import capo_glue.types.timestamp

        out["published_after"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["PublishedAfter"]
        )
    if data.get("PublishedBefore") is not None:
        import capo_glue.types.timestamp

        out["published_before"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["PublishedBefore"]
        )
    if data.get("Dimensions") is not None:
        import capo_glue.types.publish_data_quality_result_dimensions

        out["dimensions"] = (
            capo_glue.types.publish_data_quality_result_dimensions.deserialize_aws_json_1_1(
                data["Dimensions"]
            )
        )
    if data.get("EvaluationContext") is not None:
        out["evaluation_context"] = data["EvaluationContext"]
    if data.get("EvaluationRunMode") is not None:
        import capo_glue.types.data_quality_evaluation_run_mode

        out["evaluation_run_mode"] = (
            capo_glue.types.data_quality_evaluation_run_mode.deserialize_aws_json_1_1(
                data["EvaluationRunMode"]
            )
        )
    if data.get("DataQualityEvaluationConfig") is not None:
        out["data_quality_evaluation_config"] = data["DataQualityEvaluationConfig"]
    return out
