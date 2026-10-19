"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ResourceContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.resource_content_type


class ResourceContent(TypedDict, closed=True):
    type: "capo_bedrock_agentcore.types.resource_content_type.ResourceContentType"
    """<p>The type of resource content.</p>"""
    uri: NotRequired["str"]
    """<p>The URI of the resource content.</p>"""
    mime_type: NotRequired["str"]
    """<p>The MIME type of the resource content.</p>"""
    text: NotRequired["str"]
    """<p>The text resource content.</p>"""
    blob: NotRequired["bytes"]
    """<p>The binary resource content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceContent) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.resource_content_type

    out["type"] = capo_bedrock_agentcore.types.resource_content_type.serialize_json(
        value["type"]
    )
    if "uri" in value:
        out["uri"] = value["uri"]
    if "mime_type" in value:
        out["mimeType"] = value["mime_type"]
    if "text" in value:
        out["text"] = value["text"]
    if "blob" in value:
        import capo_bedrock_agentcore.types._prelude.blob

        out["blob"] = capo_bedrock_agentcore.types._prelude.blob.serialize_json(
            value["blob"]
        )
    return out


def deserialize_json(data: dict) -> ResourceContent:
    out: ResourceContent = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agentcore.types.resource_content_type

        out["type"] = (
            capo_bedrock_agentcore.types.resource_content_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agentcore.types.resource_content_type.ResourceContentType", ""
        )
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    if data.get("mimeType") is not None:
        out["mime_type"] = data["mimeType"]
    if data.get("text") is not None:
        out["text"] = data["text"]
    if data.get("blob") is not None:
        import capo_bedrock_agentcore.types._prelude.blob

        out["blob"] = capo_bedrock_agentcore.types._prelude.blob.deserialize_json(
            data["blob"]
        )
    return out
