"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisTypeDescription``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError
from capo_groundstation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_groundstation.types.ephemeris_description


class _EphemerisTypeDescription_tle(TypedDict, closed=True):
    tle: "capo_groundstation.types.ephemeris_description.EphemerisDescription"


class _EphemerisTypeDescription_oem(TypedDict, closed=True):
    oem: "capo_groundstation.types.ephemeris_description.EphemerisDescription"


class _EphemerisTypeDescription_azEl(TypedDict, closed=True):
    azEl: "capo_groundstation.types.ephemeris_description.EphemerisDescription"


EphemerisTypeDescription: TypeAlias = (
    _EphemerisTypeDescription_tle
    | _EphemerisTypeDescription_oem
    | _EphemerisTypeDescription_azEl
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisTypeDescription) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EphemerisTypeDescription: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "tle" in value:
        import capo_groundstation.types.ephemeris_description

        return {
            "tle": capo_groundstation.types.ephemeris_description.serialize_json(
                value["tle"]
            )
        }
    elif "oem" in value:
        import capo_groundstation.types.ephemeris_description

        return {
            "oem": capo_groundstation.types.ephemeris_description.serialize_json(
                value["oem"]
            )
        }
    elif "azEl" in value:
        import capo_groundstation.types.ephemeris_description

        return {
            "azEl": capo_groundstation.types.ephemeris_description.serialize_json(
                value["azEl"]
            )
        }
    else:
        raise SerializationError("EphemerisTypeDescription: no variant present")


def deserialize_json(data: dict) -> EphemerisTypeDescription:
    if data.get("tle") is not None:
        import capo_groundstation.types.ephemeris_description

        return {
            "tle": capo_groundstation.types.ephemeris_description.deserialize_json(
                data["tle"]
            )
        }
    elif data.get("oem") is not None:
        import capo_groundstation.types.ephemeris_description

        return {
            "oem": capo_groundstation.types.ephemeris_description.deserialize_json(
                data["oem"]
            )
        }
    elif data.get("azEl") is not None:
        import capo_groundstation.types.ephemeris_description

        return {
            "azEl": capo_groundstation.types.ephemeris_description.deserialize_json(
                data["azEl"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "EphemerisTypeDescription: no recognized variant key"
        )
