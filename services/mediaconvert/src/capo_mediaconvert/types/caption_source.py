"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CaptionSource``."""

from typing import Literal, TypeAlias, cast

"""Specify the source of the captions for this caption description. Choose Captions input source (INPUT_CAPTION_SELECTOR) to use a caption selector from your input. Choose Smart subtitling (SMART_SUBTITLE) to have MediaConvert and Elemental Inference generate subtitles automatically from an audio source that you specify."""
CaptionSource: TypeAlias = Literal[
    "INPUT_CAPTION_SELECTOR",
    "SMART_SUBTITLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CaptionSource) -> str:
    return value


def deserialize_json(data: str) -> CaptionSource:
    return cast(CaptionSource, data)
