"""Generated from Smithy shape ``com.amazonaws.ssm#AlarmStateInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.alarm_name
    import capo_ssm.types.external_alarm_state


class AlarmStateInformation(TypedDict, closed=True):
    name: "capo_ssm.types.alarm_name.AlarmName"
    """<p>The name of your CloudWatch alarm.</p>"""
    state: "capo_ssm.types.external_alarm_state.ExternalAlarmState"
    """<p>The state of your CloudWatch alarm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlarmStateInformation) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_ssm.types.external_alarm_state

    out["State"] = capo_ssm.types.external_alarm_state.serialize_aws_json_1_1(
        value["state"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AlarmStateInformation:
    out: AlarmStateInformation = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("State") is not None:
        import capo_ssm.types.external_alarm_state

        out["state"] = capo_ssm.types.external_alarm_state.deserialize_aws_json_1_1(
            data["State"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_ssm.types.external_alarm_state.ExternalAlarmState", ""
        )
    return out
