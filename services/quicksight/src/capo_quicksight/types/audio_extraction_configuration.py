"""Generated from Smithy shape ``com.amazonaws.quicksight#AudioExtractionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.audio_extraction_status


class AudioExtractionConfiguration(TypedDict, closed=True):
    audio_extraction_status: (
        "capo_quicksight.types.audio_extraction_status.AudioExtractionStatus"
    )
    """<p>The status of audio extraction. Valid values are ENABLED and DISABLED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioExtractionConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.audio_extraction_status

    out["audioExtractionStatus"] = (
        capo_quicksight.types.audio_extraction_status.serialize_json(
            value["audio_extraction_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> AudioExtractionConfiguration:
    out: AudioExtractionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("audioExtractionStatus") is not None:
        import capo_quicksight.types.audio_extraction_status

        out["audio_extraction_status"] = (
            capo_quicksight.types.audio_extraction_status.deserialize_json(
                data["audioExtractionStatus"]
            )
        )
    else:
        import typing

        out["audio_extraction_status"] = typing.cast(
            "capo_quicksight.types.audio_extraction_status.AudioExtractionStatus", ""
        )
    return out
