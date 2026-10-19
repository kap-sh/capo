"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteEmissionType``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_string


class RouteEmissionType(TypedDict, closed=True):
    co2_emission_class: NotRequired[
        "capo_geo_routes.types.sensitive_string.SensitiveString"
    ]
    """<p>The CO 2 emission classes.</p>"""
    type: "capo_geo_routes.types.sensitive_string.SensitiveString"
    """<p>Type of the emission.</p> <p> <b>Valid values</b>: <code>Euro1, Euro2, Euro3, Euro4, Euro5, Euro6, EuroEev</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteEmissionType) -> dict:
    out: dict = {}
    if "co2_emission_class" in value:
        out["Co2EmissionClass"] = value["co2_emission_class"]
    out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> RouteEmissionType:
    out: RouteEmissionType = {}  # type: ignore[typeddict-item]
    if data.get("Co2EmissionClass") is not None:
        out["co2_emission_class"] = data["Co2EmissionClass"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    return out


def redact_sensitive(value: RouteEmissionType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "co2_emission_class" in value:
        out["co2_emission_class"] = "*** Sensitive Data Redacted ***"
    if "type" in value:
        out["type"] = "*** Sensitive Data Redacted ***"
    return out
