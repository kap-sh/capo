"""Generated from Smithy shape ``com.amazonaws.sagemaker#CleanupStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cleanup_failure_list
    import capo_sagemaker.types.cleanup_step_name_list


class CleanupStepMetadata(TypedDict, closed=True):
    cleaned_steps: NotRequired[
        "capo_sagemaker.types.cleanup_step_name_list.CleanupStepNameList"
    ]
    """<p>The names of upstream steps whose Amazon S3 output resources the Cleanup step deleted successfully.</p>"""
    failed_steps: NotRequired[
        "capo_sagemaker.types.cleanup_failure_list.CleanupFailureList"
    ]
    """<p>The upstream steps whose Amazon S3 output resources the Cleanup step could not delete.</p>"""
    skipped_steps: NotRequired[
        "capo_sagemaker.types.cleanup_step_name_list.CleanupStepNameList"
    ]
    """<p>The names of upstream steps that the Cleanup step skipped. The Cleanup step skips a step when the output properties needed to locate its resources are unavailable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CleanupStepMetadata) -> dict:
    out: dict = {}
    if "cleaned_steps" in value:
        import capo_sagemaker.types.cleanup_step_name_list

        out["CleanedSteps"] = (
            capo_sagemaker.types.cleanup_step_name_list.serialize_aws_json_1_1(
                value["cleaned_steps"]
            )
        )
    if "failed_steps" in value:
        import capo_sagemaker.types.cleanup_failure_list

        out["FailedSteps"] = (
            capo_sagemaker.types.cleanup_failure_list.serialize_aws_json_1_1(
                value["failed_steps"]
            )
        )
    if "skipped_steps" in value:
        import capo_sagemaker.types.cleanup_step_name_list

        out["SkippedSteps"] = (
            capo_sagemaker.types.cleanup_step_name_list.serialize_aws_json_1_1(
                value["skipped_steps"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CleanupStepMetadata:
    out: CleanupStepMetadata = {}  # type: ignore[typeddict-item]
    if data.get("CleanedSteps") is not None:
        import capo_sagemaker.types.cleanup_step_name_list

        out["cleaned_steps"] = (
            capo_sagemaker.types.cleanup_step_name_list.deserialize_aws_json_1_1(
                data["CleanedSteps"]
            )
        )
    if data.get("FailedSteps") is not None:
        import capo_sagemaker.types.cleanup_failure_list

        out["failed_steps"] = (
            capo_sagemaker.types.cleanup_failure_list.deserialize_aws_json_1_1(
                data["FailedSteps"]
            )
        )
    if data.get("SkippedSteps") is not None:
        import capo_sagemaker.types.cleanup_step_name_list

        out["skipped_steps"] = (
            capo_sagemaker.types.cleanup_step_name_list.deserialize_aws_json_1_1(
                data["SkippedSteps"]
            )
        )
    return out
