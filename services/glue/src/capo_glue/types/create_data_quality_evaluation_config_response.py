"""Generated from Smithy shape ``com.amazonaws.glue#CreateDataQualityEvaluationConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_evaluation_run_mode
    import capo_glue.types.name_string


class CreateDataQualityEvaluationConfigResponse(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the data quality evaluation configuration.</p>"""
    evaluation_run_mode: NotRequired[
        "capo_glue.types.data_quality_evaluation_run_mode.DataQualityEvaluationRunMode"
    ]
    """<p>The evaluation run mode of the configuration's results, which is <code>EVALUATION_CONFIG</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataQualityEvaluationConfigResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "evaluation_run_mode" in value:
        import capo_glue.types.data_quality_evaluation_run_mode

        out["EvaluationRunMode"] = (
            capo_glue.types.data_quality_evaluation_run_mode.serialize_aws_json_1_1(
                value["evaluation_run_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataQualityEvaluationConfigResponse:
    out: CreateDataQualityEvaluationConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("EvaluationRunMode") is not None:
        import capo_glue.types.data_quality_evaluation_run_mode

        out["evaluation_run_mode"] = (
            capo_glue.types.data_quality_evaluation_run_mode.deserialize_aws_json_1_1(
                data["EvaluationRunMode"]
            )
        )
    return out
