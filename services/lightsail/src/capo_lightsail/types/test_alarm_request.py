"""Generated from Smithy shape ``com.amazonaws.lightsail#TestAlarmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.alarm_state
    import capo_lightsail.types.resource_name


class TestAlarmRequest(TypedDict, closed=True):
    alarm_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the alarm to test.</p>"""
    state: "capo_lightsail.types.alarm_state.AlarmState"
    """<p>The alarm state to test.</p> <p>An alarm has the following possible states that can be tested:</p> <ul> <li> <p> <code>ALARM</code> - The metric is outside of the defined threshold.</p> </li> <li> <p> <code>INSUFFICIENT_DATA</code> - The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.</p> </li> <li> <p> <code>OK</code> - The metric is within the defined threshold.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestAlarmRequest) -> dict:
    out: dict = {}
    out["alarmName"] = value["alarm_name"]
    import capo_lightsail.types.alarm_state

    out["state"] = capo_lightsail.types.alarm_state.serialize_aws_json_1_1(
        value["state"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestAlarmRequest:
    out: TestAlarmRequest = {}  # type: ignore[typeddict-item]
    if data.get("alarmName") is not None:
        out["alarm_name"] = data["alarmName"]
    else:
        out["alarm_name"] = ""
    if data.get("state") is not None:
        import capo_lightsail.types.alarm_state

        out["state"] = capo_lightsail.types.alarm_state.deserialize_aws_json_1_1(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast("capo_lightsail.types.alarm_state.AlarmState", "")
    return out
