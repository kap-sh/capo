"""Generated from Smithy shape ``com.amazonaws.snowball#WirelessConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.boolean


class WirelessConnection(TypedDict, closed=True):
    is_wifi_enabled: "capo_snowball.types.boolean.Boolean"
    """<p>Enables the Wi-Fi adapter on an Snowball Edge device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WirelessConnection) -> dict:
    out: dict = {}
    out["IsWifiEnabled"] = value.get("is_wifi_enabled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> WirelessConnection:
    out: WirelessConnection = {}  # type: ignore[typeddict-item]
    if data.get("IsWifiEnabled") is not None:
        out["is_wifi_enabled"] = data["IsWifiEnabled"]
    else:
        out["is_wifi_enabled"] = False
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WirelessConnection) -> dict:
    out: dict = {}
    out["IsWifiEnabled"] = value.get("is_wifi_enabled", False)
    return out


def deserialize_cbor(data: dict) -> WirelessConnection:
    out: WirelessConnection = {}  # type: ignore[typeddict-item]
    if data.get("IsWifiEnabled") is not None:
        out["is_wifi_enabled"] = data["IsWifiEnabled"]
    else:
        out["is_wifi_enabled"] = False
    return out
