"""Generated from Smithy shape ``com.amazonaws.geoplaces#TranslationName``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_places.types.language_tag
    import capo_geo_places.types.sensitive_boolean
    import capo_geo_places.types.sensitive_string
    import capo_geo_places.types.translation_name_type


class TranslationName(TypedDict, closed=True):
    value: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The translated or alternative name value.</p>"""
    language: NotRequired["capo_geo_places.types.language_tag.LanguageTag"]
    """<p>A <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">BCP 47</a> compliant language code for the translation name.</p>"""
    type: "capo_geo_places.types.translation_name_type.TranslationNameType"
    """<p>The type of translation name. Valid values are <code>Abbreviation</code>, <code>AreaCode</code>, <code>BaseName</code>, <code>Exonym</code>, <code>Shortened</code>, and <code>Synonym</code>.</p>"""
    primary: NotRequired["capo_geo_places.types.sensitive_boolean.SensitiveBoolean"]
    """<p>If <code>true</code>, indicates this is the primary name variant for the given language.</p>"""
    transliterated: NotRequired[
        "capo_geo_places.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>If <code>true</code>, indicates this name is a transliterated version rather than a native script translation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranslationName) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    if "language" in value:
        out["Language"] = value["language"]
    import capo_geo_places.types.translation_name_type

    out["Type"] = capo_geo_places.types.translation_name_type.serialize_json(
        value["type"]
    )
    if "primary" in value:
        out["Primary"] = value["primary"]
    if "transliterated" in value:
        out["Transliterated"] = value["transliterated"]
    return out


def deserialize_json(data: dict) -> TranslationName:
    out: TranslationName = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("TranslationName.value required")
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    if data.get("Type") is not None:
        import capo_geo_places.types.translation_name_type

        out["type"] = capo_geo_places.types.translation_name_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("TranslationName.type required")
    if data.get("Primary") is not None:
        out["primary"] = data["Primary"]
    if data.get("Transliterated") is not None:
        out["transliterated"] = data["Transliterated"]
    return out
