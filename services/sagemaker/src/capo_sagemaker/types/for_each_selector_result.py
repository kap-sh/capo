"""Generated from Smithy shape ``com.amazonaws.sagemaker#ForEachSelectorResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.integer
    import capo_sagemaker.types.string256


class ForEachSelectorResult(TypedDict, closed=True):
    step_name: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The name of the step associated with the iteration.</p>"""
    index: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The index of the iteration within the ForEach step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForEachSelectorResult) -> dict:
    out: dict = {}
    if "step_name" in value:
        out["StepName"] = value["step_name"]
    if "index" in value:
        out["Index"] = value["index"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ForEachSelectorResult:
    out: ForEachSelectorResult = {}  # type: ignore[typeddict-item]
    if data.get("StepName") is not None:
        out["step_name"] = data["StepName"]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    return out
