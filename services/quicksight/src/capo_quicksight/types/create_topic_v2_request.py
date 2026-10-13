"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateTopicV2Request``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.custom_instructions
    import capo_quicksight.types.folder_arn_list
    import capo_quicksight.types.tag_list
    import capo_quicksight.types.topic_id
    import capo_quicksight.types.topic_v2_details


class CreateTopicV2Request(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that you want to create a topic in.</p>"""
    topic_id: "capo_quicksight.types.topic_id.TopicId"
    """<p>The ID for the topic that you want to create. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    topic: "capo_quicksight.types.topic_v2_details.TopicV2Details"
    """<p>The definition of a topic to create.</p>"""
    tags: NotRequired["capo_quicksight.types.tag_list.TagList"]
    """<p>Contains a map of the key-value pairs for the resource tag or tags that are assigned to the topic.</p>"""
    folder_arns: NotRequired["capo_quicksight.types.folder_arn_list.FolderArnList"]
    """<p>The Amazon Resource Names (ARNs) of the folders that you want the topic to reside in.</p>"""
    custom_instructions: NotRequired[
        "capo_quicksight.types.custom_instructions.CustomInstructions"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateTopicV2Request) -> dict:
    out: dict = {}
    out["TopicId"] = value["topic_id"]
    import capo_quicksight.types.topic_v2_details

    out["Topic"] = capo_quicksight.types.topic_v2_details.serialize_json(value["topic"])
    if "tags" in value:
        import capo_quicksight.types.tag_list

        out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    if "folder_arns" in value:
        import capo_quicksight.types.folder_arn_list

        out["FolderArns"] = capo_quicksight.types.folder_arn_list.serialize_json(
            value["folder_arns"]
        )
    if "custom_instructions" in value:
        import capo_quicksight.types.custom_instructions

        out["CustomInstructions"] = (
            capo_quicksight.types.custom_instructions.serialize_json(
                value["custom_instructions"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateTopicV2Request:
    out: CreateTopicV2Request = {}  # type: ignore[typeddict-item]
    if data.get("TopicId") is not None:
        out["topic_id"] = data["TopicId"]
    else:
        raise DeserializationError("CreateTopicV2Request.topic_id required")
    if data.get("Topic") is not None:
        import capo_quicksight.types.topic_v2_details

        out["topic"] = capo_quicksight.types.topic_v2_details.deserialize_json(
            data["Topic"]
        )
    else:
        raise DeserializationError("CreateTopicV2Request.topic required")
    if data.get("Tags") is not None:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    if data.get("FolderArns") is not None:
        import capo_quicksight.types.folder_arn_list

        out["folder_arns"] = capo_quicksight.types.folder_arn_list.deserialize_json(
            data["FolderArns"]
        )
    if data.get("CustomInstructions") is not None:
        import capo_quicksight.types.custom_instructions

        out["custom_instructions"] = (
            capo_quicksight.types.custom_instructions.deserialize_json(
                data["CustomInstructions"]
            )
        )
    return out


def redact_sensitive(value: CreateTopicV2Request) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_instructions" in value:
        import capo_quicksight.types.custom_instructions

        out["custom_instructions"] = (
            capo_quicksight.types.custom_instructions.redact_sensitive(
                value["custom_instructions"]
            )
        )
    return out
