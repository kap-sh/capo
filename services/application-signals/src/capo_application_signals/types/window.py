"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Window``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.duration_unit
    import capo_application_signals.types.exclusion_duration


class Window(TypedDict, closed=True):
    duration_unit: "capo_application_signals.types.duration_unit.DurationUnit"
    """<p>The unit of time for the exclusion window duration. Valid values: MINUTE, HOUR, DAY, MONTH.</p>"""
    duration: "capo_application_signals.types.exclusion_duration.ExclusionDuration"
    """<p>The number of time units for the exclusion window length.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Window) -> dict:
    out: dict = {}
    import capo_application_signals.types.duration_unit

    out["DurationUnit"] = capo_application_signals.types.duration_unit.serialize_json(
        value["duration_unit"]
    )
    out["Duration"] = value["duration"]
    return out


def deserialize_json(data: dict) -> Window:
    out: Window = {}  # type: ignore[typeddict-item]
    if data.get("DurationUnit") is not None:
        import capo_application_signals.types.duration_unit

        out["duration_unit"] = (
            capo_application_signals.types.duration_unit.deserialize_json(
                data["DurationUnit"]
            )
        )
    else:
        import typing

        out["duration_unit"] = typing.cast(
            "capo_application_signals.types.duration_unit.DurationUnit", ""
        )
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    return out
