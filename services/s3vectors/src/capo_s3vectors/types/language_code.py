"""Generated from Smithy shape ``com.amazonaws.s3vectors#LanguageCode``."""

from typing import Literal, TypeAlias, cast

"""<p>The analysis language for a text search analyzer. Valid values are <code>en</code> (English), <code>fr</code> (French), <code>es</code> (Spanish), <code>pt</code> (Portuguese), <code>it</code> (Italian), <code>de</code> (German), <code>nl</code> (Dutch), <code>zh</code> (Chinese), <code>ja</code> (Japanese), and <code>ko</code> (Korean).</p>"""
LanguageCode: TypeAlias = Literal[
    "en",
    "fr",
    "es",
    "pt",
    "it",
    "de",
    "nl",
    "zh",
    "ja",
    "ko",
]


# --- restJson1 ser/de ---
def serialize_json(value: LanguageCode) -> str:
    return value


def deserialize_json(data: str) -> LanguageCode:
    return cast(LanguageCode, data)
