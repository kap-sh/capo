"""Generated from Smithy shape ``com.amazonaws.qbusiness#MediaExtractionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.audio_extraction_configuration
    import capo_qbusiness.types.image_extraction_configuration
    import capo_qbusiness.types.video_extraction_configuration


class MediaExtractionConfiguration(TypedDict, closed=True):
    image_extraction_configuration: NotRequired[
        "capo_qbusiness.types.image_extraction_configuration.ImageExtractionConfiguration"
    ]
    """<p>The configuration for extracting semantic meaning from images in documents. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/extracting-meaning-from-images.html">Extracting semantic meaning from images and visuals</a>. </p>"""
    audio_extraction_configuration: NotRequired[
        "capo_qbusiness.types.audio_extraction_configuration.AudioExtractionConfiguration"
    ]
    """<p>Configuration settings for extracting and processing audio content from media files.</p>"""
    video_extraction_configuration: NotRequired[
        "capo_qbusiness.types.video_extraction_configuration.VideoExtractionConfiguration"
    ]
    """<p>Configuration settings for extracting and processing video content from media files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaExtractionConfiguration) -> dict:
    out: dict = {}
    if "image_extraction_configuration" in value:
        import capo_qbusiness.types.image_extraction_configuration

        out["imageExtractionConfiguration"] = (
            capo_qbusiness.types.image_extraction_configuration.serialize_json(
                value["image_extraction_configuration"]
            )
        )
    if "audio_extraction_configuration" in value:
        import capo_qbusiness.types.audio_extraction_configuration

        out["audioExtractionConfiguration"] = (
            capo_qbusiness.types.audio_extraction_configuration.serialize_json(
                value["audio_extraction_configuration"]
            )
        )
    if "video_extraction_configuration" in value:
        import capo_qbusiness.types.video_extraction_configuration

        out["videoExtractionConfiguration"] = (
            capo_qbusiness.types.video_extraction_configuration.serialize_json(
                value["video_extraction_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaExtractionConfiguration:
    out: MediaExtractionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("imageExtractionConfiguration") is not None:
        import capo_qbusiness.types.image_extraction_configuration

        out["image_extraction_configuration"] = (
            capo_qbusiness.types.image_extraction_configuration.deserialize_json(
                data["imageExtractionConfiguration"]
            )
        )
    if data.get("audioExtractionConfiguration") is not None:
        import capo_qbusiness.types.audio_extraction_configuration

        out["audio_extraction_configuration"] = (
            capo_qbusiness.types.audio_extraction_configuration.deserialize_json(
                data["audioExtractionConfiguration"]
            )
        )
    if data.get("videoExtractionConfiguration") is not None:
        import capo_qbusiness.types.video_extraction_configuration

        out["video_extraction_configuration"] = (
            capo_qbusiness.types.video_extraction_configuration.deserialize_json(
                data["videoExtractionConfiguration"]
            )
        )
    return out
