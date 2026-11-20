"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#AssetLanguage``."""

from typing import Literal, TypeAlias, cast

"""A language a campaign is written and typeset in, as a BCP 47 tag. <p>A closed set rather than a free string: each value is one DG can render, and a document needs a font for it, so a tag outside the set could not be honoured."""
AssetLanguage: TypeAlias = Literal[
    "en",
    "es",
    "es-419",
    "fr",
    "de",
    "it",
    "pt-BR",
    "id",
    "tr",
    "ja",
    "ko",
    "zh-Hans",
    "zh-Hant",
    "ar",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssetLanguage) -> str:
    return value


def deserialize_cbor(data: str) -> AssetLanguage:
    return cast(AssetLanguage, data)
