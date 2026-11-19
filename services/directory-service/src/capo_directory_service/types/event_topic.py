"""Generated from Smithy shape ``com.amazonaws.directoryservice#EventTopic``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.created_date_time
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.topic_arn
    import capo_directory_service.types.topic_name
    import capo_directory_service.types.topic_status


class EventTopic(TypedDict, closed=True):
    directory_id: NotRequired["capo_directory_service.types.directory_id.DirectoryId"]
    """<p>The Directory ID of an Directory Service directory that will publish status messages to an Amazon SNS topic.</p>"""
    topic_name: NotRequired["capo_directory_service.types.topic_name.TopicName"]
    """<p>The name of an Amazon SNS topic the receives status messages from the directory.</p>"""
    topic_arn: NotRequired["capo_directory_service.types.topic_arn.TopicArn"]
    """<p>The Amazon SNS topic ARN (Amazon Resource Name).</p>"""
    created_date_time: NotRequired[
        "capo_directory_service.types.created_date_time.CreatedDateTime"
    ]
    """<p>The date and time of when you associated your directory with the Amazon SNS topic.</p>"""
    status: NotRequired["capo_directory_service.types.topic_status.TopicStatus"]
    """<p>The topic registration status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTopic) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "topic_name" in value:
        out["TopicName"] = value["topic_name"]
    if "topic_arn" in value:
        out["TopicArn"] = value["topic_arn"]
    if "created_date_time" in value:
        import capo_directory_service.types.created_date_time

        out["CreatedDateTime"] = (
            capo_directory_service.types.created_date_time.serialize_aws_json_1_1(
                value["created_date_time"]
            )
        )
    if "status" in value:
        import capo_directory_service.types.topic_status

        out["Status"] = (
            capo_directory_service.types.topic_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventTopic:
    out: EventTopic = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("TopicName") is not None:
        out["topic_name"] = data["TopicName"]
    if data.get("TopicArn") is not None:
        out["topic_arn"] = data["TopicArn"]
    if data.get("CreatedDateTime") is not None:
        import capo_directory_service.types.created_date_time

        out["created_date_time"] = (
            capo_directory_service.types.created_date_time.deserialize_aws_json_1_1(
                data["CreatedDateTime"]
            )
        )
    if data.get("Status") is not None:
        import capo_directory_service.types.topic_status

        out["status"] = (
            capo_directory_service.types.topic_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventTopic) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "topic_name" in value:
        out["TopicName"] = value["topic_name"]
    if "topic_arn" in value:
        out["TopicArn"] = value["topic_arn"]
    if "created_date_time" in value:
        import capo_directory_service.types.created_date_time

        out["CreatedDateTime"] = (
            capo_directory_service.types.created_date_time.serialize_cbor(
                value["created_date_time"]
            )
        )
    if "status" in value:
        import capo_directory_service.types.topic_status

        out["Status"] = capo_directory_service.types.topic_status.serialize_cbor(
            value["status"]
        )
    return out


def deserialize_cbor(data: dict) -> EventTopic:
    out: EventTopic = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("TopicName") is not None:
        out["topic_name"] = data["TopicName"]
    if data.get("TopicArn") is not None:
        out["topic_arn"] = data["TopicArn"]
    if data.get("CreatedDateTime") is not None:
        import capo_directory_service.types.created_date_time

        out["created_date_time"] = (
            capo_directory_service.types.created_date_time.deserialize_cbor(
                data["CreatedDateTime"]
            )
        )
    if data.get("Status") is not None:
        import capo_directory_service.types.topic_status

        out["status"] = capo_directory_service.types.topic_status.deserialize_cbor(
            data["Status"]
        )
    return out
