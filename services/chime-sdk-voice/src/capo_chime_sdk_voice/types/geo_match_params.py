"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GeoMatchParams``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.area_code
    import capo_chime_sdk_voice.types.country


class GeoMatchParams(TypedDict, closed=True):
    country: "capo_chime_sdk_voice.types.country.Country"
    """<p>The country.</p>"""
    area_code: "capo_chime_sdk_voice.types.area_code.AreaCode"
    """<p>The area code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeoMatchParams) -> dict:
    out: dict = {}
    out["Country"] = value["country"]
    out["AreaCode"] = value["area_code"]
    return out


def deserialize_json(data: dict) -> GeoMatchParams:
    out: GeoMatchParams = {}  # type: ignore[typeddict-item]
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    else:
        out["country"] = ""
    if data.get("AreaCode") is not None:
        out["area_code"] = data["AreaCode"]
    else:
        out["area_code"] = ""
    return out
