"""Generated from Smithy shape ``com.amazonaws.directoryservice#DeregisterEventTopicRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.topic_name


class DeregisterEventTopicRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The Directory ID to remove as a publisher. This directory will no longer send messages to the specified Amazon SNS topic.</p>"""
    topic_name: "capo_directory_service.types.topic_name.TopicName"
    """<p>The name of the Amazon SNS topic from which to remove the directory as a publisher.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterEventTopicRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["TopicName"] = value["topic_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterEventTopicRequest:
    out: DeregisterEventTopicRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("TopicName") is not None:
        out["topic_name"] = data["TopicName"]
    else:
        out["topic_name"] = ""
    return out
