"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisResponseData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.ephemeris_type
    import capo_groundstation.types.uuid


class EphemerisResponseData(TypedDict, closed=True):
    ephemeris_id: NotRequired["capo_groundstation.types.uuid.Uuid"]
    """<p>Unique identifier of the ephemeris. Appears only for custom ephemerides.</p>"""
    ephemeris_type: "capo_groundstation.types.ephemeris_type.EphemerisType"
    """<p>Type of ephemeris.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisResponseData) -> dict:
    out: dict = {}
    if "ephemeris_id" in value:
        out["ephemerisId"] = value["ephemeris_id"]
    import capo_groundstation.types.ephemeris_type

    out["ephemerisType"] = capo_groundstation.types.ephemeris_type.serialize_json(
        value["ephemeris_type"]
    )
    return out


def deserialize_json(data: dict) -> EphemerisResponseData:
    out: EphemerisResponseData = {}  # type: ignore[typeddict-item]
    if data.get("ephemerisId") is not None:
        out["ephemeris_id"] = data["ephemerisId"]
    if data.get("ephemerisType") is not None:
        import capo_groundstation.types.ephemeris_type

        out["ephemeris_type"] = (
            capo_groundstation.types.ephemeris_type.deserialize_json(
                data["ephemerisType"]
            )
        )
    else:
        import typing

        out["ephemeris_type"] = typing.cast(
            "capo_groundstation.types.ephemeris_type.EphemerisType", ""
        )
    return out
