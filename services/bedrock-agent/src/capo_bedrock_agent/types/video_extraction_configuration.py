"""Generated from Smithy shape ``com.amazonaws.bedrockagent#VideoExtractionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.enabled_or_disabled_state


class VideoExtractionConfiguration(TypedDict, closed=True):
    video_extraction_status: (
        "capo_bedrock_agent.types.enabled_or_disabled_state.EnabledOrDisabledState"
    )
    """<p>Whether video extraction is enabled or disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoExtractionConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.enabled_or_disabled_state

    out["videoExtractionStatus"] = (
        capo_bedrock_agent.types.enabled_or_disabled_state.serialize_json(
            value["video_extraction_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> VideoExtractionConfiguration:
    out: VideoExtractionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("videoExtractionStatus") is not None:
        import capo_bedrock_agent.types.enabled_or_disabled_state

        out["video_extraction_status"] = (
            capo_bedrock_agent.types.enabled_or_disabled_state.deserialize_json(
                data["videoExtractionStatus"]
            )
        )
    else:
        import typing

        out["video_extraction_status"] = typing.cast(
            "capo_bedrock_agent.types.enabled_or_disabled_state.EnabledOrDisabledState",
            "",
        )
    return out
