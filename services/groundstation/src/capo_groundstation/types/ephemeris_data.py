"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError
from capo_groundstation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_groundstation.types.az_el_ephemeris
    import capo_groundstation.types.oem_ephemeris
    import capo_groundstation.types.tle_ephemeris


class _EphemerisData_tle(TypedDict, closed=True):
    tle: "capo_groundstation.types.tle_ephemeris.TLEEphemeris"


class _EphemerisData_oem(TypedDict, closed=True):
    oem: "capo_groundstation.types.oem_ephemeris.OEMEphemeris"


class _EphemerisData_azEl(TypedDict, closed=True):
    azEl: "capo_groundstation.types.az_el_ephemeris.AzElEphemeris"


EphemerisData: TypeAlias = (
    _EphemerisData_tle | _EphemerisData_oem | _EphemerisData_azEl | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EphemerisData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "tle" in value:
        import capo_groundstation.types.tle_ephemeris

        return {
            "tle": capo_groundstation.types.tle_ephemeris.serialize_json(value["tle"])
        }
    elif "oem" in value:
        import capo_groundstation.types.oem_ephemeris

        return {
            "oem": capo_groundstation.types.oem_ephemeris.serialize_json(value["oem"])
        }
    elif "azEl" in value:
        import capo_groundstation.types.az_el_ephemeris

        return {
            "azEl": capo_groundstation.types.az_el_ephemeris.serialize_json(
                value["azEl"]
            )
        }
    else:
        raise SerializationError("EphemerisData: no variant present")


def deserialize_json(data: dict) -> EphemerisData:
    if data.get("tle") is not None:
        import capo_groundstation.types.tle_ephemeris

        return {
            "tle": capo_groundstation.types.tle_ephemeris.deserialize_json(data["tle"])
        }
    elif data.get("oem") is not None:
        import capo_groundstation.types.oem_ephemeris

        return {
            "oem": capo_groundstation.types.oem_ephemeris.deserialize_json(data["oem"])
        }
    elif data.get("azEl") is not None:
        import capo_groundstation.types.az_el_ephemeris

        return {
            "azEl": capo_groundstation.types.az_el_ephemeris.deserialize_json(
                data["azEl"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EphemerisData: no recognized variant key")
