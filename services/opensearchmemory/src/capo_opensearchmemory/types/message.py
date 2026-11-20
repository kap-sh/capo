"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#Message``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_opensearchmemory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchmemory.types.message_content
    import capo_opensearchmemory.types.message_role


class Message(TypedDict, closed=True):
    role: "capo_opensearchmemory.types.message_role.MessageRole"
    """<p>The author of the turn.</p>"""
    content: "capo_opensearchmemory.types.message_content.MessageContent"
    """<p>The content of the turn.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Message) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.message_role

    out["role"] = capo_opensearchmemory.types.message_role.serialize_aws_json_1_0(
        value["role"]
    )
    import capo_opensearchmemory.types.message_content

    out["content"] = capo_opensearchmemory.types.message_content.serialize_aws_json_1_0(
        value["content"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if data.get("role") is not None:
        import capo_opensearchmemory.types.message_role

        out["role"] = capo_opensearchmemory.types.message_role.deserialize_aws_json_1_0(
            data["role"]
        )
    else:
        import typing

        out["role"] = typing.cast(
            "capo_opensearchmemory.types.message_role.MessageRole", ""
        )
    if data.get("content") is not None:
        import capo_opensearchmemory.types.message_content

        out["content"] = (
            capo_opensearchmemory.types.message_content.deserialize_aws_json_1_0(
                data["content"]
            )
        )
    else:
        raise DeserializationError("Message.content required")
    return out


def redact_sensitive(value: Message) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_opensearchmemory.types.message_content

        out["content"] = capo_opensearchmemory.types.message_content.redact_sensitive(
            value["content"]
        )
    return out
