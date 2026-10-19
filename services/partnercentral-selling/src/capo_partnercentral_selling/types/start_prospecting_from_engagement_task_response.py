"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#StartProspectingFromEngagementTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.engagement_identifier_list
    import capo_partnercentral_selling.types.prospecting_task_arn
    import capo_partnercentral_selling.types.prospecting_task_identifier
    import capo_partnercentral_selling.types.prospecting_task_status
    import capo_partnercentral_selling.types.task_name


class StartProspectingFromEngagementTaskResponse(TypedDict, closed=True):
    identifiers: "capo_partnercentral_selling.types.engagement_identifier_list.EngagementIdentifierList"
    """<p>The list of engagement identifiers that were accepted into the task queue for processing. This list matches the identifiers provided in the request.</p>"""
    task_name: "capo_partnercentral_selling.types.task_name.TaskName"
    """<p>The task name from the request.</p>"""
    message: NotRequired["str"]
    """<p>A message providing additional context about the task's current state. When the task fails, this field contains a detailed description of the failure and suggested recovery steps. This field is only populated for tasks in a failed state.</p>"""
    reason_code: NotRequired["str"]
    """<p>An enumerated code identifying the reason for task failure. This field is only populated when the task has failed. Use the corresponding <code>Message</code> field for a human-readable description of the failure.</p>"""
    start_time: "capo_partnercentral_selling.types.date_time.DateTime"
    """<p>The timestamp indicating when the task was initiated. The format follows ISO 8601 date-time notation.</p>"""
    task_id: NotRequired[
        "capo_partnercentral_selling.types.prospecting_task_identifier.ProspectingTaskIdentifier"
    ]
    """<p>The unique identifier assigned to this task. Use this identifier with <code>GetProspectingFromEngagementTask</code> to retrieve task details and check status.</p>"""
    task_arn: NotRequired[
        "capo_partnercentral_selling.types.prospecting_task_arn.ProspectingTaskArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the task. The ARN uniquely identifies the task across AWS and can be used for resource-level IAM policies.</p>"""
    task_status: "capo_partnercentral_selling.types.prospecting_task_status.ProspectingTaskStatus"
    """<p>The current status of the task. Possible values: <code>PENDING</code> (waiting to run), <code>IN_PROGRESS</code> (actively processing), <code>COMPLETED</code> (successfully processed), and <code>FAILED</code> (unrecoverable error).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartProspectingFromEngagementTaskResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_selling.types.engagement_identifier_list

    out["Identifiers"] = (
        capo_partnercentral_selling.types.engagement_identifier_list.serialize_aws_json_1_0(
            value["identifiers"]
        )
    )
    out["TaskName"] = value["task_name"]
    if "message" in value:
        out["Message"] = value["message"]
    if "reason_code" in value:
        out["ReasonCode"] = value["reason_code"]
    import capo_partnercentral_selling.types.date_time

    out["StartTime"] = (
        capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
            value["start_time"]
        )
    )
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    import capo_partnercentral_selling.types.prospecting_task_status

    out["TaskStatus"] = (
        capo_partnercentral_selling.types.prospecting_task_status.serialize_aws_json_1_0(
            value["task_status"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartProspectingFromEngagementTaskResponse:
    out: StartProspectingFromEngagementTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("Identifiers") is not None:
        import capo_partnercentral_selling.types.engagement_identifier_list

        out["identifiers"] = (
            capo_partnercentral_selling.types.engagement_identifier_list.deserialize_aws_json_1_0(
                data["Identifiers"]
            )
        )
    else:
        out["identifiers"] = []
    if data.get("TaskName") is not None:
        out["task_name"] = data["TaskName"]
    else:
        out["task_name"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ReasonCode") is not None:
        out["reason_code"] = data["ReasonCode"]
    if data.get("StartTime") is not None:
        import capo_partnercentral_selling.types.date_time

        out["start_time"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["StartTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    if data.get("TaskStatus") is not None:
        import capo_partnercentral_selling.types.prospecting_task_status

        out["task_status"] = (
            capo_partnercentral_selling.types.prospecting_task_status.deserialize_aws_json_1_0(
                data["TaskStatus"]
            )
        )
    else:
        import typing

        out["task_status"] = typing.cast(
            "capo_partnercentral_selling.types.prospecting_task_status.ProspectingTaskStatus",
            "",
        )
    return out
