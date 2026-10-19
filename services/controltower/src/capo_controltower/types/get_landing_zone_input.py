"""Generated from Smithy shape ``com.amazonaws.controltower#GetLandingZoneInput``."""

from typing_extensions import TypedDict


class GetLandingZoneInput(TypedDict, closed=True):
    landing_zone_identifier: "str"
    """<p>The unique identifier of the landing zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLandingZoneInput) -> dict:
    out: dict = {}
    out["landingZoneIdentifier"] = value["landing_zone_identifier"]
    return out


def deserialize_json(data: dict) -> GetLandingZoneInput:
    out: GetLandingZoneInput = {}  # type: ignore[typeddict-item]
    if data.get("landingZoneIdentifier") is not None:
        out["landing_zone_identifier"] = data["landingZoneIdentifier"]
    else:
        out["landing_zone_identifier"] = ""
    return out
