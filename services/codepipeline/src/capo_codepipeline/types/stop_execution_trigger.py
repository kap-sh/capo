"""Generated from Smithy shape ``com.amazonaws.codepipeline#StopExecutionTrigger``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.stop_pipeline_execution_reason


class StopExecutionTrigger(TypedDict, closed=True):
    reason: NotRequired[
        "capo_codepipeline.types.stop_pipeline_execution_reason.StopPipelineExecutionReason"
    ]
    """<p>The user-specified reason the pipeline was stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopExecutionTrigger) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopExecutionTrigger:
    out: StopExecutionTrigger = {}  # type: ignore[typeddict-item]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopExecutionTrigger) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_cbor(data: dict) -> StopExecutionTrigger:
    out: StopExecutionTrigger = {}  # type: ignore[typeddict-item]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
