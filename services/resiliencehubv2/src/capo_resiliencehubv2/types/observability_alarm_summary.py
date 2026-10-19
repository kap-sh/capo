"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ObservabilityAlarmSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.cloud_watch_alarm_arn


class ObservabilityAlarmSummary(TypedDict, closed=True):
    alarm_arn: "capo_resiliencehubv2.types.cloud_watch_alarm_arn.CloudWatchAlarmArn"
    """<p>The ARN of the CloudWatch alarm.</p>"""
    alarm_name: "str"
    """<p>The name of the CloudWatch alarm.</p>"""
    region: "str"
    """<p>The Region of the CloudWatch alarm.</p>"""
    account_id: "str"
    """<p>The account ID that owns the CloudWatch alarm.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the source was configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObservabilityAlarmSummary) -> dict:
    out: dict = {}
    out["alarmArn"] = value["alarm_arn"]
    out["alarmName"] = value["alarm_name"]
    out["region"] = value["region"]
    out["accountId"] = value["account_id"]
    if "created_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> ObservabilityAlarmSummary:
    out: ObservabilityAlarmSummary = {}  # type: ignore[typeddict-item]
    if data.get("alarmArn") is not None:
        out["alarm_arn"] = data["alarmArn"]
    else:
        out["alarm_arn"] = ""
    if data.get("alarmName") is not None:
        out["alarm_name"] = data["alarmName"]
    else:
        out["alarm_name"] = ""
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        out["region"] = ""
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("createdAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    return out
