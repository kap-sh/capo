"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessHookTarget``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_hook_event_bridge_target
    import capo_bedrock_agentcore_control.types.harness_hook_lambda_target
    import capo_bedrock_agentcore_control.types.harness_hook_sns_target

_HarnessHookTarget_lambda = TypedDict(
    "_HarnessHookTarget_lambda",
    {
        "lambda": "capo_bedrock_agentcore_control.types.harness_hook_lambda_target.HarnessHookLambdaTarget",
    },
    closed=True,
)


class _HarnessHookTarget_sns(TypedDict, closed=True):
    sns: "capo_bedrock_agentcore_control.types.harness_hook_sns_target.HarnessHookSnsTarget"


class _HarnessHookTarget_eventBridge(TypedDict, closed=True):
    eventBridge: "capo_bedrock_agentcore_control.types.harness_hook_event_bridge_target.HarnessHookEventBridgeTarget"


HarnessHookTarget: TypeAlias = (
    _HarnessHookTarget_lambda
    | _HarnessHookTarget_sns
    | _HarnessHookTarget_eventBridge
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessHookTarget) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"HarnessHookTarget: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "lambda" in value:
        import capo_bedrock_agentcore_control.types.harness_hook_lambda_target

        return {
            "lambda": capo_bedrock_agentcore_control.types.harness_hook_lambda_target.serialize_json(
                value["lambda"]
            )
        }
    elif "sns" in value:
        import capo_bedrock_agentcore_control.types.harness_hook_sns_target

        return {
            "sns": capo_bedrock_agentcore_control.types.harness_hook_sns_target.serialize_json(
                value["sns"]
            )
        }
    elif "eventBridge" in value:
        import capo_bedrock_agentcore_control.types.harness_hook_event_bridge_target

        return {
            "eventBridge": capo_bedrock_agentcore_control.types.harness_hook_event_bridge_target.serialize_json(
                value["eventBridge"]
            )
        }
    else:
        raise SerializationError("HarnessHookTarget: no variant present")


def deserialize_json(data: dict) -> HarnessHookTarget:
    if data.get("lambda") is not None:
        import capo_bedrock_agentcore_control.types.harness_hook_lambda_target

        return {
            "lambda": capo_bedrock_agentcore_control.types.harness_hook_lambda_target.deserialize_json(
                data["lambda"]
            )
        }
    elif data.get("sns") is not None:
        import capo_bedrock_agentcore_control.types.harness_hook_sns_target

        return {
            "sns": capo_bedrock_agentcore_control.types.harness_hook_sns_target.deserialize_json(
                data["sns"]
            )
        }
    elif data.get("eventBridge") is not None:
        import capo_bedrock_agentcore_control.types.harness_hook_event_bridge_target

        return {
            "eventBridge": capo_bedrock_agentcore_control.types.harness_hook_event_bridge_target.deserialize_json(
                data["eventBridge"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("HarnessHookTarget: no recognized variant key")
