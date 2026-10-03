"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#KeyShortcutArguments``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.key_list


class KeyShortcutArguments(TypedDict, closed=True):
    keys: "capo_bedrock_agentcore.types.key_list.KeyList"
    """<p>The key combination to press (for example, <code>["ctrl", "s"]</code>). Maximum 5 keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyShortcutArguments) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.key_list

    out["keys"] = capo_bedrock_agentcore.types.key_list.serialize_json(value["keys"])
    return out


def deserialize_json(data: dict) -> KeyShortcutArguments:
    out: KeyShortcutArguments = {}  # type: ignore[typeddict-item]
    if data.get("keys") is not None:
        import capo_bedrock_agentcore.types.key_list

        out["keys"] = capo_bedrock_agentcore.types.key_list.deserialize_json(
            data["keys"]
        )
    else:
        raise DeserializationError("KeyShortcutArguments.keys required")
    return out
