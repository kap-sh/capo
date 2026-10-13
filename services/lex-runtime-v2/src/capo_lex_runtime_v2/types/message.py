"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#Message``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.image_response_card
    import capo_lex_runtime_v2.types.message_content_type
    import capo_lex_runtime_v2.types.text


class Message(TypedDict, closed=True):
    content: NotRequired["capo_lex_runtime_v2.types.text.Text"]
    """<p>The text of the message.</p>"""
    content_type: "capo_lex_runtime_v2.types.message_content_type.MessageContentType"
    """<p>Indicates the type of response.</p>"""
    image_response_card: NotRequired[
        "capo_lex_runtime_v2.types.image_response_card.ImageResponseCard"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    out: dict = {}
    if "content" in value:
        out["content"] = value["content"]
    import capo_lex_runtime_v2.types.message_content_type

    out["contentType"] = capo_lex_runtime_v2.types.message_content_type.serialize_json(
        value["content_type"]
    )
    if "image_response_card" in value:
        import capo_lex_runtime_v2.types.image_response_card

        out["imageResponseCard"] = (
            capo_lex_runtime_v2.types.image_response_card.serialize_json(
                value["image_response_card"]
            )
        )
    return out


def deserialize_json(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        out["content"] = data["content"]
    if data.get("contentType") is not None:
        import capo_lex_runtime_v2.types.message_content_type

        out["content_type"] = (
            capo_lex_runtime_v2.types.message_content_type.deserialize_json(
                data["contentType"]
            )
        )
    else:
        raise DeserializationError("Message.content_type required")
    if data.get("imageResponseCard") is not None:
        import capo_lex_runtime_v2.types.image_response_card

        out["image_response_card"] = (
            capo_lex_runtime_v2.types.image_response_card.deserialize_json(
                data["imageResponseCard"]
            )
        )
    return out


def redact_sensitive(value: Message) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out
