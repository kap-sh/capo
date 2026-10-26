"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessBeforeToolCallHook``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_hook_name
    import capo_bedrock_agentcore_control.types.harness_hook_target


class HarnessBeforeToolCallHook(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.harness_hook_name.HarnessHookName"
    """<p>The name of the hook.</p>"""
    target: "capo_bedrock_agentcore_control.types.harness_hook_target.HarnessHookTarget"
    """<p>The target that receives the hook event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessBeforeToolCallHook) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_bedrock_agentcore_control.types.harness_hook_target

    out["target"] = (
        capo_bedrock_agentcore_control.types.harness_hook_target.serialize_json(
            value["target"]
        )
    )
    return out


def deserialize_json(data: dict) -> HarnessBeforeToolCallHook:
    out: HarnessBeforeToolCallHook = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("target") is not None:
        import capo_bedrock_agentcore_control.types.harness_hook_target

        out["target"] = (
            capo_bedrock_agentcore_control.types.harness_hook_target.deserialize_json(
                data["target"]
            )
        )
    else:
        out["target"] = {"$unknown": {"name": ""}}
    return out
