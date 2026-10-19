"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ContentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.content_level
    import capo_bedrock_agentcore_control.types.content_type


class ContentConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agentcore_control.types.content_type.ContentType"
    """<p>Type of content to stream.</p>"""
    level: "capo_bedrock_agentcore_control.types.content_level.ContentLevel"
    """<p>Level of detail for streamed content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.content_type

    out["type"] = capo_bedrock_agentcore_control.types.content_type.serialize_json(
        value["type"]
    )
    import capo_bedrock_agentcore_control.types.content_level

    out["level"] = capo_bedrock_agentcore_control.types.content_level.serialize_json(
        value.get("level", "METADATA_ONLY")
    )
    return out


def deserialize_json(data: dict) -> ContentConfiguration:
    out: ContentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agentcore_control.types.content_type

        out["type"] = (
            capo_bedrock_agentcore_control.types.content_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agentcore_control.types.content_type.ContentType", ""
        )
    if data.get("level") is not None:
        import capo_bedrock_agentcore_control.types.content_level

        out["level"] = (
            capo_bedrock_agentcore_control.types.content_level.deserialize_json(
                data["level"]
            )
        )
    else:
        out["level"] = "METADATA_ONLY"
    return out
