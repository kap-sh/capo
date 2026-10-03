"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateScheduledActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_redshift_serverless.types.iam_role_arn
    import capo_redshift_serverless.types.namespace_name
    import capo_redshift_serverless.types.schedule
    import capo_redshift_serverless.types.scheduled_action_name
    import capo_redshift_serverless.types.target_action


class CreateScheduledActionRequest(TypedDict, closed=True):
    scheduled_action_name: (
        "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName"
    )
    """<p>The name of the scheduled action.</p>"""
    target_action: "capo_redshift_serverless.types.target_action.TargetAction"
    schedule: "capo_redshift_serverless.types.schedule.Schedule"
    """<p>The schedule for a one-time (at timestamp format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.</p> <ul> <li> <p>Format of at timestamp is <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2016-03-04T17:27:00</code>.</p> </li> <li> <p>Format of cron expression is <code>(Minutes Hours Day-of-month Month Day-of-week Year)</code>. For example, <code>"(0 10 ? * MON *)"</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions">Cron Expressions</a> in the <i>Amazon CloudWatch Events User Guide</i>.</p> </li> </ul>"""
    role_arn: "capo_redshift_serverless.types.iam_role_arn.IamRoleArn"
    """<p>The ARN of the IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift Serverless API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler to schedule creating snapshots. (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html">Using Identity-Based Policies for Amazon Redshift</a> in the Amazon Redshift Management Guide</p>"""
    namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName"
    """<p>The name of the namespace for which to create a scheduled action.</p>"""
    enabled: NotRequired["bool"]
    """<p>Indicates whether the schedule is enabled. If false, the scheduled action does not trigger. For more information about <code>state</code> of the scheduled action, see <a href="https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ScheduledAction.html">ScheduledAction</a>.</p>"""
    scheduled_action_description: NotRequired["str"]
    """<p>The description of the scheduled action.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateScheduledActionRequest) -> dict:
    out: dict = {}
    out["scheduledActionName"] = value["scheduled_action_name"]
    import capo_redshift_serverless.types.target_action

    out["targetAction"] = (
        capo_redshift_serverless.types.target_action.serialize_aws_json_1_1(
            value["target_action"]
        )
    )
    import capo_redshift_serverless.types.schedule

    out["schedule"] = capo_redshift_serverless.types.schedule.serialize_aws_json_1_1(
        value["schedule"]
    )
    out["roleArn"] = value["role_arn"]
    out["namespaceName"] = value["namespace_name"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateScheduledActionRequest:
    out: CreateScheduledActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("scheduledActionName") is not None:
        out["scheduled_action_name"] = data["scheduledActionName"]
    else:
        raise DeserializationError(
            "CreateScheduledActionRequest.scheduled_action_name required"
        )
    if data.get("targetAction") is not None:
        import capo_redshift_serverless.types.target_action

        out["target_action"] = (
            capo_redshift_serverless.types.target_action.deserialize_aws_json_1_1(
                data["targetAction"]
            )
        )
    else:
        raise DeserializationError(
            "CreateScheduledActionRequest.target_action required"
        )
    if data.get("schedule") is not None:
        import capo_redshift_serverless.types.schedule

        out["schedule"] = (
            capo_redshift_serverless.types.schedule.deserialize_aws_json_1_1(
                data["schedule"]
            )
        )
    else:
        raise DeserializationError("CreateScheduledActionRequest.schedule required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateScheduledActionRequest.role_arn required")
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    else:
        raise DeserializationError(
            "CreateScheduledActionRequest.namespace_name required"
        )
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
