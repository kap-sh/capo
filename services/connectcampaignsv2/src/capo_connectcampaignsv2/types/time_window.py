"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TimeWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.open_hours
    import capo_connectcampaignsv2.types.restricted_periods


class TimeWindow(TypedDict, closed=True):
    open_hours: "capo_connectcampaignsv2.types.open_hours.OpenHours"
    restricted_periods: NotRequired[
        "capo_connectcampaignsv2.types.restricted_periods.RestrictedPeriods"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: TimeWindow) -> dict:
    out: dict = {}
    import capo_connectcampaignsv2.types.open_hours

    out["openHours"] = capo_connectcampaignsv2.types.open_hours.serialize_json(
        value["open_hours"]
    )
    if "restricted_periods" in value:
        import capo_connectcampaignsv2.types.restricted_periods

        out["restrictedPeriods"] = (
            capo_connectcampaignsv2.types.restricted_periods.serialize_json(
                value["restricted_periods"]
            )
        )
    return out


def deserialize_json(data: dict) -> TimeWindow:
    out: TimeWindow = {}  # type: ignore[typeddict-item]
    if data.get("openHours") is not None:
        import capo_connectcampaignsv2.types.open_hours

        out["open_hours"] = capo_connectcampaignsv2.types.open_hours.deserialize_json(
            data["openHours"]
        )
    else:
        import capo_connectcampaignsv2.types._unknown

        out["open_hours"] = capo_connectcampaignsv2.types._unknown.UnknownUnionMember(
            ""
        )
    if data.get("restrictedPeriods") is not None:
        import capo_connectcampaignsv2.types.restricted_periods

        out["restricted_periods"] = (
            capo_connectcampaignsv2.types.restricted_periods.deserialize_json(
                data["restrictedPeriods"]
            )
        )
    return out
