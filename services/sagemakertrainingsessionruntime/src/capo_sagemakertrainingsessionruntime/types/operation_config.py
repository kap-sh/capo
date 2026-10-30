"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#OperationConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_sagemakertrainingsessionruntime.errors import (
    DeserializationError,
    SerializationError,
)
from capo_sagemakertrainingsessionruntime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.forward_backward_config
    import capo_sagemakertrainingsessionruntime.types.forward_config
    import capo_sagemakertrainingsessionruntime.types.load_state_config
    import capo_sagemakertrainingsessionruntime.types.optimizer_step_config
    import capo_sagemakertrainingsessionruntime.types.save_state_config
    import capo_sagemakertrainingsessionruntime.types.save_weights_config


class OperationConfigForwardMember(TypedDict, closed=True):
    forward: "capo_sagemakertrainingsessionruntime.types.forward_config.ForwardConfig"


class OperationConfigForwardBackwardMember(TypedDict, closed=True):
    forwardBackward: "capo_sagemakertrainingsessionruntime.types.forward_backward_config.ForwardBackwardConfig"


class OperationConfigOptimizerStepMember(TypedDict, closed=True):
    optimizerStep: "capo_sagemakertrainingsessionruntime.types.optimizer_step_config.OptimizerStepConfig"


class OperationConfigSaveWeightsMember(TypedDict, closed=True):
    saveWeights: "capo_sagemakertrainingsessionruntime.types.save_weights_config.SaveWeightsConfig"


class OperationConfigSaveStateMember(TypedDict, closed=True):
    saveState: (
        "capo_sagemakertrainingsessionruntime.types.save_state_config.SaveStateConfig"
    )


class OperationConfigLoadStateMember(TypedDict, closed=True):
    loadState: (
        "capo_sagemakertrainingsessionruntime.types.load_state_config.LoadStateConfig"
    )


OperationConfig: TypeAlias = (
    OperationConfigForwardMember
    | OperationConfigForwardBackwardMember
    | OperationConfigOptimizerStepMember
    | OperationConfigSaveWeightsMember
    | OperationConfigSaveStateMember
    | OperationConfigLoadStateMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: OperationConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OperationConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "forward" in value:
        import capo_sagemakertrainingsessionruntime.types.forward_config

        return {
            "forward": capo_sagemakertrainingsessionruntime.types.forward_config.serialize_json(
                value["forward"]
            )
        }
    elif "forwardBackward" in value:
        import capo_sagemakertrainingsessionruntime.types.forward_backward_config

        return {
            "forwardBackward": capo_sagemakertrainingsessionruntime.types.forward_backward_config.serialize_json(
                value["forwardBackward"]
            )
        }
    elif "optimizerStep" in value:
        import capo_sagemakertrainingsessionruntime.types.optimizer_step_config

        return {
            "optimizerStep": capo_sagemakertrainingsessionruntime.types.optimizer_step_config.serialize_json(
                value["optimizerStep"]
            )
        }
    elif "saveWeights" in value:
        import capo_sagemakertrainingsessionruntime.types.save_weights_config

        return {
            "saveWeights": capo_sagemakertrainingsessionruntime.types.save_weights_config.serialize_json(
                value["saveWeights"]
            )
        }
    elif "saveState" in value:
        import capo_sagemakertrainingsessionruntime.types.save_state_config

        return {
            "saveState": capo_sagemakertrainingsessionruntime.types.save_state_config.serialize_json(
                value["saveState"]
            )
        }
    elif "loadState" in value:
        import capo_sagemakertrainingsessionruntime.types.load_state_config

        return {
            "loadState": capo_sagemakertrainingsessionruntime.types.load_state_config.serialize_json(
                value["loadState"]
            )
        }
    else:
        raise SerializationError("OperationConfig: no variant present")


def deserialize_json(data: dict) -> OperationConfig:
    if data.get("forward") is not None:
        import capo_sagemakertrainingsessionruntime.types.forward_config

        return {
            "forward": capo_sagemakertrainingsessionruntime.types.forward_config.deserialize_json(
                data["forward"]
            )
        }
    elif data.get("forwardBackward") is not None:
        import capo_sagemakertrainingsessionruntime.types.forward_backward_config

        return {
            "forwardBackward": capo_sagemakertrainingsessionruntime.types.forward_backward_config.deserialize_json(
                data["forwardBackward"]
            )
        }
    elif data.get("optimizerStep") is not None:
        import capo_sagemakertrainingsessionruntime.types.optimizer_step_config

        return {
            "optimizerStep": capo_sagemakertrainingsessionruntime.types.optimizer_step_config.deserialize_json(
                data["optimizerStep"]
            )
        }
    elif data.get("saveWeights") is not None:
        import capo_sagemakertrainingsessionruntime.types.save_weights_config

        return {
            "saveWeights": capo_sagemakertrainingsessionruntime.types.save_weights_config.deserialize_json(
                data["saveWeights"]
            )
        }
    elif data.get("saveState") is not None:
        import capo_sagemakertrainingsessionruntime.types.save_state_config

        return {
            "saveState": capo_sagemakertrainingsessionruntime.types.save_state_config.deserialize_json(
                data["saveState"]
            )
        }
    elif data.get("loadState") is not None:
        import capo_sagemakertrainingsessionruntime.types.load_state_config

        return {
            "loadState": capo_sagemakertrainingsessionruntime.types.load_state_config.deserialize_json(
                data["loadState"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("OperationConfig: no recognized variant key")


def redact_sensitive(value: OperationConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "forward" in value:
        import capo_sagemakertrainingsessionruntime.types.forward_config

        out["forward"] = (
            capo_sagemakertrainingsessionruntime.types.forward_config.redact_sensitive(
                value["forward"]
            )
        )
    if "forwardBackward" in value:
        import capo_sagemakertrainingsessionruntime.types.forward_backward_config

        out["forwardBackward"] = (
            capo_sagemakertrainingsessionruntime.types.forward_backward_config.redact_sensitive(
                value["forwardBackward"]
            )
        )
    return out
