"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#InvokeBlueprintOptimizationAsyncResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_optimization_invocation_arn


class InvokeBlueprintOptimizationAsyncResponse(TypedDict, closed=True):
    invocation_arn: "capo_bedrock_data_automation.types.blueprint_optimization_invocation_arn.BlueprintOptimizationInvocationArn"
    """ARN of the blueprint optimization job"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeBlueprintOptimizationAsyncResponse) -> dict:
    out: dict = {}
    out["invocationArn"] = value["invocation_arn"]
    return out


def deserialize_json(data: dict) -> InvokeBlueprintOptimizationAsyncResponse:
    out: InvokeBlueprintOptimizationAsyncResponse = {}  # type: ignore[typeddict-item]
    if data.get("invocationArn") is not None:
        out["invocation_arn"] = data["invocationArn"]
    else:
        out["invocation_arn"] = ""
    return out
