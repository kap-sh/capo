"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ImageExtractionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.enabled_or_disabled_state


class ImageExtractionConfiguration(TypedDict, closed=True):
    image_extraction_status: (
        "capo_bedrock_agent.types.enabled_or_disabled_state.EnabledOrDisabledState"
    )
    """<p>Whether image extraction is enabled or disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageExtractionConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.enabled_or_disabled_state

    out["imageExtractionStatus"] = (
        capo_bedrock_agent.types.enabled_or_disabled_state.serialize_json(
            value["image_extraction_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> ImageExtractionConfiguration:
    out: ImageExtractionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("imageExtractionStatus") is not None:
        import capo_bedrock_agent.types.enabled_or_disabled_state

        out["image_extraction_status"] = (
            capo_bedrock_agent.types.enabled_or_disabled_state.deserialize_json(
                data["imageExtractionStatus"]
            )
        )
    else:
        import typing

        out["image_extraction_status"] = typing.cast(
            "capo_bedrock_agent.types.enabled_or_disabled_state.EnabledOrDisabledState",
            "",
        )
    return out
