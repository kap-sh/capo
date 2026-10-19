"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AudioExtractionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.enabled_or_disabled_state


class AudioExtractionConfiguration(TypedDict, closed=True):
    audio_extraction_status: (
        "capo_bedrock_agent.types.enabled_or_disabled_state.EnabledOrDisabledState"
    )
    """<p>Whether audio extraction is enabled or disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioExtractionConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.enabled_or_disabled_state

    out["audioExtractionStatus"] = (
        capo_bedrock_agent.types.enabled_or_disabled_state.serialize_json(
            value["audio_extraction_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> AudioExtractionConfiguration:
    out: AudioExtractionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("audioExtractionStatus") is not None:
        import capo_bedrock_agent.types.enabled_or_disabled_state

        out["audio_extraction_status"] = (
            capo_bedrock_agent.types.enabled_or_disabled_state.deserialize_json(
                data["audioExtractionStatus"]
            )
        )
    else:
        import typing

        out["audio_extraction_status"] = typing.cast(
            "capo_bedrock_agent.types.enabled_or_disabled_state.EnabledOrDisabledState",
            "",
        )
    return out
