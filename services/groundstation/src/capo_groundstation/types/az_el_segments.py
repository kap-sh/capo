"""Generated from Smithy shape ``com.amazonaws.groundstation#AzElSegments``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.angle_units
    import capo_groundstation.types.az_el_segment_list


class AzElSegments(TypedDict, closed=True):
    angle_unit: "capo_groundstation.types.angle_units.AngleUnits"
    """<p>The unit of measure for azimuth and elevation angles. All angles in all segments must use the same unit.</p>"""
    az_el_segment_list: "capo_groundstation.types.az_el_segment_list.AzElSegmentList"
    """<p>List of azimuth elevation segments.</p> <p>Must contain between 1 and 100 segments. Segments must be in chronological order with no overlaps.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzElSegments) -> dict:
    out: dict = {}
    import capo_groundstation.types.angle_units

    out["angleUnit"] = capo_groundstation.types.angle_units.serialize_json(
        value["angle_unit"]
    )
    import capo_groundstation.types.az_el_segment_list

    out["azElSegmentList"] = capo_groundstation.types.az_el_segment_list.serialize_json(
        value["az_el_segment_list"]
    )
    return out


def deserialize_json(data: dict) -> AzElSegments:
    out: AzElSegments = {}  # type: ignore[typeddict-item]
    if data.get("angleUnit") is not None:
        import capo_groundstation.types.angle_units

        out["angle_unit"] = capo_groundstation.types.angle_units.deserialize_json(
            data["angleUnit"]
        )
    else:
        import typing

        out["angle_unit"] = typing.cast(
            "capo_groundstation.types.angle_units.AngleUnits", ""
        )
    if data.get("azElSegmentList") is not None:
        import capo_groundstation.types.az_el_segment_list

        out["az_el_segment_list"] = (
            capo_groundstation.types.az_el_segment_list.deserialize_json(
                data["azElSegmentList"]
            )
        )
    else:
        out["az_el_segment_list"] = []
    return out
