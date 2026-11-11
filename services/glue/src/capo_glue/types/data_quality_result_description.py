"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityResultDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_evaluation_run_mode
    import capo_glue.types.data_source
    import capo_glue.types.hash_string
    import capo_glue.types.name_string
    import capo_glue.types.timestamp


class DataQualityResultDescription(TypedDict, closed=True):
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
    """<p>The table name associated with the data quality result.</p>"""
    job_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The job name associated with the data quality result.</p>"""
    job_run_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The job run ID associated with the data quality result.</p>"""
    started_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time that the run started for this data quality result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityResultDescription) -> dict:
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
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_run_id" in value:
        out["JobRunId"] = value["job_run_id"]
    if "started_on" in value:
        import capo_glue.types.timestamp

        out["StartedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_on"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityResultDescription:
    out: DataQualityResultDescription = {}  # type: ignore[typeddict-item]
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
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobRunId") is not None:
        out["job_run_id"] = data["JobRunId"]
    if data.get("StartedOn") is not None:
        import capo_glue.types.timestamp

        out["started_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedOn"]
        )
    return out
