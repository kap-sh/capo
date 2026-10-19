"""Generated from Smithy shape ``com.amazonaws.iotwireless#SemtechGnssConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.position_configuration_fec
    import capo_iot_wireless.types.position_configuration_status


class SemtechGnssConfiguration(TypedDict, closed=True):
    status: "capo_iot_wireless.types.position_configuration_status.PositionConfigurationStatus"
    """<p>The status indicating whether the solver is enabled.</p>"""
    fec: "capo_iot_wireless.types.position_configuration_fec.PositionConfigurationFec"
    """<p>Whether forward error correction is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SemtechGnssConfiguration) -> dict:
    out: dict = {}
    import capo_iot_wireless.types.position_configuration_status

    out["Status"] = (
        capo_iot_wireless.types.position_configuration_status.serialize_json(
            value["status"]
        )
    )
    import capo_iot_wireless.types.position_configuration_fec

    out["Fec"] = capo_iot_wireless.types.position_configuration_fec.serialize_json(
        value["fec"]
    )
    return out


def deserialize_json(data: dict) -> SemtechGnssConfiguration:
    out: SemtechGnssConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_iot_wireless.types.position_configuration_status

        out["status"] = (
            capo_iot_wireless.types.position_configuration_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_iot_wireless.types.position_configuration_status.PositionConfigurationStatus",
            "",
        )
    if data.get("Fec") is not None:
        import capo_iot_wireless.types.position_configuration_fec

        out["fec"] = (
            capo_iot_wireless.types.position_configuration_fec.deserialize_json(
                data["Fec"]
            )
        )
    else:
        import typing

        out["fec"] = typing.cast(
            "capo_iot_wireless.types.position_configuration_fec.PositionConfigurationFec",
            "",
        )
    return out
