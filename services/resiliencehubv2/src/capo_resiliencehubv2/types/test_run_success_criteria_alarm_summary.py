"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunSuccessCriteriaAlarmSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.cloud_watch_alarm_arn
    import capo_resiliencehubv2.types.test_source_outcome


class TestRunSuccessCriteriaAlarmSummary(TypedDict, closed=True):
    alarm_arn: "capo_resiliencehubv2.types.cloud_watch_alarm_arn.CloudWatchAlarmArn"
    """<p>The ARN of the CloudWatch alarm.</p>"""
    alarm_name: "str"
    """<p>The name of the CloudWatch alarm.</p>"""
    region: "str"
    """<p>The Region of the CloudWatch alarm.</p>"""
    account_id: "str"
    """<p>The account ID that owns the CloudWatch alarm.</p>"""
    outcome: NotRequired[
        "capo_resiliencehubv2.types.test_source_outcome.TestSourceOutcome"
    ]
    """<p>The evaluation outcome of the source. Absent while the source has not yet been evaluated; set to the terminal outcome afterwards.</p>"""
    outcome_reason: NotRequired["str"]
    """<p>A human-readable reason for the outcome.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRunSuccessCriteriaAlarmSummary) -> dict:
    out: dict = {}
    out["alarmArn"] = value["alarm_arn"]
    out["alarmName"] = value["alarm_name"]
    out["region"] = value["region"]
    out["accountId"] = value["account_id"]
    if "outcome" in value:
        import capo_resiliencehubv2.types.test_source_outcome

        out["outcome"] = capo_resiliencehubv2.types.test_source_outcome.serialize_json(
            value["outcome"]
        )
    if "outcome_reason" in value:
        out["outcomeReason"] = value["outcome_reason"]
    return out


def deserialize_json(data: dict) -> TestRunSuccessCriteriaAlarmSummary:
    out: TestRunSuccessCriteriaAlarmSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("outcome") is not None:
        import capo_resiliencehubv2.types.test_source_outcome

        out["outcome"] = (
            capo_resiliencehubv2.types.test_source_outcome.deserialize_json(
                data["outcome"]
            )
        )
    if data.get("outcomeReason") is not None:
        out["outcome_reason"] = data["outcomeReason"]
    return out
