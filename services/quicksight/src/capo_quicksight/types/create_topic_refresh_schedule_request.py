"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateTopicRefreshScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.string
    import capo_quicksight.types.topic_id
    import capo_quicksight.types.topic_refresh_schedule


class CreateTopicRefreshScheduleRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the topic you're creating a refresh schedule for.</p>"""
    topic_id: "capo_quicksight.types.topic_id.TopicId"
    """<p>The ID of the topic that you want to modify. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    dataset_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset.</p>"""
    dataset_name: NotRequired["capo_quicksight.types.string.String"]
    """<p>The name of the dataset.</p>"""
    refresh_schedule: (
        "capo_quicksight.types.topic_refresh_schedule.TopicRefreshSchedule"
    )
    """<p>The definition of a refresh schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTopicRefreshScheduleRequest) -> dict:
    out: dict = {}
    out["DatasetArn"] = value["dataset_arn"]
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    import capo_quicksight.types.topic_refresh_schedule

    out["RefreshSchedule"] = (
        capo_quicksight.types.topic_refresh_schedule.serialize_json(
            value["refresh_schedule"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateTopicRefreshScheduleRequest:
    out: CreateTopicRefreshScheduleRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatasetArn") is not None:
        out["dataset_arn"] = data["DatasetArn"]
    else:
        out["dataset_arn"] = ""
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    if data.get("RefreshSchedule") is not None:
        import capo_quicksight.types.topic_refresh_schedule

        out["refresh_schedule"] = (
            capo_quicksight.types.topic_refresh_schedule.deserialize_json(
                data["RefreshSchedule"]
            )
        )
    else:
        raise DeserializationError(
            "CreateTopicRefreshScheduleRequest.refresh_schedule required"
        )
    return out
