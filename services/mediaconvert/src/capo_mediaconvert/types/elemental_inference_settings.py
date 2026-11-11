"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ElementalInferenceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.elemental_inference_feed_configuration_source


class ElementalInferenceSettings(TypedDict, closed=True):
    feed_configuration_source: NotRequired[
        "capo_mediaconvert.types.elemental_inference_feed_configuration_source.ElementalInferenceFeedConfigurationSource"
    ]
    """Optional. The source of your Elemental Inference Feed configuration. MediaConvert will reference this configuration source when you specify job settings which use Elemental Inference."""


# --- restJson1 ser/de ---
def serialize_json(value: ElementalInferenceSettings) -> dict:
    out: dict = {}
    if "feed_configuration_source" in value:
        import capo_mediaconvert.types.elemental_inference_feed_configuration_source

        out["feedConfigurationSource"] = (
            capo_mediaconvert.types.elemental_inference_feed_configuration_source.serialize_json(
                value["feed_configuration_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> ElementalInferenceSettings:
    out: ElementalInferenceSettings = {}  # type: ignore[typeddict-item]
    if data.get("feedConfigurationSource") is not None:
        import capo_mediaconvert.types.elemental_inference_feed_configuration_source

        out["feed_configuration_source"] = (
            capo_mediaconvert.types.elemental_inference_feed_configuration_source.deserialize_json(
                data["feedConfigurationSource"]
            )
        )
    return out
