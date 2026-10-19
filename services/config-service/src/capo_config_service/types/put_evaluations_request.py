"""Generated from Smithy shape ``com.amazonaws.configservice#PutEvaluationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.boolean
    import capo_config_service.types.evaluations
    import capo_config_service.types.string


class PutEvaluationsRequest(TypedDict, closed=True):
    evaluations: NotRequired["capo_config_service.types.evaluations.Evaluations"]
    """<p>The assessments that the Lambda function performs. Each evaluation identifies an Amazon Web Services resource and indicates whether it complies with the Config rule that invokes the Lambda function.</p>"""
    result_token: "capo_config_service.types.string.String"
    """<p>An encrypted token that associates an evaluation with an Config rule. Identifies the rule and the event that triggered the evaluation.</p>"""
    test_mode: NotRequired["capo_config_service.types.boolean.Boolean"]
    """<p>Use this parameter to specify a test run for <code>PutEvaluations</code>. You can verify whether your Lambda function will deliver evaluation results to Config. No updates occur to your existing evaluations, and evaluation results are not sent to Config.</p> <note> <p>When <code>TestMode</code> is <code>true</code>, <code>PutEvaluations</code> doesn't require a valid value for the <code>ResultToken</code> parameter, but the value cannot be null.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEvaluationsRequest) -> dict:
    out: dict = {}
    if "evaluations" in value:
        import capo_config_service.types.evaluations

        out["Evaluations"] = (
            capo_config_service.types.evaluations.serialize_aws_json_1_1(
                value["evaluations"]
            )
        )
    out["ResultToken"] = value["result_token"]
    if "test_mode" in value:
        out["TestMode"] = value["test_mode"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutEvaluationsRequest:
    out: PutEvaluationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Evaluations") is not None:
        import capo_config_service.types.evaluations

        out["evaluations"] = (
            capo_config_service.types.evaluations.deserialize_aws_json_1_1(
                data["Evaluations"]
            )
        )
    if data.get("ResultToken") is not None:
        out["result_token"] = data["ResultToken"]
    else:
        out["result_token"] = ""
    if data.get("TestMode") is not None:
        out["test_mode"] = data["TestMode"]
    return out
