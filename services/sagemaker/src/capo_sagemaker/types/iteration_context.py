"""Generated from Smithy shape ``com.amazonaws.sagemaker#IterationContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.integer
    import capo_sagemaker.types.string256
    import capo_sagemaker.types.string12800


class IterationContext(TypedDict, closed=True):
    parent_step_name: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The name of the ForEach step that generated this iteration.</p>"""
    index: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The index of the iteration within the ForEach step.</p>"""
    item: NotRequired["capo_sagemaker.types.string12800.String12800"]
    """<p>The input item that is being processed in this iteration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IterationContext) -> dict:
    out: dict = {}
    if "parent_step_name" in value:
        out["ParentStepName"] = value["parent_step_name"]
    if "index" in value:
        out["Index"] = value["index"]
    if "item" in value:
        out["Item"] = value["item"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IterationContext:
    out: IterationContext = {}  # type: ignore[typeddict-item]
    if data.get("ParentStepName") is not None:
        out["parent_step_name"] = data["ParentStepName"]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    if data.get("Item") is not None:
        out["item"] = data["Item"]
    return out
