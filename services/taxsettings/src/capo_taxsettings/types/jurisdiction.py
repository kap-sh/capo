"""Generated from Smithy shape ``com.amazonaws.taxsettings#Jurisdiction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.country_code
    import capo_taxsettings.types.state


class Jurisdiction(TypedDict, closed=True):
    state_or_region: NotRequired["capo_taxsettings.types.state.State"]
    """<p> The state, region, or province associated with the country of the jurisdiction, if applicable. </p>"""
    country_code: "capo_taxsettings.types.country_code.CountryCode"
    """<p> The country code of the jurisdiction. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Jurisdiction) -> dict:
    out: dict = {}
    if "state_or_region" in value:
        out["stateOrRegion"] = value["state_or_region"]
    out["countryCode"] = value["country_code"]
    return out


def deserialize_json(data: dict) -> Jurisdiction:
    out: Jurisdiction = {}  # type: ignore[typeddict-item]
    if data.get("stateOrRegion") is not None:
        out["state_or_region"] = data["stateOrRegion"]
    if data.get("countryCode") is not None:
        out["country_code"] = data["countryCode"]
    else:
        out["country_code"] = ""
    return out
