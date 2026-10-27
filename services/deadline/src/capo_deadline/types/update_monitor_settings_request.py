"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateMonitorSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.monitor_id
    import capo_deadline.types.settings_map


class UpdateMonitorSettingsRequest(TypedDict, closed=True):
    monitor_id: "capo_deadline.types.monitor_id.MonitorId"
    """The unique identifier of the monitor to update settings for."""
    settings: "capo_deadline.types.settings_map.SettingsMap"
    """The monitor settings to update as key-value pairs. Keys present in the request are upserted; keys absent are left unchanged. Send an empty string value to delete a key."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMonitorSettingsRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.settings_map

    out["settings"] = capo_deadline.types.settings_map.serialize_json(value["settings"])
    return out


def deserialize_json(data: dict) -> UpdateMonitorSettingsRequest:
    out: UpdateMonitorSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("settings") is not None:
        import capo_deadline.types.settings_map

        out["settings"] = capo_deadline.types.settings_map.deserialize_json(
            data["settings"]
        )
    else:
        out["settings"] = {}
    return out
