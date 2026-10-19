"""Generated from Smithy shape ``com.amazonaws.braket#DeviceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_braket.types.string256


class DeviceConfig(TypedDict, closed=True):
    device: "capo_braket.types.string256.String256"
    """<p>The primary device ARN used to create and run an Amazon Braket hybrid job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceConfig) -> dict:
    out: dict = {}
    out["device"] = value["device"]
    return out


def deserialize_json(data: dict) -> DeviceConfig:
    out: DeviceConfig = {}  # type: ignore[typeddict-item]
    if data.get("device") is not None:
        out["device"] = data["device"]
    else:
        out["device"] = ""
    return out
