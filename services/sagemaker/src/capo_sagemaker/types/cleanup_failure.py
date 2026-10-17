"""Generated from Smithy shape ``com.amazonaws.sagemaker#CleanupFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cleanup_failure_error_code
    import capo_sagemaker.types.string256
    import capo_sagemaker.types.string2048


class CleanupFailure(TypedDict, closed=True):
    step_name: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The name of the upstream step whose Amazon S3 output resources the Cleanup step could not delete.</p>"""
    error_code: NotRequired[
        "capo_sagemaker.types.cleanup_failure_error_code.CleanupFailureErrorCode"
    ]
    """<p>The error code that identifies why the Cleanup step could not delete the output resources associated with the upstream step.</p>"""
    error_message: NotRequired["capo_sagemaker.types.string2048.String2048"]
    """<p>A message describing why the Cleanup step could not delete the output resources associated with the upstream step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CleanupFailure) -> dict:
    out: dict = {}
    if "step_name" in value:
        out["StepName"] = value["step_name"]
    if "error_code" in value:
        import capo_sagemaker.types.cleanup_failure_error_code

        out["ErrorCode"] = (
            capo_sagemaker.types.cleanup_failure_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CleanupFailure:
    out: CleanupFailure = {}  # type: ignore[typeddict-item]
    if data.get("StepName") is not None:
        out["step_name"] = data["StepName"]
    if data.get("ErrorCode") is not None:
        import capo_sagemaker.types.cleanup_failure_error_code

        out["error_code"] = (
            capo_sagemaker.types.cleanup_failure_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
