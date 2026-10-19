"""Generated from Smithy shape ``com.amazonaws.groundstation#UplinkEchoConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.config_arn


class UplinkEchoConfig(TypedDict, closed=True):
    enabled: "bool"
    """<p>Whether or not an uplink <code>Config</code> is enabled.</p>"""
    antenna_uplink_config_arn: "capo_groundstation.types.config_arn.ConfigArn"
    """<p>ARN of an uplink <code>Config</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UplinkEchoConfig) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    out["antennaUplinkConfigArn"] = value["antenna_uplink_config_arn"]
    return out


def deserialize_json(data: dict) -> UplinkEchoConfig:
    out: UplinkEchoConfig = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if data.get("antennaUplinkConfigArn") is not None:
        out["antenna_uplink_config_arn"] = data["antennaUplinkConfigArn"]
    else:
        out["antenna_uplink_config_arn"] = ""
    return out
