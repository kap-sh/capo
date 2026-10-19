"""Generated from Smithy shape ``com.amazonaws.georoutes#LocalizedString``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.language_tag
    import capo_geo_routes.types.sensitive_string


class LocalizedString(TypedDict, closed=True):
    language: NotRequired["capo_geo_routes.types.language_tag.LanguageTag"]
    """<p>A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language can't be provided.</p>"""
    value: "capo_geo_routes.types.sensitive_string.SensitiveString"
    """<p>The value of the localized string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocalizedString) -> dict:
    out: dict = {}
    if "language" in value:
        out["Language"] = value["language"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> LocalizedString:
    out: LocalizedString = {}  # type: ignore[typeddict-item]
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out


def redact_sensitive(value: LocalizedString) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
