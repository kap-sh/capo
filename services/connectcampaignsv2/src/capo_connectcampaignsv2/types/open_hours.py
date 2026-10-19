"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#OpenHours``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError
from capo_connectcampaignsv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.daily_hours


class _OpenHours_dailyHours(TypedDict, closed=True):
    dailyHours: "capo_connectcampaignsv2.types.daily_hours.DailyHours"


OpenHours: TypeAlias = _OpenHours_dailyHours | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: OpenHours) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"OpenHours: cannot serialize unknown variant {value.name!r}"
        )
    elif "dailyHours" in value:
        import capo_connectcampaignsv2.types.daily_hours

        return {
            "dailyHours": capo_connectcampaignsv2.types.daily_hours.serialize_json(
                value["dailyHours"]
            )
        }
    else:
        raise SerializationError("OpenHours: no variant present")


def deserialize_json(data: dict) -> OpenHours:
    if data.get("dailyHours") is not None:
        import capo_connectcampaignsv2.types.daily_hours

        return {
            "dailyHours": capo_connectcampaignsv2.types.daily_hours.deserialize_json(
                data["dailyHours"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("OpenHours: no recognized variant key")
