"""Generated from Smithy shape ``com.amazonaws.freetier#GetAccountActivityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_freetier.types.activity_id
    import capo_freetier.types.activity_reward
    import capo_freetier.types.activity_status
    import capo_freetier.types.generic_string


class GetAccountActivityResponse(TypedDict, closed=True):
    activity_id: "capo_freetier.types.activity_id.ActivityId"
    """<p> A unique identifier that identifies the activity. </p>"""
    title: "capo_freetier.types.generic_string.GenericString"
    """<p> A short activity title. </p>"""
    description: "capo_freetier.types.generic_string.GenericString"
    """<p> Provides detailed information about the activity and its expected outcomes. </p>"""
    status: "capo_freetier.types.activity_status.ActivityStatus"
    """<p> The current activity status. </p>"""
    instructions_url: "capo_freetier.types.generic_string.GenericString"
    """<p> The URL resource that provides guidance on activity requirements and completion. </p>"""
    reward: "capo_freetier.types.activity_reward.ActivityReward"
    """<p> A reward granted upon activity completion. </p>"""
    estimated_time_to_complete_in_minutes: NotRequired["int"]
    """<p> The estimated time to complete the activity. This is the duration in minutes. </p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p> The time by which the activity must be completed to receive a reward. </p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the activity started. This field appears only for activities in the <code>IN_PROGRESS</code> or <code>COMPLETED</code> states. </p>"""
    completed_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the activity is completed. This field appears only for activities in the <code>COMPLETED</code> state. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAccountActivityResponse) -> dict:
    out: dict = {}
    out["activityId"] = value["activity_id"]
    out["title"] = value["title"]
    out["description"] = value["description"]
    import capo_freetier.types.activity_status

    out["status"] = capo_freetier.types.activity_status.serialize_aws_json_1_0(
        value["status"]
    )
    out["instructionsUrl"] = value["instructions_url"]
    import capo_freetier.types.activity_reward

    out["reward"] = capo_freetier.types.activity_reward.serialize_aws_json_1_0(
        value["reward"]
    )
    if "estimated_time_to_complete_in_minutes" in value:
        out["estimatedTimeToCompleteInMinutes"] = value[
            "estimated_time_to_complete_in_minutes"
        ]
    if "expires_at" in value:
        import capo_freetier._protocol.serialize

        out["expiresAt"] = capo_freetier._protocol.serialize.fmt_date_time(
            value["expires_at"]
        )
    if "started_at" in value:
        import capo_freetier._protocol.serialize

        out["startedAt"] = capo_freetier._protocol.serialize.fmt_date_time(
            value["started_at"]
        )
    if "completed_at" in value:
        import capo_freetier._protocol.serialize

        out["completedAt"] = capo_freetier._protocol.serialize.fmt_date_time(
            value["completed_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAccountActivityResponse:
    out: GetAccountActivityResponse = {}  # type: ignore[typeddict-item]
    if data.get("activityId") is not None:
        out["activity_id"] = data["activityId"]
    else:
        out["activity_id"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("status") is not None:
        import capo_freetier.types.activity_status

        out["status"] = capo_freetier.types.activity_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_freetier.types.activity_status.ActivityStatus", ""
        )
    if data.get("instructionsUrl") is not None:
        out["instructions_url"] = data["instructionsUrl"]
    else:
        out["instructions_url"] = ""
    if data.get("reward") is not None:
        import capo_freetier.types.activity_reward

        out["reward"] = capo_freetier.types.activity_reward.deserialize_aws_json_1_0(
            data["reward"]
        )
    else:
        out["reward"] = {"$unknown": {"name": ""}}
    if data.get("estimatedTimeToCompleteInMinutes") is not None:
        out["estimated_time_to_complete_in_minutes"] = data[
            "estimatedTimeToCompleteInMinutes"
        ]
    if data.get("expiresAt") is not None:
        import datetime

        out["expires_at"] = datetime.datetime.fromisoformat(
            data["expiresAt"].replace("Z", "+00:00")
        )
    if data.get("startedAt") is not None:
        import datetime

        out["started_at"] = datetime.datetime.fromisoformat(
            data["startedAt"].replace("Z", "+00:00")
        )
    if data.get("completedAt") is not None:
        import datetime

        out["completed_at"] = datetime.datetime.fromisoformat(
            data["completedAt"].replace("Z", "+00:00")
        )
    return out
