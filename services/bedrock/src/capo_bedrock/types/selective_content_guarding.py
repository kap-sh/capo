"""Generated from Smithy shape ``com.amazonaws.bedrock#SelectiveContentGuarding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.selective_guarding_mode


class SelectiveContentGuarding(TypedDict, closed=True):
    system: NotRequired[
        "capo_bedrock.types.selective_guarding_mode.SelectiveGuardingMode"
    ]
    """<p>Selective guarding mode for system prompts."</p>"""
    messages: NotRequired[
        "capo_bedrock.types.selective_guarding_mode.SelectiveGuardingMode"
    ]
    """<p>Selective guarding mode for user messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelectiveContentGuarding) -> dict:
    out: dict = {}
    if "system" in value:
        import capo_bedrock.types.selective_guarding_mode

        out["system"] = capo_bedrock.types.selective_guarding_mode.serialize_json(
            value["system"]
        )
    if "messages" in value:
        import capo_bedrock.types.selective_guarding_mode

        out["messages"] = capo_bedrock.types.selective_guarding_mode.serialize_json(
            value["messages"]
        )
    return out


def deserialize_json(data: dict) -> SelectiveContentGuarding:
    out: SelectiveContentGuarding = {}  # type: ignore[typeddict-item]
    if data.get("system") is not None:
        import capo_bedrock.types.selective_guarding_mode

        out["system"] = capo_bedrock.types.selective_guarding_mode.deserialize_json(
            data["system"]
        )
    if data.get("messages") is not None:
        import capo_bedrock.types.selective_guarding_mode

        out["messages"] = capo_bedrock.types.selective_guarding_mode.deserialize_json(
            data["messages"]
        )
    return out
