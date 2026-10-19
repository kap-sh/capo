"""Generated from Smithy shape ``com.amazonaws.qbusiness#AudioExtractionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.audio_extraction_status


class AudioExtractionConfiguration(TypedDict, closed=True):
    audio_extraction_status: (
        "capo_qbusiness.types.audio_extraction_status.AudioExtractionStatus"
    )
    """<p>The status of audio extraction (ENABLED or DISABLED) for processing audio content from files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioExtractionConfiguration) -> dict:
    out: dict = {}
    import capo_qbusiness.types.audio_extraction_status

    out["audioExtractionStatus"] = (
        capo_qbusiness.types.audio_extraction_status.serialize_json(
            value["audio_extraction_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> AudioExtractionConfiguration:
    out: AudioExtractionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("audioExtractionStatus") is not None:
        import capo_qbusiness.types.audio_extraction_status

        out["audio_extraction_status"] = (
            capo_qbusiness.types.audio_extraction_status.deserialize_json(
                data["audioExtractionStatus"]
            )
        )
    else:
        import typing

        out["audio_extraction_status"] = typing.cast(
            "capo_qbusiness.types.audio_extraction_status.AudioExtractionStatus", ""
        )
    return out
