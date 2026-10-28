"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessHook``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_after_invocation_hook
    import capo_bedrock_agentcore_control.types.harness_after_tool_call_hook
    import capo_bedrock_agentcore_control.types.harness_before_invocation_hook
    import capo_bedrock_agentcore_control.types.harness_before_tool_call_hook


class HarnessHookBeforeInvocationMember(TypedDict, closed=True):
    beforeInvocation: "capo_bedrock_agentcore_control.types.harness_before_invocation_hook.HarnessBeforeInvocationHook"


class HarnessHookAfterInvocationMember(TypedDict, closed=True):
    afterInvocation: "capo_bedrock_agentcore_control.types.harness_after_invocation_hook.HarnessAfterInvocationHook"


class HarnessHookBeforeToolCallMember(TypedDict, closed=True):
    beforeToolCall: "capo_bedrock_agentcore_control.types.harness_before_tool_call_hook.HarnessBeforeToolCallHook"


class HarnessHookAfterToolCallMember(TypedDict, closed=True):
    afterToolCall: "capo_bedrock_agentcore_control.types.harness_after_tool_call_hook.HarnessAfterToolCallHook"


HarnessHook: TypeAlias = (
    HarnessHookBeforeInvocationMember
    | HarnessHookAfterInvocationMember
    | HarnessHookBeforeToolCallMember
    | HarnessHookAfterToolCallMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessHook) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"HarnessHook: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "beforeInvocation" in value:
        import capo_bedrock_agentcore_control.types.harness_before_invocation_hook

        return {
            "beforeInvocation": capo_bedrock_agentcore_control.types.harness_before_invocation_hook.serialize_json(
                value["beforeInvocation"]
            )
        }
    elif "afterInvocation" in value:
        import capo_bedrock_agentcore_control.types.harness_after_invocation_hook

        return {
            "afterInvocation": capo_bedrock_agentcore_control.types.harness_after_invocation_hook.serialize_json(
                value["afterInvocation"]
            )
        }
    elif "beforeToolCall" in value:
        import capo_bedrock_agentcore_control.types.harness_before_tool_call_hook

        return {
            "beforeToolCall": capo_bedrock_agentcore_control.types.harness_before_tool_call_hook.serialize_json(
                value["beforeToolCall"]
            )
        }
    elif "afterToolCall" in value:
        import capo_bedrock_agentcore_control.types.harness_after_tool_call_hook

        return {
            "afterToolCall": capo_bedrock_agentcore_control.types.harness_after_tool_call_hook.serialize_json(
                value["afterToolCall"]
            )
        }
    else:
        raise SerializationError("HarnessHook: no variant present")


def deserialize_json(data: dict) -> HarnessHook:
    if data.get("beforeInvocation") is not None:
        import capo_bedrock_agentcore_control.types.harness_before_invocation_hook

        return {
            "beforeInvocation": capo_bedrock_agentcore_control.types.harness_before_invocation_hook.deserialize_json(
                data["beforeInvocation"]
            )
        }
    elif data.get("afterInvocation") is not None:
        import capo_bedrock_agentcore_control.types.harness_after_invocation_hook

        return {
            "afterInvocation": capo_bedrock_agentcore_control.types.harness_after_invocation_hook.deserialize_json(
                data["afterInvocation"]
            )
        }
    elif data.get("beforeToolCall") is not None:
        import capo_bedrock_agentcore_control.types.harness_before_tool_call_hook

        return {
            "beforeToolCall": capo_bedrock_agentcore_control.types.harness_before_tool_call_hook.deserialize_json(
                data["beforeToolCall"]
            )
        }
    elif data.get("afterToolCall") is not None:
        import capo_bedrock_agentcore_control.types.harness_after_tool_call_hook

        return {
            "afterToolCall": capo_bedrock_agentcore_control.types.harness_after_tool_call_hook.deserialize_json(
                data["afterToolCall"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("HarnessHook: no recognized variant key")
