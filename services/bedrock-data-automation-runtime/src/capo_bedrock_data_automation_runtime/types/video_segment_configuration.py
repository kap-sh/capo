"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#VideoSegmentConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_data_automation_runtime.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_data_automation_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.timestamp_segment


class VideoSegmentConfigurationTimestampSegmentMember(TypedDict, closed=True):
    timestampSegment: (
        "capo_bedrock_data_automation_runtime.types.timestamp_segment.TimestampSegment"
    )


VideoSegmentConfiguration: TypeAlias = (
    VideoSegmentConfigurationTimestampSegmentMember | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VideoSegmentConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"VideoSegmentConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "timestampSegment" in value:
        import capo_bedrock_data_automation_runtime.types.timestamp_segment

        return {
            "timestampSegment": capo_bedrock_data_automation_runtime.types.timestamp_segment.serialize_aws_json_1_1(
                value["timestampSegment"]
            )
        }
    else:
        raise SerializationError("VideoSegmentConfiguration: no variant present")


def deserialize_aws_json_1_1(data: dict) -> VideoSegmentConfiguration:
    if data.get("timestampSegment") is not None:
        import capo_bedrock_data_automation_runtime.types.timestamp_segment

        return {
            "timestampSegment": capo_bedrock_data_automation_runtime.types.timestamp_segment.deserialize_aws_json_1_1(
                data["timestampSegment"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "VideoSegmentConfiguration: no recognized variant key"
        )
