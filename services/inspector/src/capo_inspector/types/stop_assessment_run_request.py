"""Generated from Smithy shape ``com.amazonaws.inspector#StopAssessmentRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.stop_action


class StopAssessmentRunRequest(TypedDict, closed=True):
    assessment_run_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the assessment run that you want to stop.</p>"""
    stop_action: NotRequired["capo_inspector.types.stop_action.StopAction"]
    """<p>An input option that can be set to either START_EVALUATION or SKIP_EVALUATION. START_EVALUATION (the default value), stops the AWS agent from collecting data and begins the results evaluation and the findings generation process. SKIP_EVALUATION cancels the assessment run immediately, after which no findings are generated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopAssessmentRunRequest) -> dict:
    out: dict = {}
    out["assessmentRunArn"] = value["assessment_run_arn"]
    if "stop_action" in value:
        import capo_inspector.types.stop_action

        out["stopAction"] = capo_inspector.types.stop_action.serialize_aws_json_1_1(
            value["stop_action"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopAssessmentRunRequest:
    out: StopAssessmentRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("assessmentRunArn") is not None:
        out["assessment_run_arn"] = data["assessmentRunArn"]
    else:
        out["assessment_run_arn"] = ""
    if data.get("stopAction") is not None:
        import capo_inspector.types.stop_action

        out["stop_action"] = capo_inspector.types.stop_action.deserialize_aws_json_1_1(
            data["stopAction"]
        )
    return out
