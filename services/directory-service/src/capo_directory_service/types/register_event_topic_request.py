"""Generated from Smithy shape ``com.amazonaws.directoryservice#RegisterEventTopicRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.topic_name


class RegisterEventTopicRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The Directory ID that will publish status messages to the Amazon SNS topic.</p>"""
    topic_name: "capo_directory_service.types.topic_name.TopicName"
    """<p>The Amazon SNS topic name to which the directory will publish status messages. This Amazon SNS topic must be in the same region as the specified Directory ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterEventTopicRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["TopicName"] = value["topic_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterEventTopicRequest:
    out: RegisterEventTopicRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("TopicName") is not None:
        out["topic_name"] = data["TopicName"]
    else:
        out["topic_name"] = ""
    return out
