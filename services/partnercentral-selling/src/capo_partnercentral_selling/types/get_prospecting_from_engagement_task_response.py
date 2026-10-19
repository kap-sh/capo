"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#GetProspectingFromEngagementTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.engagement_prospecting_result_list
    import capo_partnercentral_selling.types.prospecting_task_arn
    import capo_partnercentral_selling.types.prospecting_task_identifier
    import capo_partnercentral_selling.types.task_name


class GetProspectingFromEngagementTaskResponse(TypedDict, closed=True):
    task_id: "capo_partnercentral_selling.types.prospecting_task_identifier.ProspectingTaskIdentifier"
    """<p>The unique identifier of the task.</p>"""
    task_arn: (
        "capo_partnercentral_selling.types.prospecting_task_arn.ProspectingTaskArn"
    )
    """<p>The Amazon Resource Name (ARN) of the task.</p>"""
    task_name: "capo_partnercentral_selling.types.task_name.TaskName"
    """<p>The descriptive name of the task that you provided when you created it.</p>"""
    start_time: "capo_partnercentral_selling.types.date_time.DateTime"
    """<p>The timestamp indicating when the task was initiated. The format follows ISO 8601 date-time notation.</p>"""
    end_time: NotRequired["capo_partnercentral_selling.types.date_time.DateTime"]
    """<p>The timestamp indicating when the task finished processing. This field is absent if the task is still in progress. The format follows ISO 8601 date-time notation.</p>"""
    engagements: "capo_partnercentral_selling.types.engagement_prospecting_result_list.EngagementProspectingResultList"
    """<p>An array of <code>EngagementProspectingResult</code> entries for each engagement in the task. Each entry contains the processing status. For successfully completed engagements, includes the prospecting context identifier. For failed engagements, includes an error code and message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetProspectingFromEngagementTaskResponse) -> dict:
    out: dict = {}
    out["TaskId"] = value["task_id"]
    out["TaskArn"] = value["task_arn"]
    out["TaskName"] = value["task_name"]
    import capo_partnercentral_selling.types.date_time

    out["StartTime"] = (
        capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
            value["start_time"]
        )
    )
    if "end_time" in value:
        import capo_partnercentral_selling.types.date_time

        out["EndTime"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["end_time"]
            )
        )
    import capo_partnercentral_selling.types.engagement_prospecting_result_list

    out["Engagements"] = (
        capo_partnercentral_selling.types.engagement_prospecting_result_list.serialize_aws_json_1_0(
            value["engagements"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetProspectingFromEngagementTaskResponse:
    out: GetProspectingFromEngagementTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    else:
        out["task_id"] = ""
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    else:
        out["task_arn"] = ""
    if data.get("TaskName") is not None:
        out["task_name"] = data["TaskName"]
    else:
        out["task_name"] = ""
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
    if data.get("EndTime") is not None:
        import capo_partnercentral_selling.types.date_time

        out["end_time"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["EndTime"]
            )
        )
    if data.get("Engagements") is not None:
        import capo_partnercentral_selling.types.engagement_prospecting_result_list

        out["engagements"] = (
            capo_partnercentral_selling.types.engagement_prospecting_result_list.deserialize_aws_json_1_0(
                data["Engagements"]
            )
        )
    else:
        out["engagements"] = []
    return out
