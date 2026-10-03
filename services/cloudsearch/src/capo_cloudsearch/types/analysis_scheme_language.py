"""Generated from Smithy shape ``com.amazonaws.cloudsearch#AnalysisSchemeLanguage``."""

from typing import Literal, TypeAlias, cast

from capo_cloudsearch._protocol.xml import Element

"""<p>An <a href="http://tools.ietf.org/html/rfc4646" target="_blank">IETF RFC 4646</a> language code or <code>mul</code> for multiple languages.</p>"""
AnalysisSchemeLanguage: TypeAlias = Literal[
    "ar",
    "bg",
    "ca",
    "cs",
    "da",
    "de",
    "el",
    "en",
    "es",
    "eu",
    "fa",
    "fi",
    "fr",
    "ga",
    "gl",
    "he",
    "hi",
    "hu",
    "hy",
    "id",
    "it",
    "ja",
    "ko",
    "lv",
    "mul",
    "nl",
    "no",
    "pt",
    "ro",
    "ru",
    "sv",
    "th",
    "tr",
    "zh-Hans",
    "zh-Hant",
]


# --- awsQuery ser/de ---
def to_query_text(value: AnalysisSchemeLanguage) -> str:
    return value


def from_query_text(text: str) -> AnalysisSchemeLanguage:
    return cast(AnalysisSchemeLanguage, text)


def serialize_query(
    value: AnalysisSchemeLanguage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AnalysisSchemeLanguage:
    return from_query_text(el.text or "")
