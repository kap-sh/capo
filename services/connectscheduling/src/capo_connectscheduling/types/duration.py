"""Generated from Smithy shape ``com.amazonaws.connectscheduling#Duration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectscheduling.types.duration_unit
    import capo_connectscheduling.types.duration_value


class Duration(TypedDict, closed=True):
    value: "capo_connectscheduling.types.duration_value.DurationValue"
    """<p>The number of units of time. You can use a negative value to report an overdrawn balance. The value must be within 876,000 hours (100 years) of zero: at most 52,560,000 <code>MINUTES</code>, 876,000 <code>HOURS</code>, or 36,500 <code>DAYS</code>.</p>"""
    unit: "capo_connectscheduling.types.duration_unit.DurationUnit"
    """<p>The unit the value is counted in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Duration) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    import capo_connectscheduling.types.duration_unit

    out["Unit"] = capo_connectscheduling.types.duration_unit.serialize_json(
        value["unit"]
    )
    return out


def deserialize_json(data: dict) -> Duration:
    out: Duration = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    if data.get("Unit") is not None:
        import capo_connectscheduling.types.duration_unit

        out["unit"] = capo_connectscheduling.types.duration_unit.deserialize_json(
            data["Unit"]
        )
    else:
        import typing

        out["unit"] = typing.cast(
            "capo_connectscheduling.types.duration_unit.DurationUnit", ""
        )
    return out
