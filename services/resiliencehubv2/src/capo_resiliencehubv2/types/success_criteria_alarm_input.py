"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SuccessCriteriaAlarmInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.cloud_watch_alarm_arn


class SuccessCriteriaAlarmInput(TypedDict, closed=True):
    alarm_arn: "capo_resiliencehubv2.types.cloud_watch_alarm_arn.CloudWatchAlarmArn"
    """<p>The ARN of the CloudWatch alarm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuccessCriteriaAlarmInput) -> dict:
    out: dict = {}
    out["alarmArn"] = value["alarm_arn"]
    return out


def deserialize_json(data: dict) -> SuccessCriteriaAlarmInput:
    out: SuccessCriteriaAlarmInput = {}  # type: ignore[typeddict-item]
    if data.get("alarmArn") is not None:
        out["alarm_arn"] = data["alarmArn"]
    else:
        out["alarm_arn"] = ""
    return out
