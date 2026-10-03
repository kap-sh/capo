"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdConditioningConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.streaming_media_file_conditioning


class AdConditioningConfiguration(TypedDict, closed=True):
    streaming_media_file_conditioning: "capo_mediatailor.types.streaming_media_file_conditioning.StreamingMediaFileConditioning"
    """<p>For ads that have media files with streaming delivery and supported file extensions, indicates what transcoding action MediaTailor takes when it first receives these ads from the ADS. <code>TRANSCODE</code> indicates that MediaTailor must transcode the ads. <code>NONE</code> indicates that you have already transcoded the ads outside of MediaTailor and don't need them transcoded as part of the ad insertion workflow. For more information about ad conditioning see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/precondition-ads.html">Using preconditioned ads</a> in the Elemental MediaTailor user guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdConditioningConfiguration) -> dict:
    out: dict = {}
    import capo_mediatailor.types.streaming_media_file_conditioning

    out["StreamingMediaFileConditioning"] = (
        capo_mediatailor.types.streaming_media_file_conditioning.serialize_json(
            value["streaming_media_file_conditioning"]
        )
    )
    return out


def deserialize_json(data: dict) -> AdConditioningConfiguration:
    out: AdConditioningConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("StreamingMediaFileConditioning") is not None:
        import capo_mediatailor.types.streaming_media_file_conditioning

        out["streaming_media_file_conditioning"] = (
            capo_mediatailor.types.streaming_media_file_conditioning.deserialize_json(
                data["StreamingMediaFileConditioning"]
            )
        )
    else:
        raise DeserializationError(
            "AdConditioningConfiguration.streaming_media_file_conditioning required"
        )
    return out
