"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ScheduledActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_redshift_serverless.types.iam_role_arn
    import capo_redshift_serverless.types.namespace_name
    import capo_redshift_serverless.types.next_invocations_list
    import capo_redshift_serverless.types.schedule
    import capo_redshift_serverless.types.scheduled_action_name
    import capo_redshift_serverless.types.state
    import capo_redshift_serverless.types.target_action


class ScheduledActionResponse(TypedDict, closed=True):
    scheduled_action_name: NotRequired[
        "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName"
    ]
    """<p>The name of the scheduled action.</p>"""
    schedule: NotRequired["capo_redshift_serverless.types.schedule.Schedule"]
    """<p>The schedule for a one-time (at timestamp format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.</p> <ul> <li> <p>Format of at timestamp is <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2016-03-04T17:27:00</code>.</p> </li> <li> <p>Format of cron expression is <code>(Minutes Hours Day-of-month Month Day-of-week Year)</code>. For example, <code>"(0 10 ? * MON *)"</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions">Cron Expressions</a> in the <i>Amazon CloudWatch Events User Guide</i>.</p> </li> </ul>"""
    scheduled_action_description: NotRequired["str"]
    """<p>The description of the scheduled action.</p>"""
    next_invocations: NotRequired[
        "capo_redshift_serverless.types.next_invocations_list.NextInvocationsList"
    ]
    """<p>An array of timestamps of when the next scheduled actions will trigger.</p>"""
    role_arn: NotRequired["capo_redshift_serverless.types.iam_role_arn.IamRoleArn"]
    """<p>The ARN of the IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift Serverless API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler to schedule creating snapshots. (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html">Using Identity-Based Policies for Amazon Redshift</a> in the Amazon Redshift Management Guide</p>"""
    state: NotRequired["capo_redshift_serverless.types.state.State"]
    """<p>The state of the scheduled action.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time of </p>"""
    target_action: NotRequired[
        "capo_redshift_serverless.types.target_action.TargetAction"
    ]
    namespace_name: NotRequired[
        "capo_redshift_serverless.types.namespace_name.NamespaceName"
    ]
    """<p>The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.</p>"""
    scheduled_action_uuid: NotRequired["str"]
    """<p>The uuid of the scheduled action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledActionResponse) -> dict:
    out: dict = {}
    if "scheduled_action_name" in value:
        out["scheduledActionName"] = value["scheduled_action_name"]
    if "schedule" in value:
        import capo_redshift_serverless.types.schedule

        out["schedule"] = (
            capo_redshift_serverless.types.schedule.serialize_aws_json_1_1(
                value["schedule"]
            )
        )
    if "scheduled_action_description" in value:
        out["scheduledActionDescription"] = value["scheduled_action_description"]
    if "next_invocations" in value:
        import capo_redshift_serverless.types.next_invocations_list

        out["nextInvocations"] = (
            capo_redshift_serverless.types.next_invocations_list.serialize_aws_json_1_1(
                value["next_invocations"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "state" in value:
        out["state"] = value["state"]
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
    if "target_action" in value:
        import capo_redshift_serverless.types.target_action

        out["targetAction"] = (
            capo_redshift_serverless.types.target_action.serialize_aws_json_1_1(
                value["target_action"]
            )
        )
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "scheduled_action_uuid" in value:
        out["scheduledActionUuid"] = value["scheduled_action_uuid"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScheduledActionResponse:
    out: ScheduledActionResponse = {}  # type: ignore[typeddict-item]
    if data.get("scheduledActionName") is not None:
        out["scheduled_action_name"] = data["scheduledActionName"]
    if data.get("schedule") is not None:
        import capo_redshift_serverless.types.schedule

        out["schedule"] = (
            capo_redshift_serverless.types.schedule.deserialize_aws_json_1_1(
                data["schedule"]
            )
        )
    if data.get("scheduledActionDescription") is not None:
        out["scheduled_action_description"] = data["scheduledActionDescription"]
    if data.get("nextInvocations") is not None:
        import capo_redshift_serverless.types.next_invocations_list

        out["next_invocations"] = (
            capo_redshift_serverless.types.next_invocations_list.deserialize_aws_json_1_1(
                data["nextInvocations"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("state") is not None:
        out["state"] = data["state"]
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
    if data.get("targetAction") is not None:
        import capo_redshift_serverless.types.target_action

        out["target_action"] = (
            capo_redshift_serverless.types.target_action.deserialize_aws_json_1_1(
                data["targetAction"]
            )
        )
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    if data.get("scheduledActionUuid") is not None:
        out["scheduled_action_uuid"] = data["scheduledActionUuid"]
    return out
