"""Generated from Smithy shape ``com.amazonaws.sagemaker#ForEachStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.for_each_selector_result
    import capo_sagemaker.types.for_each_status
    import capo_sagemaker.types.integer


class ForEachStepMetadata(TypedDict, closed=True):
    status: NotRequired["capo_sagemaker.types.for_each_status.ForEachStatus"]
    """<p>The status of the ForEach step execution.</p>"""
    input_item_count: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The number of input items that the ForEach step iterates over.</p>"""
    total_step_count: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The total number of steps generated across all iterations of the ForEach step.</p>"""
    succeeded_step_count: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The number of iteration steps that completed successfully.</p>"""
    failed_step_count: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The number of iteration steps that failed.</p>"""
    stopped_step_count: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The number of iteration steps that were stopped.</p>"""
    selector: NotRequired[
        "capo_sagemaker.types.for_each_selector_result.ForEachSelectorResult"
    ]
    """<p>Identifies the body step and iteration selected within the ForEach step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForEachStepMetadata) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_sagemaker.types.for_each_status

        out["Status"] = capo_sagemaker.types.for_each_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "input_item_count" in value:
        out["InputItemCount"] = value["input_item_count"]
    if "total_step_count" in value:
        out["TotalStepCount"] = value["total_step_count"]
    if "succeeded_step_count" in value:
        out["SucceededStepCount"] = value["succeeded_step_count"]
    if "failed_step_count" in value:
        out["FailedStepCount"] = value["failed_step_count"]
    if "stopped_step_count" in value:
        out["StoppedStepCount"] = value["stopped_step_count"]
    if "selector" in value:
        import capo_sagemaker.types.for_each_selector_result

        out["Selector"] = (
            capo_sagemaker.types.for_each_selector_result.serialize_aws_json_1_1(
                value["selector"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ForEachStepMetadata:
    out: ForEachStepMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_sagemaker.types.for_each_status

        out["status"] = capo_sagemaker.types.for_each_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("InputItemCount") is not None:
        out["input_item_count"] = data["InputItemCount"]
    if data.get("TotalStepCount") is not None:
        out["total_step_count"] = data["TotalStepCount"]
    if data.get("SucceededStepCount") is not None:
        out["succeeded_step_count"] = data["SucceededStepCount"]
    if data.get("FailedStepCount") is not None:
        out["failed_step_count"] = data["FailedStepCount"]
    if data.get("StoppedStepCount") is not None:
        out["stopped_step_count"] = data["StoppedStepCount"]
    if data.get("Selector") is not None:
        import capo_sagemaker.types.for_each_selector_result

        out["selector"] = (
            capo_sagemaker.types.for_each_selector_result.deserialize_aws_json_1_1(
                data["Selector"]
            )
        )
    return out
