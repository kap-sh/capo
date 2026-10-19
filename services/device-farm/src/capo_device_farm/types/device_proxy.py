"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceProxy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.device_proxy_host
    import capo_device_farm.types.device_proxy_port


class DeviceProxy(TypedDict, closed=True):
    host: "capo_device_farm.types.device_proxy_host.DeviceProxyHost"
    """<p>Hostname or IPv4 address of the proxy.</p>"""
    port: "capo_device_farm.types.device_proxy_port.DeviceProxyPort"
    """<p>The port number on which the http/s proxy is listening.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceProxy) -> dict:
    out: dict = {}
    out["host"] = value["host"]
    out["port"] = value.get("port", 3128)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceProxy:
    out: DeviceProxy = {}  # type: ignore[typeddict-item]
    if data.get("host") is not None:
        out["host"] = data["host"]
    else:
        out["host"] = ""
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        out["port"] = 3128
    return out
