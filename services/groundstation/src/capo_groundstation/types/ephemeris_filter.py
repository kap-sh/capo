"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError
from capo_groundstation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_groundstation.types.az_el_ephemeris_filter


class _EphemerisFilter_azEl(TypedDict, closed=True):
    azEl: "capo_groundstation.types.az_el_ephemeris_filter.AzElEphemerisFilter"


EphemerisFilter: TypeAlias = _EphemerisFilter_azEl | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisFilter) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"EphemerisFilter: cannot serialize unknown variant {value.name!r}"
        )
    elif "azEl" in value:
        import capo_groundstation.types.az_el_ephemeris_filter

        return {
            "azEl": capo_groundstation.types.az_el_ephemeris_filter.serialize_json(
                value["azEl"]
            )
        }
    else:
        raise SerializationError("EphemerisFilter: no variant present")


def deserialize_json(data: dict) -> EphemerisFilter:
    if data.get("azEl") is not None:
        import capo_groundstation.types.az_el_ephemeris_filter

        return {
            "azEl": capo_groundstation.types.az_el_ephemeris_filter.deserialize_json(
                data["azEl"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("EphemerisFilter: no recognized variant key")
