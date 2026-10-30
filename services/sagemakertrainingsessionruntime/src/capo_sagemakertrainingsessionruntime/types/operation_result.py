"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#OperationResult``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemakertrainingsessionruntime.errors import (
    DeserializationError,
    SerializationError,
)
from capo_sagemakertrainingsessionruntime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.forward_backward_result
    import capo_sagemakertrainingsessionruntime.types.forward_result
    import capo_sagemakertrainingsessionruntime.types.load_state_result
    import capo_sagemakertrainingsessionruntime.types.optimizer_step_result
    import capo_sagemakertrainingsessionruntime.types.save_state_result
    import capo_sagemakertrainingsessionruntime.types.save_weights_result


class OperationResultForwardMember(TypedDict, closed=True):
    forward: "capo_sagemakertrainingsessionruntime.types.forward_result.ForwardResult"


class OperationResultForwardBackwardMember(TypedDict, closed=True):
    forwardBackward: "capo_sagemakertrainingsessionruntime.types.forward_backward_result.ForwardBackwardResult"


class OperationResultOptimizerStepMember(TypedDict, closed=True):
    optimizerStep: "capo_sagemakertrainingsessionruntime.types.optimizer_step_result.OptimizerStepResult"


class OperationResultSaveWeightsMember(TypedDict, closed=True):
    saveWeights: "capo_sagemakertrainingsessionruntime.types.save_weights_result.SaveWeightsResult"


class OperationResultSaveStateMember(TypedDict, closed=True):
    saveState: (
        "capo_sagemakertrainingsessionruntime.types.save_state_result.SaveStateResult"
    )


class OperationResultLoadStateMember(TypedDict, closed=True):
    loadState: (
        "capo_sagemakertrainingsessionruntime.types.load_state_result.LoadStateResult"
    )


OperationResult: TypeAlias = (
    OperationResultForwardMember
    | OperationResultForwardBackwardMember
    | OperationResultOptimizerStepMember
    | OperationResultSaveWeightsMember
    | OperationResultSaveStateMember
    | OperationResultLoadStateMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: OperationResult) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OperationResult: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "forward" in value:
        import capo_sagemakertrainingsessionruntime.types.forward_result

        return {
            "forward": capo_sagemakertrainingsessionruntime.types.forward_result.serialize_json(
                value["forward"]
            )
        }
    elif "forwardBackward" in value:
        import capo_sagemakertrainingsessionruntime.types.forward_backward_result

        return {
            "forwardBackward": capo_sagemakertrainingsessionruntime.types.forward_backward_result.serialize_json(
                value["forwardBackward"]
            )
        }
    elif "optimizerStep" in value:
        import capo_sagemakertrainingsessionruntime.types.optimizer_step_result

        return {
            "optimizerStep": capo_sagemakertrainingsessionruntime.types.optimizer_step_result.serialize_json(
                value["optimizerStep"]
            )
        }
    elif "saveWeights" in value:
        import capo_sagemakertrainingsessionruntime.types.save_weights_result

        return {
            "saveWeights": capo_sagemakertrainingsessionruntime.types.save_weights_result.serialize_json(
                value["saveWeights"]
            )
        }
    elif "saveState" in value:
        import capo_sagemakertrainingsessionruntime.types.save_state_result

        return {
            "saveState": capo_sagemakertrainingsessionruntime.types.save_state_result.serialize_json(
                value["saveState"]
            )
        }
    elif "loadState" in value:
        import capo_sagemakertrainingsessionruntime.types.load_state_result

        return {
            "loadState": capo_sagemakertrainingsessionruntime.types.load_state_result.serialize_json(
                value["loadState"]
            )
        }
    else:
        raise SerializationError("OperationResult: no variant present")


def deserialize_json(data: dict) -> OperationResult:
    if data.get("forward") is not None:
        import capo_sagemakertrainingsessionruntime.types.forward_result

        return {
            "forward": capo_sagemakertrainingsessionruntime.types.forward_result.deserialize_json(
                data["forward"]
            )
        }
    elif data.get("forwardBackward") is not None:
        import capo_sagemakertrainingsessionruntime.types.forward_backward_result

        return {
            "forwardBackward": capo_sagemakertrainingsessionruntime.types.forward_backward_result.deserialize_json(
                data["forwardBackward"]
            )
        }
    elif data.get("optimizerStep") is not None:
        import capo_sagemakertrainingsessionruntime.types.optimizer_step_result

        return {
            "optimizerStep": capo_sagemakertrainingsessionruntime.types.optimizer_step_result.deserialize_json(
                data["optimizerStep"]
            )
        }
    elif data.get("saveWeights") is not None:
        import capo_sagemakertrainingsessionruntime.types.save_weights_result

        return {
            "saveWeights": capo_sagemakertrainingsessionruntime.types.save_weights_result.deserialize_json(
                data["saveWeights"]
            )
        }
    elif data.get("saveState") is not None:
        import capo_sagemakertrainingsessionruntime.types.save_state_result

        return {
            "saveState": capo_sagemakertrainingsessionruntime.types.save_state_result.deserialize_json(
                data["saveState"]
            )
        }
    elif data.get("loadState") is not None:
        import capo_sagemakertrainingsessionruntime.types.load_state_result

        return {
            "loadState": capo_sagemakertrainingsessionruntime.types.load_state_result.deserialize_json(
                data["loadState"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("OperationResult: no recognized variant key")
