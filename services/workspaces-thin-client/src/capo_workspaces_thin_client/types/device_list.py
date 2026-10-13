"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#DeviceList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.device_summary

DeviceList: TypeAlias = list[
    "capo_workspaces_thin_client.types.device_summary.DeviceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceList) -> list:
    import capo_workspaces_thin_client.types.device_summary

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_thin_client.types.device_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeviceList:
    import capo_workspaces_thin_client.types.device_summary

    out: DeviceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_thin_client.types.device_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: DeviceList) -> list[Any]:
    import capo_workspaces_thin_client.types.device_summary

    return [
        capo_workspaces_thin_client.types.device_summary.redact_sensitive(item)
        for item in value
    ]
