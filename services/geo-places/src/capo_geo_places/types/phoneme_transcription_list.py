"""Generated from Smithy shape ``com.amazonaws.geoplaces#PhonemeTranscriptionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.phoneme_transcription

PhonemeTranscriptionList: TypeAlias = list[
    "capo_geo_places.types.phoneme_transcription.PhonemeTranscription"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhonemeTranscriptionList) -> list:
    import capo_geo_places.types.phoneme_transcription

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.phoneme_transcription.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhonemeTranscriptionList:
    import capo_geo_places.types.phoneme_transcription

    out: PhonemeTranscriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_places.types.phoneme_transcription.deserialize_json(item))
    return out


def redact_sensitive(value: PhonemeTranscriptionList) -> list[Any]:
    import capo_geo_places.types.phoneme_transcription

    return [
        capo_geo_places.types.phoneme_transcription.redact_sensitive(item)
        for item in value
    ]
