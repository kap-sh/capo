"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeviceList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.device

DeviceList: TypeAlias = list["capo_networkmanager.types.device.Device"]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceList) -> list:
    import capo_networkmanager.types.device

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.device.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeviceList:
    import capo_networkmanager.types.device

    out: DeviceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_networkmanager.types.device.deserialize_json(item))
    return out


def redact_sensitive(value: DeviceList) -> list[Any]:
    import capo_networkmanager.types.device

    return [capo_networkmanager.types.device.redact_sensitive(item) for item in value]
