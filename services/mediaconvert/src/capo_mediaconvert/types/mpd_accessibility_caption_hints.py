"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MpdAccessibilityCaptionHints``."""

from typing import Literal, TypeAlias, cast

"""Optional. Choose Include to have MediaConvert mark up your DASH manifest with <Accessibility> elements for embedded 608 captions. This markup isn't generally required, but some video players require it to discover and play embedded 608 captions. Keep the default value, Exclude, to leave these elements out. When you enable this setting, this is the markup that MediaConvert includes in your manifest: <Accessibility schemeIdUri="urn:scte:dash:cc:cea-608:2015" value="CC1=eng"/>"""
MpdAccessibilityCaptionHints: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MpdAccessibilityCaptionHints) -> str:
    return value


def deserialize_json(data: str) -> MpdAccessibilityCaptionHints:
    return cast(MpdAccessibilityCaptionHints, data)
