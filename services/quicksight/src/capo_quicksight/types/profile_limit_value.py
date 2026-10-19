"""Generated from Smithy shape ``com.amazonaws.quicksight#ProfileLimitValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.limit_unit
    import capo_quicksight.types.profile_limit_value_max_value_long


class ProfileLimitValue(TypedDict, closed=True):
    max_value: "capo_quicksight.types.profile_limit_value_max_value_long.ProfileLimitValueMaxValueLong"
    """<p>The maximum allowed value for the resource.</p>"""
    unit: "capo_quicksight.types.limit_unit.LimitUnit"
    """<p>The unit of measurement for the limit value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileLimitValue) -> dict:
    out: dict = {}
    out["maxValue"] = value["max_value"]
    import capo_quicksight.types.limit_unit

    out["unit"] = capo_quicksight.types.limit_unit.serialize_json(value["unit"])
    return out


def deserialize_json(data: dict) -> ProfileLimitValue:
    out: ProfileLimitValue = {}  # type: ignore[typeddict-item]
    if data.get("maxValue") is not None:
        out["max_value"] = data["maxValue"]
    else:
        out["max_value"] = 0
    if data.get("unit") is not None:
        import capo_quicksight.types.limit_unit

        out["unit"] = capo_quicksight.types.limit_unit.deserialize_json(data["unit"])
    else:
        import typing

        out["unit"] = typing.cast("capo_quicksight.types.limit_unit.LimitUnit", "")
    return out
