"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#Message``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.content_blocks
    import capo_bedrock_runtime.types.conversation_role


class Message(TypedDict, closed=True):
    role: "capo_bedrock_runtime.types.conversation_role.ConversationRole"
    """<p>The role that the message plays in the message.</p>"""
    content: "capo_bedrock_runtime.types.content_blocks.ContentBlocks"
    """<p>The message content. Note the following restrictions:</p> <ul> <li> <p>You can include up to 20 images. Each image's size, height, and width must be no more than 3.75 MB, 8000 px, and 8000 px, respectively.</p> </li> <li> <p>You can include up to five documents. Each document's size must be no more than 4.5 MB.</p> </li> <li> <p>If you include a <code>ContentBlock</code> with a <code>document</code> field in the array, you must also include a <code>ContentBlock</code> with a <code>text</code> field.</p> </li> <li> <p>You can only include images and documents if the <code>role</code> is <code>user</code>.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.conversation_role

    out["role"] = capo_bedrock_runtime.types.conversation_role.serialize_json(
        value["role"]
    )
    import capo_bedrock_runtime.types.content_blocks

    out["content"] = capo_bedrock_runtime.types.content_blocks.serialize_json(
        value["content"]
    )
    return out


def deserialize_json(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if data.get("role") is not None:
        import capo_bedrock_runtime.types.conversation_role

        out["role"] = capo_bedrock_runtime.types.conversation_role.deserialize_json(
            data["role"]
        )
    else:
        import typing

        out["role"] = typing.cast(
            "capo_bedrock_runtime.types.conversation_role.ConversationRole", ""
        )
    if data.get("content") is not None:
        import capo_bedrock_runtime.types.content_blocks

        out["content"] = capo_bedrock_runtime.types.content_blocks.deserialize_json(
            data["content"]
        )
    else:
        out["content"] = []
    return out


def redact_sensitive(value: Message) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_bedrock_runtime.types.content_blocks

        out["content"] = capo_bedrock_runtime.types.content_blocks.redact_sensitive(
            value["content"]
        )
    return out
