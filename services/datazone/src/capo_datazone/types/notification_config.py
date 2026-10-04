"""Generated from Smithy shape ``com.amazonaws.datazone#NotificationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.notify_on_states


class NotificationConfig(TypedDict, closed=True):
    notify_on: "capo_datazone.types.notify_on_states.NotifyOnStates"
    """Notebook run states that trigger notifications. Ordering is not significant."""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationConfig) -> dict:
    out: dict = {}
    import capo_datazone.types.notify_on_states

    out["notifyOn"] = capo_datazone.types.notify_on_states.serialize_json(
        value["notify_on"]
    )
    return out


def deserialize_json(data: dict) -> NotificationConfig:
    out: NotificationConfig = {}  # type: ignore[typeddict-item]
    if data.get("notifyOn") is not None:
        import capo_datazone.types.notify_on_states

        out["notify_on"] = capo_datazone.types.notify_on_states.deserialize_json(
            data["notifyOn"]
        )
    else:
        raise DeserializationError("NotificationConfig.notify_on required")
    return out
