"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityResultsV2Description``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_evaluation_run_mode
    import capo_glue.types.data_source
    import capo_glue.types.hash_string
    import capo_glue.types.name_string
    import capo_glue.types.publish_data_quality_result_descriptors
    import capo_glue.types.publish_data_quality_result_dimensions
    import capo_glue.types.timestamp


class DataQualityResultsV2Description(TypedDict, closed=True):
    result_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The unique result ID for this data quality result.</p>"""
    evaluation_run_mode: NotRequired[
        "capo_glue.types.data_quality_evaluation_run_mode.DataQualityEvaluationRunMode"
    ]
    """<p>How the evaluation run that produced the result started: <code>ON_DEMAND</code> for a run started by <code>StartDataQualityRulesetEvaluationRun</code>, or <code>EVALUATION_CONFIG</code> for a run started by a data quality evaluation configuration. Not returned for results that no evaluation run produced, such as results from any ETL job.</p>"""
    data_quality_evaluation_config: NotRequired[
        "capo_glue.types.name_string.NameString"
    ]
    """<p>The name of the data quality evaluation configuration that started the evaluation run, returned when <code>EvaluationRunMode</code> is <code>EVALUATION_CONFIG</code>.</p>"""
    data_source: NotRequired["capo_glue.types.data_source.DataSource"]
    """<p>The table associated with the data quality result, if any.</p>"""
    result_published_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The date and time when this data quality result was published.</p>"""
    dimensions: NotRequired[
        "capo_glue.types.publish_data_quality_result_dimensions.PublishDataQualityResultDimensions"
    ]
    """<p>A map of platform-specific identifiers, such as cluster, application, workgroup, or project IDs, that identify where the data quality evaluation ran.</p>"""
    evaluation_context: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The evaluation context for the data quality result. This value identifies a specific data quality result, or a series of related results, within a run.</p>"""
    descriptors: NotRequired[
        "capo_glue.types.publish_data_quality_result_descriptors.PublishDataQualityResultDescriptors"
    ]
    """<p>A map of user-provided descriptors that add contextual metadata and configuration to the data quality result, such as database name, table name, team, or environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityResultsV2Description) -> dict:
    out: dict = {}
    if "result_id" in value:
        out["ResultId"] = value["result_id"]
    if "evaluation_run_mode" in value:
        import capo_glue.types.data_quality_evaluation_run_mode

        out["EvaluationRunMode"] = (
            capo_glue.types.data_quality_evaluation_run_mode.serialize_aws_json_1_1(
                value["evaluation_run_mode"]
            )
        )
    if "data_quality_evaluation_config" in value:
        out["DataQualityEvaluationConfig"] = value["data_quality_evaluation_config"]
    if "data_source" in value:
        import capo_glue.types.data_source

        out["DataSource"] = capo_glue.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "result_published_on" in value:
        import capo_glue.types.timestamp

        out["ResultPublishedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["result_published_on"]
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
    if "descriptors" in value:
        import capo_glue.types.publish_data_quality_result_descriptors

        out["Descriptors"] = (
            capo_glue.types.publish_data_quality_result_descriptors.serialize_aws_json_1_1(
                value["descriptors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityResultsV2Description:
    out: DataQualityResultsV2Description = {}  # type: ignore[typeddict-item]
    if data.get("ResultId") is not None:
        out["result_id"] = data["ResultId"]
    if data.get("EvaluationRunMode") is not None:
        import capo_glue.types.data_quality_evaluation_run_mode

        out["evaluation_run_mode"] = (
            capo_glue.types.data_quality_evaluation_run_mode.deserialize_aws_json_1_1(
                data["EvaluationRunMode"]
            )
        )
    if data.get("DataQualityEvaluationConfig") is not None:
        out["data_quality_evaluation_config"] = data["DataQualityEvaluationConfig"]
    if data.get("DataSource") is not None:
        import capo_glue.types.data_source

        out["data_source"] = capo_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    if data.get("ResultPublishedOn") is not None:
        import capo_glue.types.timestamp

        out["result_published_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["ResultPublishedOn"]
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
    if data.get("Descriptors") is not None:
        import capo_glue.types.publish_data_quality_result_descriptors

        out["descriptors"] = (
            capo_glue.types.publish_data_quality_result_descriptors.deserialize_aws_json_1_1(
                data["Descriptors"]
            )
        )
    return out
