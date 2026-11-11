"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BuildLifecycleHooks``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.lifecycle_hook


class BuildLifecycleHooks(TypedDict, closed=True):
    warmup: NotRequired[
        "capo_bedrock_agentcore_control.types.lifecycle_hook.LifecycleHook"
    ]
    """<p>The hook that warms up your agent before any sessions are created. Use this hook to load the resources that your sessions need, such as models, libraries, or caches. Your hook must complete within 120 seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BuildLifecycleHooks) -> dict:
    out: dict = {}
    if "warmup" in value:
        import capo_bedrock_agentcore_control.types.lifecycle_hook

        out["warmup"] = (
            capo_bedrock_agentcore_control.types.lifecycle_hook.serialize_json(
                value["warmup"]
            )
        )
    return out


def deserialize_json(data: dict) -> BuildLifecycleHooks:
    out: BuildLifecycleHooks = {}  # type: ignore[typeddict-item]
    if data.get("warmup") is not None:
        import capo_bedrock_agentcore_control.types.lifecycle_hook

        out["warmup"] = (
            capo_bedrock_agentcore_control.types.lifecycle_hook.deserialize_json(
                data["warmup"]
            )
        )
    return out
