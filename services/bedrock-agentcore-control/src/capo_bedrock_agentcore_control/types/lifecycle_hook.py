"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LifecycleHook``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.lifecycle_hook_action


class LifecycleHook(TypedDict, closed=True):
    action: (
        "capo_bedrock_agentcore_control.types.lifecycle_hook_action.LifecycleHookAction"
    )
    """<p>The action that AgentCore Runtime runs for the hook. Specify exactly one action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleHook) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.lifecycle_hook_action

    out["action"] = (
        capo_bedrock_agentcore_control.types.lifecycle_hook_action.serialize_json(
            value["action"]
        )
    )
    return out


def deserialize_json(data: dict) -> LifecycleHook:
    out: LifecycleHook = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_bedrock_agentcore_control.types.lifecycle_hook_action

        out["action"] = (
            capo_bedrock_agentcore_control.types.lifecycle_hook_action.deserialize_json(
                data["action"]
            )
        )
    else:
        out["action"] = {"$unknown": {"name": ""}}
    return out
