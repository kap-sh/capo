"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#RestrictedPeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.iso8601_date
    import capo_connectcampaignsv2.types.restricted_period_name


class RestrictedPeriod(TypedDict, closed=True):
    name: NotRequired[
        "capo_connectcampaignsv2.types.restricted_period_name.RestrictedPeriodName"
    ]
    start_date: "capo_connectcampaignsv2.types.iso8601_date.Iso8601Date"
    end_date: "capo_connectcampaignsv2.types.iso8601_date.Iso8601Date"


# --- restJson1 ser/de ---
def serialize_json(value: RestrictedPeriod) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["startDate"] = value["start_date"]
    out["endDate"] = value["end_date"]
    return out


def deserialize_json(data: dict) -> RestrictedPeriod:
    out: RestrictedPeriod = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("startDate") is not None:
        out["start_date"] = data["startDate"]
    else:
        out["start_date"] = ""
    if data.get("endDate") is not None:
        out["end_date"] = data["endDate"]
    else:
        out["end_date"] = ""
    return out
