"""Generated from Smithy shape ``com.amazonaws.mediaconvert#FontScript``."""

from typing import Literal, TypeAlias, cast

"""Provide the font script, using an ISO 15924 script code, if the LanguageCode is not sufficient for determining the script type. Where LanguageCode or CustomLanguageCode is sufficient, use "AUTOMATIC" or leave unset."""
FontScript: TypeAlias = Literal[
    "AUTOMATIC",
    "HANS",
    "HANT",
]


# --- restJson1 ser/de ---
def serialize_json(value: FontScript) -> str:
    return value


def deserialize_json(data: str) -> FontScript:
    return cast(FontScript, data)
