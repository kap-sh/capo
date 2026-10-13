"""Generated from Smithy shape ``com.amazonaws.geoplaces#Country``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.country_code2
    import capo_geo_places.types.country_code3
    import capo_geo_places.types.sensitive_string


class Country(TypedDict, closed=True):
    code2: NotRequired["capo_geo_places.types.country_code2.CountryCode2"]
    """<p>Country, represented by its alpha 2-character code. </p>"""
    code3: NotRequired["capo_geo_places.types.country_code3.CountryCode3"]
    """<p>Country, represented by its alpha t-character code. </p>"""
    name: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>Name of the country.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Country) -> dict:
    out: dict = {}
    if "code2" in value:
        out["Code2"] = value["code2"]
    if "code3" in value:
        out["Code3"] = value["code3"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> Country:
    out: Country = {}  # type: ignore[typeddict-item]
    if data.get("Code2") is not None:
        out["code2"] = data["Code2"]
    if data.get("Code3") is not None:
        out["code3"] = data["Code3"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out


def redact_sensitive(value: Country) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "code2" in value:
        out["code2"] = "*** Sensitive Data Redacted ***"
    if "code3" in value:
        out["code3"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
