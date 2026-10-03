"""Generated from Smithy shape ``com.amazonaws.geoplaces#PhonemeTranscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.language_tag
    import capo_geo_places.types.sensitive_boolean
    import capo_geo_places.types.sensitive_string


class PhonemeTranscription(TypedDict, closed=True):
    value: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>Value which indicates how to pronounce the value.</p>"""
    language: NotRequired["capo_geo_places.types.language_tag.LanguageTag"]
    """<p>A list of <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.</p>"""
    preferred: NotRequired["capo_geo_places.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Boolean which indicates if it the preferred pronunciation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhonemeTranscription) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "language" in value:
        out["Language"] = value["language"]
    if "preferred" in value:
        out["Preferred"] = value["preferred"]
    return out


def deserialize_json(data: dict) -> PhonemeTranscription:
    out: PhonemeTranscription = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    if data.get("Preferred") is not None:
        out["preferred"] = data["Preferred"]
    return out
