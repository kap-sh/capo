"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RuntimeHooksConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.build_lifecycle_hooks


class RuntimeHooksConfiguration(TypedDict, closed=True):
    build: NotRequired[
        "capo_bedrock_agentcore_control.types.build_lifecycle_hooks.BuildLifecycleHooks"
    ]
    """<p>The hooks that run when you create or update the AgentCore Runtime, before any sessions are created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeHooksConfiguration) -> dict:
    out: dict = {}
    if "build" in value:
        import capo_bedrock_agentcore_control.types.build_lifecycle_hooks

        out["build"] = (
            capo_bedrock_agentcore_control.types.build_lifecycle_hooks.serialize_json(
                value["build"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuntimeHooksConfiguration:
    out: RuntimeHooksConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("build") is not None:
        import capo_bedrock_agentcore_control.types.build_lifecycle_hooks

        out["build"] = (
            capo_bedrock_agentcore_control.types.build_lifecycle_hooks.deserialize_json(
                data["build"]
            )
        )
    return out
