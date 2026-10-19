"""Generated from Smithy shape ``com.amazonaws.applicationsignals#RollingInterval``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.duration_unit
    import capo_application_signals.types.rolling_interval_duration


class RollingInterval(TypedDict, closed=True):
    duration_unit: "capo_application_signals.types.duration_unit.DurationUnit"
    """<p>Specifies the rolling interval unit.</p>"""
    duration: "capo_application_signals.types.rolling_interval_duration.RollingIntervalDuration"
    """<p>Specifies the duration of each rolling interval. For example, if <code>Duration</code> is <code>7</code> and <code>DurationUnit</code> is <code>DAY</code>, each rolling interval is seven days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RollingInterval) -> dict:
    out: dict = {}
    import capo_application_signals.types.duration_unit

    out["DurationUnit"] = capo_application_signals.types.duration_unit.serialize_json(
        value["duration_unit"]
    )
    out["Duration"] = value["duration"]
    return out


def deserialize_json(data: dict) -> RollingInterval:
    out: RollingInterval = {}  # type: ignore[typeddict-item]
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
