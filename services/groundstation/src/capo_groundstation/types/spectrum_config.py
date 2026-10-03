"""Generated from Smithy shape ``com.amazonaws.groundstation#SpectrumConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.frequency
    import capo_groundstation.types.frequency_bandwidth
    import capo_groundstation.types.polarization


class SpectrumConfig(TypedDict, closed=True):
    center_frequency: "capo_groundstation.types.frequency.Frequency"
    """<p>Center frequency of a spectral <code>Config</code>. Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.</p>"""
    bandwidth: "capo_groundstation.types.frequency_bandwidth.FrequencyBandwidth"
    """<p>Bandwidth of a spectral <code>Config</code>. AWS Ground Station currently has the following bandwidth limitations:</p> <ul> <li> <p>For <code>AntennaDownlinkDemodDecodeconfig</code>, valid values are between 125 kHz to 650 MHz.</p> </li> <li> <p>For <code>AntennaDownlinkconfig</code> valid values are between 10 kHz to 54 MHz.</p> </li> <li> <p>For <code>AntennaUplinkConfig</code>, valid values are between 10 kHz to 54 MHz.</p> </li> </ul>"""
    polarization: NotRequired["capo_groundstation.types.polarization.Polarization"]
    """<p>Polarization of a spectral <code>Config</code>. Capturing both <code>"RIGHT_HAND"</code> and <code>"LEFT_HAND"</code> polarization requires two separate configs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpectrumConfig) -> dict:
    out: dict = {}
    import capo_groundstation.types.frequency

    out["centerFrequency"] = capo_groundstation.types.frequency.serialize_json(
        value["center_frequency"]
    )
    import capo_groundstation.types.frequency_bandwidth

    out["bandwidth"] = capo_groundstation.types.frequency_bandwidth.serialize_json(
        value["bandwidth"]
    )
    import capo_groundstation.types.polarization

    out["polarization"] = capo_groundstation.types.polarization.serialize_json(
        value.get("polarization", "NONE")
    )
    return out


def deserialize_json(data: dict) -> SpectrumConfig:
    out: SpectrumConfig = {}  # type: ignore[typeddict-item]
    if data.get("centerFrequency") is not None:
        import capo_groundstation.types.frequency

        out["center_frequency"] = capo_groundstation.types.frequency.deserialize_json(
            data["centerFrequency"]
        )
    else:
        raise DeserializationError("SpectrumConfig.center_frequency required")
    if data.get("bandwidth") is not None:
        import capo_groundstation.types.frequency_bandwidth

        out["bandwidth"] = (
            capo_groundstation.types.frequency_bandwidth.deserialize_json(
                data["bandwidth"]
            )
        )
    else:
        raise DeserializationError("SpectrumConfig.bandwidth required")
    if data.get("polarization") is not None:
        import capo_groundstation.types.polarization

        out["polarization"] = capo_groundstation.types.polarization.deserialize_json(
            data["polarization"]
        )
    else:
        out["polarization"] = "NONE"
    return out
