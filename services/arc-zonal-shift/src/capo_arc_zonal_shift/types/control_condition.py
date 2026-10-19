"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ControlCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.control_condition_type
    import capo_arc_zonal_shift.types.metric_identifier


class ControlCondition(TypedDict, closed=True):
    type: "capo_arc_zonal_shift.types.control_condition_type.ControlConditionType"
    """<p>The type of alarm specified for a practice run. You can only specify Amazon CloudWatch alarms for practice runs, so the only valid value is <code>CLOUDWATCH</code>.</p>"""
    alarm_identifier: "capo_arc_zonal_shift.types.metric_identifier.MetricIdentifier"
    """<p>The Amazon Resource Name (ARN) for an Amazon CloudWatch alarm that you specify as a control condition for a practice run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlCondition) -> dict:
    out: dict = {}
    import capo_arc_zonal_shift.types.control_condition_type

    out["type"] = capo_arc_zonal_shift.types.control_condition_type.serialize_json(
        value["type"]
    )
    out["alarmIdentifier"] = value["alarm_identifier"]
    return out


def deserialize_json(data: dict) -> ControlCondition:
    out: ControlCondition = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_arc_zonal_shift.types.control_condition_type

        out["type"] = (
            capo_arc_zonal_shift.types.control_condition_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_arc_zonal_shift.types.control_condition_type.ControlConditionType", ""
        )
    if data.get("alarmIdentifier") is not None:
        out["alarm_identifier"] = data["alarmIdentifier"]
    else:
        out["alarm_identifier"] = ""
    return out
