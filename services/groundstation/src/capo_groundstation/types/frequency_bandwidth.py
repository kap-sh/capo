"""Generated from Smithy shape ``com.amazonaws.groundstation#FrequencyBandwidth``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.bandwidth_units


class FrequencyBandwidth(TypedDict, closed=True):
    value: "float"
    """<p>Frequency bandwidth value. AWS Ground Station currently has the following bandwidth limitations:</p> <ul> <li> <p>For <code>AntennaDownlinkDemodDecodeconfig</code>, valid values are between 125 kHz to 650 MHz.</p> </li> <li> <p>For <code>AntennaDownlinkconfig</code>, valid values are between 10 kHz to 54 MHz.</p> </li> <li> <p>For <code>AntennaUplinkConfig</code>, valid values are between 10 kHz to 54 MHz.</p> </li> </ul>"""
    units: "capo_groundstation.types.bandwidth_units.BandwidthUnits"
    """<p>Frequency bandwidth units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrequencyBandwidth) -> dict:
    out: dict = {}
    out["value"] = (
        "NaN"
        if value["value"] != value["value"]
        else "Infinity"
        if value["value"] == float("inf")
        else "-Infinity"
        if value["value"] == float("-inf")
        else value["value"]
    )
    import capo_groundstation.types.bandwidth_units

    out["units"] = capo_groundstation.types.bandwidth_units.serialize_json(
        value["units"]
    )
    return out


def deserialize_json(data: dict) -> FrequencyBandwidth:
    out: FrequencyBandwidth = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0.0
    if data.get("units") is not None:
        import capo_groundstation.types.bandwidth_units

        out["units"] = capo_groundstation.types.bandwidth_units.deserialize_json(
            data["units"]
        )
    else:
        import typing

        out["units"] = typing.cast(
            "capo_groundstation.types.bandwidth_units.BandwidthUnits", ""
        )
    return out
