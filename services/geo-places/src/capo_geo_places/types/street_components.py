"""Generated from Smithy shape ``com.amazonaws.geoplaces#StreetComponents``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.language_tag
    import capo_geo_places.types.sensitive_string
    import capo_geo_places.types.type_placement
    import capo_geo_places.types.type_separator


class StreetComponents(TypedDict, closed=True):
    base_name: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>Base name part of the street name. </p> <p>Example: Younge from the "Younge street".</p>"""
    type: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>Street type part of the street name. </p> <p>Example: <code>"avenue"</code>.</p>"""
    type_placement: NotRequired["capo_geo_places.types.type_placement.TypePlacement"]
    """<p>Defines if the street type is before or after the base name.</p>"""
    type_separator: NotRequired["capo_geo_places.types.type_separator.TypeSeparator"]
    """<p>Defines a separator character such as <code>""</code> or <code>" "</code> between the base name and type.</p>"""
    prefix: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>A prefix is a directional identifier that precedes, but is not included in, the base name of a road. </p> <p>Example: E for East.</p>"""
    suffix: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>A suffix is a directional identifier that follows, but is not included in, the base name of a road. </p> <p>Example W for West.</p>"""
    direction: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>Indicates the official directional identifiers assigned to highways.</p>"""
    language: NotRequired["capo_geo_places.types.language_tag.LanguageTag"]
    """<p>A <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreetComponents) -> dict:
    out: dict = {}
    if "base_name" in value:
        out["BaseName"] = value["base_name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "type_placement" in value:
        import capo_geo_places.types.type_placement

        out["TypePlacement"] = capo_geo_places.types.type_placement.serialize_json(
            value["type_placement"]
        )
    if "type_separator" in value:
        out["TypeSeparator"] = value["type_separator"]
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "suffix" in value:
        out["Suffix"] = value["suffix"]
    if "direction" in value:
        out["Direction"] = value["direction"]
    if "language" in value:
        out["Language"] = value["language"]
    return out


def deserialize_json(data: dict) -> StreetComponents:
    out: StreetComponents = {}  # type: ignore[typeddict-item]
    if data.get("BaseName") is not None:
        out["base_name"] = data["BaseName"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("TypePlacement") is not None:
        import capo_geo_places.types.type_placement

        out["type_placement"] = capo_geo_places.types.type_placement.deserialize_json(
            data["TypePlacement"]
        )
    if data.get("TypeSeparator") is not None:
        out["type_separator"] = data["TypeSeparator"]
    if data.get("Prefix") is not None:
        out["prefix"] = data["Prefix"]
    if data.get("Suffix") is not None:
        out["suffix"] = data["Suffix"]
    if data.get("Direction") is not None:
        out["direction"] = data["Direction"]
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    return out
