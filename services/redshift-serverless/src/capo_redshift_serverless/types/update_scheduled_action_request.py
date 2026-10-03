"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateScheduledActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_redshift_serverless.types.iam_role_arn
    import capo_redshift_serverless.types.schedule
    import capo_redshift_serverless.types.scheduled_action_name
    import capo_redshift_serverless.types.target_action


class UpdateScheduledActionRequest(TypedDict, closed=True):
    scheduled_action_name: (
        "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName"
    )
    """<p>The name of the scheduled action to update to.</p>"""
    target_action: NotRequired[
        "capo_redshift_serverless.types.target_action.TargetAction"
    ]
    schedule: NotRequired["capo_redshift_serverless.types.schedule.Schedule"]
    """<p>The schedule for a one-time (at timestamp format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.</p> <ul> <li> <p>Format of at timestamp is <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2016-03-04T17:27:00</code>.</p> </li> <li> <p>Format of cron expression is <code>(Minutes Hours Day-of-month Month Day-of-week Year)</code>. For example, <code>"(0 10 ? * MON *)"</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions">Cron Expressions</a> in the <i>Amazon CloudWatch Events User Guide</i>.</p> </li> </ul>"""
    role_arn: NotRequired["capo_redshift_serverless.types.iam_role_arn.IamRoleArn"]
    """<p>The ARN of the IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift Serverless API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler to schedule creating snapshots (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html">Using Identity-Based Policies for Amazon Redshift</a> in the Amazon Redshift Management Guide</p>"""
    enabled: NotRequired["bool"]
    """<p>Specifies whether to enable the scheduled action.</p>"""
    scheduled_action_description: NotRequired["str"]
    """<p>The descripion of the scheduled action to update to.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start time in UTC of the scheduled action to update to.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time in UTC of the scheduled action to update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateScheduledActionRequest) -> dict:
    out: dict = {}
    out["scheduledActionName"] = value["scheduled_action_name"]
    if "target_action" in value:
        import capo_redshift_serverless.types.target_action

        out["targetAction"] = (
            capo_redshift_serverless.types.target_action.serialize_aws_json_1_1(
                value["target_action"]
            )
        )
    if "schedule" in value:
        import capo_redshift_serverless.types.schedule

        out["schedule"] = (
            capo_redshift_serverless.types.schedule.serialize_aws_json_1_1(
                value["schedule"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "scheduled_action_description" in value:
        out["scheduledActionDescription"] = value["scheduled_action_description"]
    if "start_time" in value:
        import capo_redshift_serverless.types._prelude.timestamp

        out["startTime"] = (
            capo_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import capo_redshift_serverless.types._prelude.timestamp

        out["endTime"] = (
            capo_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["end_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateScheduledActionRequest:
    out: UpdateScheduledActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("scheduledActionName") is not None:
        out["scheduled_action_name"] = data["scheduledActionName"]
    else:
        raise DeserializationError(
            "UpdateScheduledActionRequest.scheduled_action_name required"
        )
    if data.get("targetAction") is not None:
        import capo_redshift_serverless.types.target_action

        out["target_action"] = (
            capo_redshift_serverless.types.target_action.deserialize_aws_json_1_1(
                data["targetAction"]
            )
        )
    if data.get("schedule") is not None:
        import capo_redshift_serverless.types.schedule

        out["schedule"] = (
            capo_redshift_serverless.types.schedule.deserialize_aws_json_1_1(
                data["schedule"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("scheduledActionDescription") is not None:
        out["scheduled_action_description"] = data["scheduledActionDescription"]
    if data.get("startTime") is not None:
        import capo_redshift_serverless.types._prelude.timestamp

        out["start_time"] = (
            capo_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["startTime"]
            )
        )
    if data.get("endTime") is not None:
        import capo_redshift_serverless.types._prelude.timestamp

        out["end_time"] = (
            capo_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["endTime"]
            )
        )
    return out
