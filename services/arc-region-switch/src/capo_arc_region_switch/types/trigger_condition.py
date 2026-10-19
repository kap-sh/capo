"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#TriggerCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.alarm_condition


class TriggerCondition(TypedDict, closed=True):
    associated_alarm_name: "str"
    """<p>The name of the CloudWatch alarm associated with the condition.</p>"""
    condition: "capo_arc_region_switch.types.alarm_condition.AlarmCondition"
    """<p>The condition that must be met. Valid values include <code>green</code> and <code>red</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TriggerCondition) -> dict:
    out: dict = {}
    out["associatedAlarmName"] = value["associated_alarm_name"]
    import capo_arc_region_switch.types.alarm_condition

    out["condition"] = (
        capo_arc_region_switch.types.alarm_condition.serialize_aws_json_1_0(
            value["condition"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TriggerCondition:
    out: TriggerCondition = {}  # type: ignore[typeddict-item]
    if data.get("associatedAlarmName") is not None:
        out["associated_alarm_name"] = data["associatedAlarmName"]
    else:
        out["associated_alarm_name"] = ""
    if data.get("condition") is not None:
        import capo_arc_region_switch.types.alarm_condition

        out["condition"] = (
            capo_arc_region_switch.types.alarm_condition.deserialize_aws_json_1_0(
                data["condition"]
            )
        )
    else:
        import typing

        out["condition"] = typing.cast(
            "capo_arc_region_switch.types.alarm_condition.AlarmCondition", ""
        )
    return out
