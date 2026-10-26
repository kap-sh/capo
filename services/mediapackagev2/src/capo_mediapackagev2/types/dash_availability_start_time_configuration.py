"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashAvailabilityStartTimeConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediapackagev2.errors import DeserializationError, SerializationError
from capo_mediapackagev2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import datetime


class _DashAvailabilityStartTimeConfiguration_FixedAvailabilityStartTime(
    TypedDict, closed=True
):
    FixedAvailabilityStartTime: "datetime.datetime"


DashAvailabilityStartTimeConfiguration: TypeAlias = (
    _DashAvailabilityStartTimeConfiguration_FixedAvailabilityStartTime
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DashAvailabilityStartTimeConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DashAvailabilityStartTimeConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "FixedAvailabilityStartTime" in value:
        import capo_mediapackagev2.types._prelude.timestamp

        return {
            "FixedAvailabilityStartTime": capo_mediapackagev2.types._prelude.timestamp.serialize_json(
                value["FixedAvailabilityStartTime"]
            )
        }
    else:
        raise SerializationError(
            "DashAvailabilityStartTimeConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> DashAvailabilityStartTimeConfiguration:
    if data.get("FixedAvailabilityStartTime") is not None:
        import capo_mediapackagev2.types._prelude.timestamp

        return {
            "FixedAvailabilityStartTime": capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["FixedAvailabilityStartTime"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "DashAvailabilityStartTimeConfiguration: no recognized variant key"
        )
