"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetProfileUpdateTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.date_time
    import capo_partnercentral_account.types.error_detail_list
    import capo_partnercentral_account.types.partner_arn
    import capo_partnercentral_account.types.partner_id
    import capo_partnercentral_account.types.profile_task_id
    import capo_partnercentral_account.types.profile_task_status
    import capo_partnercentral_account.types.task_details


class GetProfileUpdateTaskResponse(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    arn: "capo_partnercentral_account.types.partner_arn.PartnerArn"
    """<p>The Amazon Resource Name (ARN) of the profile update task.</p>"""
    id: "capo_partnercentral_account.types.partner_id.PartnerId"
    """<p>The unique identifier of the partner account.</p>"""
    task_id: "capo_partnercentral_account.types.profile_task_id.ProfileTaskId"
    """<p>The unique identifier of the profile update task.</p>"""
    task_details: "capo_partnercentral_account.types.task_details.TaskDetails"
    """<p>The details of the profile update task including what changes are being made.</p>"""
    started_at: "capo_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the profile update task was started.</p>"""
    status: "capo_partnercentral_account.types.profile_task_status.ProfileTaskStatus"
    """<p>The current status of the profile update task (in progress, completed, failed, etc.).</p>"""
    ended_at: NotRequired["capo_partnercentral_account.types.date_time.DateTime"]
    """<p>The timestamp when the profile update task was completed or failed.</p>"""
    error_detail_list: NotRequired[
        "capo_partnercentral_account.types.error_detail_list.ErrorDetailList"
    ]
    """<p>A list of error details if any errors occurred during the profile update task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetProfileUpdateTaskResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Arn"] = value["arn"]
    out["Id"] = value["id"]
    out["TaskId"] = value["task_id"]
    import capo_partnercentral_account.types.task_details

    out["TaskDetails"] = (
        capo_partnercentral_account.types.task_details.serialize_aws_json_1_0(
            value["task_details"]
        )
    )
    import capo_partnercentral_account.types.date_time

    out["StartedAt"] = (
        capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["started_at"]
        )
    )
    import capo_partnercentral_account.types.profile_task_status

    out["Status"] = (
        capo_partnercentral_account.types.profile_task_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "ended_at" in value:
        import capo_partnercentral_account.types.date_time

        out["EndedAt"] = (
            capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
                value["ended_at"]
            )
        )
    if "error_detail_list" in value:
        import capo_partnercentral_account.types.error_detail_list

        out["ErrorDetailList"] = (
            capo_partnercentral_account.types.error_detail_list.serialize_aws_json_1_0(
                value["error_detail_list"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetProfileUpdateTaskResponse:
    out: GetProfileUpdateTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    else:
        out["task_id"] = ""
    if data.get("TaskDetails") is not None:
        import capo_partnercentral_account.types.task_details

        out["task_details"] = (
            capo_partnercentral_account.types.task_details.deserialize_aws_json_1_0(
                data["TaskDetails"]
            )
        )
    else:
        raise DeserializationError("GetProfileUpdateTaskResponse.task_details required")
    if data.get("StartedAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["started_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["StartedAt"]
            )
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Status") is not None:
        import capo_partnercentral_account.types.profile_task_status

        out["status"] = (
            capo_partnercentral_account.types.profile_task_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_partnercentral_account.types.profile_task_status.ProfileTaskStatus",
            "",
        )
    if data.get("EndedAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["ended_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["EndedAt"]
            )
        )
    if data.get("ErrorDetailList") is not None:
        import capo_partnercentral_account.types.error_detail_list

        out["error_detail_list"] = (
            capo_partnercentral_account.types.error_detail_list.deserialize_aws_json_1_0(
                data["ErrorDetailList"]
            )
        )
    return out
