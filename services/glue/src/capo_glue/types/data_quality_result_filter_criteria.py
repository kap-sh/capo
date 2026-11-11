"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityResultFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_evaluation_run_mode
    import capo_glue.types.data_source
    import capo_glue.types.hash_string
    import capo_glue.types.name_string
    import capo_glue.types.timestamp


class DataQualityResultFilterCriteria(TypedDict, closed=True):
    data_source: NotRequired["capo_glue.types.data_source.DataSource"]
    """<p>Filter results by the specified data source. For example, retrieving all results for an Glue table.</p>"""
    job_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>Filter results by the specified job name.</p>"""
    job_run_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>Filter results by the specified job run ID.</p>"""
    started_after: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>Filter results by runs that started after this time.</p>"""
    started_before: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>Filter results by runs that started before this time.</p>"""
    evaluation_run_mode: NotRequired[
        "capo_glue.types.data_quality_evaluation_run_mode.DataQualityEvaluationRunMode"
    ]
    """<p>Filter results by how their evaluation run started: <code>ON_DEMAND</code> or <code>EVALUATION_CONFIG</code>. Results that no evaluation run produced match neither value.</p>"""
    data_quality_evaluation_config: NotRequired[
        "capo_glue.types.name_string.NameString"
    ]
    """<p>Filter results by the evaluation configuration name which started the evaluation run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityResultFilterCriteria) -> dict:
    out: dict = {}
    if "data_source" in value:
        import capo_glue.types.data_source

        out["DataSource"] = capo_glue.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_run_id" in value:
        out["JobRunId"] = value["job_run_id"]
    if "started_after" in value:
        import capo_glue.types.timestamp

        out["StartedAfter"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_after"]
        )
    if "started_before" in value:
        import capo_glue.types.timestamp

        out["StartedBefore"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_before"]
        )
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


def deserialize_aws_json_1_1(data: dict) -> DataQualityResultFilterCriteria:
    out: DataQualityResultFilterCriteria = {}  # type: ignore[typeddict-item]
    if data.get("DataSource") is not None:
        import capo_glue.types.data_source

        out["data_source"] = capo_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobRunId") is not None:
        out["job_run_id"] = data["JobRunId"]
    if data.get("StartedAfter") is not None:
        import capo_glue.types.timestamp

        out["started_after"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedAfter"]
        )
    if data.get("StartedBefore") is not None:
        import capo_glue.types.timestamp

        out["started_before"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedBefore"]
        )
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
