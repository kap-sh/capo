"""Generated from Smithy shape ``com.amazonaws.bedrockagent#InlineContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.byte_content_doc
    import capo_bedrock_agent.types.inline_content_type
    import capo_bedrock_agent.types.text_content_doc


class InlineContent(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.inline_content_type.InlineContentType"
    """<p>The type of inline content to define.</p>"""
    byte_content: NotRequired[
        "capo_bedrock_agent.types.byte_content_doc.ByteContentDoc"
    ]
    """<p>Contains information about content defined inline in bytes.</p>"""
    text_content: NotRequired[
        "capo_bedrock_agent.types.text_content_doc.TextContentDoc"
    ]
    """<p>Contains information about content defined inline in text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineContent) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.inline_content_type

    out["type"] = capo_bedrock_agent.types.inline_content_type.serialize_json(
        value["type"]
    )
    if "byte_content" in value:
        import capo_bedrock_agent.types.byte_content_doc

        out["byteContent"] = capo_bedrock_agent.types.byte_content_doc.serialize_json(
            value["byte_content"]
        )
    if "text_content" in value:
        import capo_bedrock_agent.types.text_content_doc

        out["textContent"] = capo_bedrock_agent.types.text_content_doc.serialize_json(
            value["text_content"]
        )
    return out


def deserialize_json(data: dict) -> InlineContent:
    out: InlineContent = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent.types.inline_content_type

        out["type"] = capo_bedrock_agent.types.inline_content_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent.types.inline_content_type.InlineContentType", ""
        )
    if data.get("byteContent") is not None:
        import capo_bedrock_agent.types.byte_content_doc

        out["byte_content"] = (
            capo_bedrock_agent.types.byte_content_doc.deserialize_json(
                data["byteContent"]
            )
        )
    if data.get("textContent") is not None:
        import capo_bedrock_agent.types.text_content_doc

        out["text_content"] = (
            capo_bedrock_agent.types.text_content_doc.deserialize_json(
                data["textContent"]
            )
        )
    return out


def redact_sensitive(value: InlineContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "byte_content" in value:
        import capo_bedrock_agent.types.byte_content_doc

        out["byte_content"] = (
            capo_bedrock_agent.types.byte_content_doc.redact_sensitive(
                value["byte_content"]
            )
        )
    if "text_content" in value:
        import capo_bedrock_agent.types.text_content_doc

        out["text_content"] = (
            capo_bedrock_agent.types.text_content_doc.redact_sensitive(
                value["text_content"]
            )
        )
    return out
