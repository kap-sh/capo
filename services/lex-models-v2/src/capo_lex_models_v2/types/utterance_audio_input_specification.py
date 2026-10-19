"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceAudioInputSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.audio_file_s3_location


class UtteranceAudioInputSpecification(TypedDict, closed=True):
    audio_file_s3_location: (
        "capo_lex_models_v2.types.audio_file_s3_location.AudioFileS3Location"
    )
    """<p>Amazon S3 file pointing to the audio.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceAudioInputSpecification) -> dict:
    out: dict = {}
    out["audioFileS3Location"] = value["audio_file_s3_location"]
    return out


def deserialize_json(data: dict) -> UtteranceAudioInputSpecification:
    out: UtteranceAudioInputSpecification = {}  # type: ignore[typeddict-item]
    if data.get("audioFileS3Location") is not None:
        out["audio_file_s3_location"] = data["audioFileS3Location"]
    else:
        out["audio_file_s3_location"] = ""
    return out
