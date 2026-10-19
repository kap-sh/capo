"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Interval``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError, SerializationError
from capo_application_signals.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_application_signals.types.calendar_interval
    import capo_application_signals.types.rolling_interval


class _Interval_RollingInterval(TypedDict, closed=True):
    RollingInterval: "capo_application_signals.types.rolling_interval.RollingInterval"


class _Interval_CalendarInterval(TypedDict, closed=True):
    CalendarInterval: (
        "capo_application_signals.types.calendar_interval.CalendarInterval"
    )


Interval: TypeAlias = (
    _Interval_RollingInterval | _Interval_CalendarInterval | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Interval) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Interval: cannot serialize unknown variant {value.name!r}"
        )
    elif "RollingInterval" in value:
        import capo_application_signals.types.rolling_interval

        return {
            "RollingInterval": capo_application_signals.types.rolling_interval.serialize_json(
                value["RollingInterval"]
            )
        }
    elif "CalendarInterval" in value:
        import capo_application_signals.types.calendar_interval

        return {
            "CalendarInterval": capo_application_signals.types.calendar_interval.serialize_json(
                value["CalendarInterval"]
            )
        }
    else:
        raise SerializationError("Interval: no variant present")


def deserialize_json(data: dict) -> Interval:
    if data.get("RollingInterval") is not None:
        import capo_application_signals.types.rolling_interval

        return {
            "RollingInterval": capo_application_signals.types.rolling_interval.deserialize_json(
                data["RollingInterval"]
            )
        }
    elif data.get("CalendarInterval") is not None:
        import capo_application_signals.types.calendar_interval

        return {
            "CalendarInterval": capo_application_signals.types.calendar_interval.deserialize_json(
                data["CalendarInterval"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Interval: no recognized variant key")
