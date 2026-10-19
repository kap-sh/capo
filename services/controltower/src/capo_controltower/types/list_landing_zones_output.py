"""Generated from Smithy shape ``com.amazonaws.controltower#ListLandingZonesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.landing_zone_summaries


class ListLandingZonesOutput(TypedDict, closed=True):
    landing_zones: "capo_controltower.types.landing_zone_summaries.LandingZoneSummaries"
    """<p>The ARN of the landing zone.</p>"""
    next_token: NotRequired["str"]
    """<p>Retrieves the next page of results. If the string is empty, the response is the end of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLandingZonesOutput) -> dict:
    out: dict = {}
    import capo_controltower.types.landing_zone_summaries

    out["landingZones"] = capo_controltower.types.landing_zone_summaries.serialize_json(
        value["landing_zones"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLandingZonesOutput:
    out: ListLandingZonesOutput = {}  # type: ignore[typeddict-item]
    if data.get("landingZones") is not None:
        import capo_controltower.types.landing_zone_summaries

        out["landing_zones"] = (
            capo_controltower.types.landing_zone_summaries.deserialize_json(
                data["landingZones"]
            )
        )
    else:
        out["landing_zones"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
