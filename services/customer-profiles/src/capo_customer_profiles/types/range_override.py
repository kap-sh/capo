"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RangeOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.end
    import capo_customer_profiles.types.range_unit
    import capo_customer_profiles.types.start


class RangeOverride(TypedDict, closed=True):
    start: "capo_customer_profiles.types.start.Start"
    """<p>The start time of when to include objects.</p>"""
    end: "capo_customer_profiles.types.end.End"
    """<p>The end time of when to include objects.</p>"""
    unit: "capo_customer_profiles.types.range_unit.RangeUnit"
    """<p>The unit for start and end.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RangeOverride) -> dict:
    out: dict = {}
    out["Start"] = value.get("start", 366)
    out["End"] = value.get("end", 0)
    import capo_customer_profiles.types.range_unit

    out["Unit"] = capo_customer_profiles.types.range_unit.serialize_json(value["unit"])
    return out


def deserialize_json(data: dict) -> RangeOverride:
    out: RangeOverride = {}  # type: ignore[typeddict-item]
    if data.get("Start") is not None:
        out["start"] = data["Start"]
    else:
        out["start"] = 366
    if data.get("End") is not None:
        out["end"] = data["End"]
    else:
        out["end"] = 0
    if data.get("Unit") is not None:
        import capo_customer_profiles.types.range_unit

        out["unit"] = capo_customer_profiles.types.range_unit.deserialize_json(
            data["Unit"]
        )
    else:
        import typing

        out["unit"] = typing.cast(
            "capo_customer_profiles.types.range_unit.RangeUnit", ""
        )
    return out
